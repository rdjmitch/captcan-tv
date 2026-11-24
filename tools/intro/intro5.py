import numpy as np, cv2, os, glob, sys
from PIL import Image
OPT=os.environ.get('OPT','A'); OUT='i5f_'+OPT; os.makedirs(OUT,exist_ok=True)
FPS=30; A0=16.64; DUR=18.0; N=int(FPS*DUR); W,H=1920,1080
CA=[16.64,17.07,17.43,17.94,18.17,18.36,18.62,18.92,19.11,19.35,19.74,20.04,20.24,20.53,20.75,21.16,21.37,21.51,21.91,22.19,22.74,22.91,23.09,
    23.46,23.89,24.14,24.51,24.92,25.36,25.66,26.06,26.24,26.51,26.64,26.78,26.90,27.00]+([27.10,27.47,28.11,28.39,29.00,29.50,29.77] if OPT=='D' else [])
CUTS=[c-A0 for c in CA]
T_IN=23.09-A0; T_HIT=27.10-A0; T_NEON=30.48-A0; T_CATCH=31.27-A0; T_CA=32.02-A0
T_WHITE=T_NEON if OPT=='D' else T_HIT
if OPT=='D': T_IN=T_HIT
PULSE=[27.47-A0,28.39-A0,29.00-A0]; NP=[32.47-A0,32.77-A0]
# ---- art
def fit(im):
    h,w=im.shape[:2]; k=max(W/w,H/h); im=cv2.resize(im,(int(w*k+1),int(h*k+1)),interpolation=cv2.INTER_CUBIC if k>1 else cv2.INTER_AREA)
    y=(im.shape[0]-H)//2; x=(im.shape[1]-W)//2; return im[y:y+H,x:x+W].astype(np.float32)
arts=[fit(cv2.cvtColor(cv2.imread(f),cv2.COLOR_BGR2RGB)) for f in sorted(glob.glob('i3/pack/art_*.jpg'))]
for n in ['d10','s07','d11','s06','d04','s03','d08','s12','d12','s14','x01','d06','s05']:
    im=cv2.cvtColor(cv2.imread(f'tv/books/{n}.jpg'),cv2.COLOR_BGR2RGB); h,w=im.shape[:2]; im=im[int(h*.03):int(h*.97),int(w*.05):int(w*.95)]
    k=W/im.shape[1]; im=cv2.resize(im,(W,int(im.shape[0]*k)),interpolation=cv2.INTER_CUBIC); y=int(im.shape[0]*0.2); arts.append(im[y:y+H].astype(np.float32))
order=list(range(len(arts)))
# ---- logo
text=np.load('intro/text.npy'); leaf=np.load('intro/leaf.npy')
al=np.array(Image.open('intro/newlogo_t.png'))[...,3].astype(np.float32)/255
TXT=(al*text).astype(np.float32); LEAF=(al*leaf).astype(np.float32); lh,lw=al.shape; S=0.74
ca_im=np.array(Image.open('intro/logo_white_ca.png').convert('RGBA')); ca_a=ca_im[:,1905:,3].astype(np.float32)/255
ys,xs=np.where(ca_a>0.05); ca_a=ca_a[ys.min():ys.max()+1,xs.min():xs.max()+1]; ca_top=ys.min(); ys2,_=np.where(al>0.05); logo_top=ys2.min()
ca_s=cv2.resize(ca_a,(int(ca_a.shape[1]*S),int(ca_a.shape[0]*S)),interpolation=cv2.INTER_AREA); GAP=int(14*S)
dt=cv2.distanceTransform((TXT>0.5).astype(np.uint8),cv2.DIST_L2,5); fy,fx=np.unravel_index(dt.argmax(),dt.shape); R=dt.max()
S0=1250/(R*S); F0=np.array([fx,fy],np.float32); FC=np.array([lw/2,lh/2],np.float32)
print('stroke r',R,'S0',S0,'focal',fx,fy)
def warp(a,k,f,dx=0):
    M=np.float32([[k,0,W/2-f[0]*k+dx],[0,k,H/2-f[1]*k]]); o=cv2.warpAffine(a,M,(W,H),flags=cv2.INTER_AREA if k<1 else cv2.INTER_LINEAR)
    if k>1.5: o=np.clip((o-0.5)*min(k/1.5,12)+0.5,0,1)
    return o
