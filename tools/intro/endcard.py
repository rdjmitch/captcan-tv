import numpy as np, cv2, os
from PIL import Image
OUT='endf'; os.makedirs(OUT, exist_ok=True)
FPS=24; DUR=4.6; N=int(FPS*DUR)
W,H=1920,1080
text=np.load('intro/text.npy'); leaf=np.load('intro/leaf.npy')
al=np.array(Image.open('intro/newlogo_t.png'))[...,3].astype(np.float32)/255
# .ca glyphs from the composed logo (right part beyond the S)
ca_im=np.array(Image.open('intro/logo_white_ca.png').convert('RGBA'))
ca_a=ca_im[:,1905:,3].astype(np.float32)/255   # just the ".ca"
ys,xs=np.where(ca_a>0.05); ca_a=ca_a[ys.min():ys.max()+1, xs.min():xs.max()+1]; ca_top=ys.min()
ys2,_=np.where(al>0.05); logo_top=ys2.min()
S=0.74                     # logo scale on screen
lh,lw=al.shape
txt_a=cv2.resize(al*text,(int(lw*S),int(lh*S)),interpolation=cv2.INTER_AREA)
leaf_a=cv2.resize(al*leaf,(int(lw*S),int(lh*S)),interpolation=cv2.INTER_AREA)
ca_s=cv2.resize(ca_a,(int(ca_a.shape[1]*S),int(ca_a.shape[0]*S)),interpolation=cv2.INTER_AREA)
GAP=int(14*S)
# background: deep red radial like the 3D end frame
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
r=np.sqrt(((xx-W/2)/(W*0.62))**2+((yy-H*0.48)/(H*0.75))**2)
base=np.clip(1-r,0,1)**1.4
BG=np.dstack([18+52*base, 0+2*base, 2+5*base]).astype(np.float32)   # RGB
rng=np.random.default_rng(3)
def place(canvas_a, a, x, y):
    h,w=a.shape; x0,y0=max(0,x),max(0,y); x1,y1=min(W,x+w),min(H,y+h)
    if x1<=x0 or y1<=y0: return
    canvas_a[y0:y1,x0:x1]=np.maximum(canvas_a[y0:y1,x0:x1],a[y0-y:y1-y,x0-x:x1-x])
def ease_back(x):  # overshoot
    c1=2.2; c3=c1+1; return 1+c3*(x-1)**3+c1*(x-1)**2
def neon(t):
    # ignition: stutter, then catch, then settle with a slight hum
    seq=[(0.00,0.0),(0.06,0.9),(0.10,0.05),(0.18,0.7),(0.22,0.1),(0.30,0.0),(0.40,1.0),(0.44,0.35),(0.50,1.0)]
    if t<0: return 0.0
    v=0.0
    for a,b in seq:
        if t>=a: v=b
    if t>=0.5: v=1.0+0.04*np.sin(t*37)+0.03*np.sin(t*91)
    return v
T_NEON=0.55; T_CA=2.35
for f in range(N):
    t=f/FPS
    img=BG.copy()
    # logo layout: centred without .ca, slides left as .ca arrives
    k=np.clip((t-T_CA)/0.45,0,1); k=k*k*(3-2*k)
    total_w=txt_a.shape[1]; ca_w=ca_s.shape[1]+GAP
    x_logo=int((W-total_w)/2 - k*ca_w/2); y_logo=int((H-txt_a.shape[0])/2)
    A_txt=np.zeros((H,W),np.float32); A_leaf=np.zeros((H,W),np.float32); A_ca=np.zeros((H,W),np.float32)
    place(A_txt,txt_a,x_logo,y_logo); place(A_leaf,leaf_a,x_logo,y_logo)
    n=neon(t-T_NEON)
    # neon glow layers (light spills on the wall and the letters)
    if n>0:
        g1=cv2.GaussianBlur(A_leaf,(0,0),4)*1.6
        g2=cv2.GaussianBlur(A_leaf,(0,0),16)*2.2
        g3=cv2.GaussianBlur(A_leaf,(0,0),70)*6.0;g4=cv2.GaussianBlur(A_leaf,(0,0),220)*9.0
        glow=np.clip(g1*1.0+g2*1.0+g3*0.9+g4*0.6,0,5)*n
        img+=np.dstack([255*glow*0.55, 20*glow*0.4, 30*glow*0.4])
    # letters: white, warmed by the neon
    tint=np.array([255,248,246])*(0.93+0.07*min(n,1))
    img=img*(1-A_txt[...,None])+tint*A_txt[...,None]
    # neon tube: hot pink-white core with red edge when on, dark red glass when off
    on=min(max(n,0),1.2)
    core=np.clip(cv2.GaussianBlur(cv2.dilate(A_leaf,np.ones((2,2),np.uint8)),(0,0),1.0)*1.3,0,1)
    tube_on=np.array([255,205,210]); tube_off=np.array([70,8,12])
    col=tube_off*(1-min(on,1))+tube_on*min(on,1)
    img=img*(1-core[...,None])+col*core[...,None]
    # .ca: Pixar-style pop (squash and stretch, overshoot, settle)
    if t>=T_CA:
        u=(t-T_CA)
        s=ease_back(min(u/0.38,1.0)) if u<0.38 else 1.0+0.06*np.exp(-(u-0.38)*9)*np.sin((u-0.38)*28)
        sy=s*(1+0.18*np.exp(-u*10)*np.sin(u*30)); sx=s*(1-0.12*np.exp(-u*10)*np.sin(u*30))
        if s>0.02:
            ch,cw=ca_s.shape
            a=cv2.resize(ca_s,(max(1,int(cw*sx)),max(1,int(ch*sy))),interpolation=cv2.INTER_LINEAR)
            cx=x_logo+total_w+GAP+cw//2
            base_y=y_logo+int((ca_top-logo_top)*S)+ch   # baseline anchored (pops up from the line)
            place(A_ca,a,cx-a.shape[1]//2,base_y-a.shape[0] - int(18*max(0,np.sin(min(u/0.38,1)*np.pi))))
            img=img*(1-A_ca[...,None])+np.array([255,250,248])*A_ca[...,None]
    # vignette + fine grain
    img*= (0.82+0.18*np.clip(1-r*0.7,0,1))[...,None]
    img+=rng.normal(0,2.2,(H,W,1))
    # fade out at the very end
    img*=np.clip((DUR-t)/0.5,0,1)
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(f'{OUT}/{f:04d}.jpg',quality=94)
print('frames',N)
