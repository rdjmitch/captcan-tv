import re,json,io,base64,subprocess,sys
from PIL import Image
s=open('/home/claude/captcan-tv/index.html').read()
j=json.loads(s[s.find('>',129201)+1:s.find('</script>',129201)])
f,m=j['feed'],j['market']
clips=json.loads(re.sub(r'([{,])([a-z]+):',r'\1"\2":',re.search(r'const CLIPS=(\[.*?\]);const TRU',s).group(1)))
for t in m['trailers']: clips.insert(0,{"id":t['id'],"ty":"t","t":t['t'],"sub":t['sub'],"kw":t.get('kw','')})
names=json.loads(re.sub(r'([{,])([a-zA-Z0-9]+):',r'\1"\2":',re.search(r'const NAMES=(\{.*?\});',s).group(1)))
def b64(im,w,q=62):
    im=im.convert('RGB'); im.thumbnail((w,w*2)); b=io.BytesIO(); im.save(b,'JPEG',quality=q); return 'data:image/jpeg;base64,'+base64.b64encode(b.getvalue()).decode()
reels=[]
for k,n,d in [("doom","Doom",23),("batman","Absolute Batman",25.5),("midnight","Midnight",25.4),("blacksuit","Black Suit",23)]:
    reels.append({"k":k,"n":n,"d":d,"img":b64(Image.open(f'/home/claude/captcan-tv/v/{k}.jpg'),360)})
books={}
def add(lst,src):
    for b in lst:
        t=b.get('title') or b.get('t'); 
        if t and b.get('img') and t not in books: books[t]={"t":t,"p":b.get('price'),"u":b['img'],"src":src}
add(f['hot'],'Hot this week'); add(f['keys'],'Just landed'); add(f['inc'],'Incentive covers'); add(f['trades'],'Trades'); add(f['run']['items'],"Friday's run"); add(f['soon'],'Coming soon'); add(f['blow'],'Blowout'); add(f.get('monk',[]),'Monk'); add(f.get('merch',[]),'Merch')
bl=list(books.values())
pri=lambda b: 0 if re.search(r'Doom|Batman|Spider|Hulk|X-Men',b['t']) else 1
bl.sort(key=pri); bl=bl[:44]
import urllib.request
out=[]
for b in bl:
    try:
        u=b['u']+('&' if '?' in b['u'] else '?')+'width=150'
        raw=subprocess.run(['curl','-s','-m','20',u],capture_output=True).stdout
        b['img']=b64(Image.open(io.BytesIO(raw)),130,58); del b['u']; out.append(b)
    except Exception as e: print('skip',b['t'],e,file=sys.stderr)
D={"build":re.search(r'BUILD="([^"]+)"',s).group(1),"asOf":f['asOf'],"newLabel":f['newLabel'],"clips":clips,"reels":reels,"books":out,"older":names}
json.dump(D,open('data.json','w'))
print(len(out),'books',len(clips),'clips',len(json.dumps(D))//1024,'KB')
print([b['t'] for b in out if pri(b)==0])