yy,xx=np.mgrid[0:H,0:W].astype(np.float32); r=np.sqrt(((xx-W/2)/(W*0.62))**2+((yy-H*0.48)/(H*0.75))**2); base=np.clip(1-r,0,1)**1.4
BG=np.dstack([18+52*base,0+2*base,2+5*base]).astype(np.float32); BLOOM=np.dstack([120*base,10*base,14*base]).astype(np.float32)
VIG=(0.82+0.18*np.clip(1-r*0.7,0,1))[...,None]
# final-layout neon glow (precomputed, shifted when the logo slides)
LF=warp(LEAF,S,FC); TF=warp(TXT,S,FC)
G=np.clip(cv2.GaussianBlur(LF,(0,0),4)*1.6+cv2.GaussianBlur(LF,(0,0),16)*2.2+cv2.GaussianBlur(LF,(0,0),70)*5.4+cv2.GaussianBlur(LF,(0,0),220)*5.4,0,5)
CORE=np.clip(cv2.GaussianBlur(cv2.dilate(LF,np.ones((2,2),np.uint8)),(0,0),1.0)*1.3,0,1)
def sh(a,dx):
    if dx==0: return a
    o=np.zeros_like(a); o[:,:W+dx]=a[:,-dx:]; return o
eo=lambda x:1-(1-x)**3
def ease_back(x): c1=2.2;c3=c1+1;return 1+c3*(x-1)**3+c1*(x-1)**2
def neon(t):
    if t<0: return 0.0
    k=(T_CATCH-T_NEON)/0.5; seq=[(0.00,0.0),(0.06,0.9),(0.10,0.05),(0.18,0.7),(0.22,0.1),(0.30,0.0),(0.40,1.0),(0.44,0.35),(0.50,1.0)]
    v=0.0
    for a,b in seq:
        if t>=a*k: v=b
    if t>=0.5*k: v=1.0+0.04*np.sin(t*37)+0.03*np.sin(t*91)
    return v
def pages(t):
    i=max(j for j,c in enumerate(CUTS) if t>=c) if t>=CUTS[0] else 0
    cur=arts[order[i%len(arts)]]; u=(t-CUTS[i])/0.12
    if i==0: return cur*min(1,t/0.2)
    if u>=1: return cur
    prev=arts[order[(i-1)%len(arts)]]; e=eo(u); y=int(H*(1-e)); out=prev.copy()
    if y<H:
        k=int(90*(1-u))|1; new=cv2.blur(cur,(1,k)) if k>3 else cur
        out[y:]=new[:H-y]; 
        if y>6: out[max(0,y-40):y]*=np.linspace(1,0.45,min(40,y))[:,None,None]   # shadow under the turning page
    return out
rng=np.random.default_rng(3)
F=range(N) if len(sys.argv)<2 else [int(x) for x in sys.argv[1].split(',')]
for f in F:
    t=f/FPS
    art=pages(min(t,T_WHITE)) if t<T_WHITE+0.4 else None
    if OPT=='C' and art is not None:
        wa=1-np.clip((t-T_IN)/0.7,0,1)
        if wa>0:
            g=(art@np.float32([0.3,0.59,0.11]))[...,None]/255; rw=np.float32([60,4,8])*(1-g)+np.float32([255,70,60])*g; art=art*(1-wa)+rw*wa
    if t<T_IN: img=art
    else:
        u=min(1,(t-T_IN)/max(1e-6,T_HIT-T_IN)); uu=1-(1-u)**1.35; s=float(np.exp(np.log(S0)*(1-uu)))
        if OPT=='D':
            v=t-T_HIT; u=1.0 if v>=0.4 else 0.5; s=1+0.35*(1-v/0.4)**3 if v<0.4 else 1.0
        w=(1/s-1/S0)/(1-1/S0); fpt=F0+(FC-F0)*w
        kk=np.clip((t-T_CA)/0.4,0,1); kk=kk*kk*(3-2*kk); dx=-int(kk*(ca_s.shape[1]+GAP)/2)
        if u<1: A_t=warp(TXT,S*s,fpt); A_l=warp(LEAF,S*s,fpt); core=A_l; glow=None
        else: A_t=sh(TF,dx); A_l=sh(LF,dx); core=sh(CORE,dx)
        img=BG.copy()
        for p in PULSE:
            if t>=p: img+=BLOOM*0.5*np.exp(-(t-p)*4)
        if t>=T_HIT: img+=BLOOM*0.9*np.exp(-(t-T_HIT)*2.2)
        n=neon(t-T_NEON)
        for p in NP:
            if t>=p: n+=0.3*np.exp(-(t-p)*7)
        if n>0:
            g=sh(G,dx)*n; img+=np.dstack([255*g*0.55,20*g*0.4,30*g*0.4])
        # soft shadow under the letters once the logo is on screen
        if s<6:
            sd=cv2.GaussianBlur(np.maximum(A_t,A_l),(0,0),10*min(s,2)); M=np.float32([[1,0,0],[0,1,10*min(s,2)]]); sd=cv2.warpAffine(sd,M,(W,H))
            img*=(1-0.55*sd*(1 if n<=0 else max(0.3,1-n)))[...,None]
        white=np.array([255,248,246],np.float32)*1.0
        m=max(np.clip((t-T_WHITE)/0.18,0,1),0 if OPT=='D' else 0.45*np.clip((u-0.7)/0.3,0,1))
        fill=white if art is None else np.clip(art*1.15+18,0,255)*(1-m)+white*m
        img=img*(1-A_t[...,None])+fill*A_t[...,None]
        on=min(max(n,0),1.0); col=np.array([70,8,12])*(1-on)+np.array([255,205,210])*on
        img=img*(1-core[...,None])+col*core[...,None]
        if t>=T_CA:
            v=t-T_CA; sc=ease_back(min(v/0.38,1.0)) if v<0.38 else 1.0+0.06*np.exp(-(v-0.38)*9)*np.sin((v-0.38)*28)
            sy=sc*(1+0.18*np.exp(-v*10)*np.sin(v*30)); sx=sc*(1-0.12*np.exp(-v*10)*np.sin(v*30))
            if sc>0.02:
                ch,cw=ca_s.shape; a=cv2.resize(ca_s,(max(1,int(cw*sx)),max(1,int(ch*sy))))
                x_logo=int((W-lw*S)/2)+dx; y_logo=int((H-lh*S)/2); cx=x_logo+int(lw*S)+GAP+cw//2
                by=y_logo+int((ca_top-logo_top)*S)+ch; x0=cx-a.shape[1]//2; y0=by-a.shape[0]-int(18*max(0,np.sin(min(v/0.38,1)*np.pi)))
                A=np.zeros((H,W),np.float32); A[y0:y0+a.shape[0],x0:x0+a.shape[1]]=a
                img=img*(1-A[...,None])+np.array([255,250,248])*A[...,None]
        if t>=T_HIT: img+=255*0.5*np.exp(-(t-T_HIT)*9)
        if OPT=='D' and t>=T_WHITE: img+=255*0.3*np.exp(-(t-T_WHITE)*9)
    img=img*VIG+rng.normal(0,2.0,(H,W,1))
    img*=np.clip((DUR-t)/0.8,0,1)
    Image.fromarray(np.clip(img,0,255).astype(np.uint8)).save(f'{OUT}/{f:04d}.jpg',quality=93)
print('done')
