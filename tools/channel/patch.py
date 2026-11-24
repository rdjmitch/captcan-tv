import re,sys
src=open('/home/claude/captcan-tv/index.html').read()
s=src
def rep(a,b,count=1):
    global s
    n=s.count(a)
    assert n>=1 and (count is None or n==count), (a[:70],n)
    s=s.replace(a,b)
def between(start,end,new):
    global s
    i=s.index(start); j=s.index(end,i)
    s=s[:i]+new+s[j:]

BUILD=sys.argv[1]
s=re.sub(r'const BUILD="[^"]+"','const BUILD="%s"'%BUILD,s,1)

# ---------- CSS: two preload players instead of one ----------
assert s.count('#ytpre')>=10
s=s.replace('#ytpre','.ytpre')

# ---------- the channel programmer ----------
CH=r'''/* ===== the channel: programmed blocks =====
   A block is a run of slots. Each kind of slot draws from its own shuffled bag, so nothing repeats until everything
   else of its kind has played (the bags survive a reload). A kind with no approved screens yet is skipped, so the
   intro, ident, product and own-reel slots are ready and simply stay empty until screens are approved into SCREENS. */
const LEADTR="Wb8Tq_HD4E8";/* Avengers: Doomsday final trailer: takes every other trailer slot until it leaves the trailer list */
const BLOCKS=[["intro","ident","reel","trl","c","product","reel","s","k","own"],["ident","reel","c","s","product","reel","trl","c","own"]];
const KINDS={intro:"Main intro",ident:"CaptCan ident",reel:"Art reel",trl:"Trailer",c:"Cartoon opening",s:"Movie scene",k:"Talking clip",product:"Product screen",own:"Our own reels"};
const KSEC={intro:20,ident:8,reel:24,trl:150,c:65,s:140,k:190,product:15,own:40};
const ISCLIP={trl:1,c:1,s:1,k:1};
const SCREENS={intro:[],ident:[],product:[],own:[]};/* approved screens: {id,n,fn:()=>scene} */
const CH={n:0,trn:0,bag:{},bench:{},rb:false,st:{shown:0,fill:0,skip:0,stall:0,bad:{},waits:[],err:""},
  load(){try{const o=JSON.parse(localStorage.getItem("cctvCh")||"null");if(o){this.n=o.n||0;this.trn=o.trn||0;this.bag=o.bag||{};}}catch(x){}},
  save(){try{localStorage.setItem("cctvCh",JSON.stringify({n:this.n,trn:this.trn,bag:this.bag}));}catch(x){}},
  pool(kind){const ok=x=>x&&x.id&&liveT(x)&&!(this.bench[x.id]>Date.now());
    if(kind==="reel")return REELS.map(r=>({id:r.k,r}));
    if(kind==="trl")return ((MARKET&&MARKET.trailers)||[]).filter(ok);
    if(ISCLIP[kind])return CLIPS.filter(c=>c.ty===kind).filter(ok);
    return SCREENS[kind]||[];},
  draw(kind,pool){pool=pool||this.pool(kind);if(!pool.length)return null;const ids=pool.map(x=>x.id),b=this.bag[kind]=this.bag[kind]||{left:[],last:""};
    b.left=(b.left||[]).filter(i=>ids.includes(i));
    if(!b.left.length){b.left=ids.slice();for(let i=b.left.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[b.left[i],b.left[j]]=[b.left[j],b.left[i]];}
      if(b.left.length>1&&b.left[0]===b.last)b.left.push(b.left.shift());}
    b.last=b.left.shift();return pool.find(x=>x.id===b.last);},
  item(kind){if(kind==="trl"){const p=this.pool("trl"),lead=p.find(x=>x.id===LEADTR),rest=p.filter(x=>x.id!==LEADTR);
      if(lead&&(this.trn++%2===0||!rest.length))return lead;return this.draw("trl",rest);}
    return this.draw(kind);},
  block(){const tpl=BLOCKS[this.n++%BLOCKS.length],out=[];
    tpl.forEach(kind=>{if(TRON===false&&ISCLIP[kind])return;const it=this.item(kind);if(!it)return;const slot={kind,it,tries:0};const f=()=>CH.play(slot,f);f.slot=slot;out.push(f);});
    this.save();return out;},
  /* the next two clips that will play; tops the queue up early so the first clip of the next block can load ahead too */
  plan(){const clips=()=>queue.filter(q=>q.slot&&ISCLIP[q.slot.kind]&&!(this.bench[q.slot.it.id]>Date.now())).map(q=>q.slot.it);
    if(clips().length<2&&queue.length<4&&!paused){try{queue.push(...this.block());}catch(x){}}
    return clips().slice(0,2);},
  wait(sec){this.st.waits.push(sec);if(this.st.waits.length>12)this.st.waits.shift();},
  play(slot,f){const k=slot.kind,ok=sc=>{if(sc&&!this.rb)this.st.shown++;return sc;};
    if(k==="reel")return ok(S.reel(slot.it.id));
    if(ISCLIP[k]){const sc=YTM.sceneFor(slot.it.id);if(sc||this.rb)return ok(sc);
      if(this.bench[slot.it.id]>Date.now()&&!slot.sub&&!slot.tries&&TRON!==false){/* this clip is sitting out: swap in another of the same kind */const it=this.draw(k,this.pool(k).filter(x=>x.id!==slot.it.id));if(it){slot.it=it;slot.sub=true;slot.tries=0;}}
      if(TRON===false||this.bench[slot.it.id]>Date.now()||slot.tries>=2){this.st.skip++;return null;}
      slot.tries++;YTM.sync();
      /* this clip has not finished loading: bring the next non-clip screen forward (or fill with one art reel), then come back to it */
      const j=queue.findIndex(q=>q.slot&&!ISCLIP[q.slot.kind]);let alt=null;if(j>=0&&j<3)alt=queue.splice(j,1)[0];
      queue.unshift(f);if(alt){const a=alt();if(a)return a;}
      this.st.fill++;const r=this.draw("reel");return r?S.reel(r.id):null;}
    let sc=null;try{sc=slot.it.fn?slot.it.fn():null;}catch(x){}return ok(sc);},
  stats(){const s=this.st;return {sh:s.shown,fi:s.fill,sk:s.skip,stl:s.stall,nf:s.nf||0,w:s.waits.slice(-8),bad:s.bad,err:s.err,blk:this.n,q:queue.slice(0,8).map(q=>q.slot?q.slot.kind+":"+String(q.slot.it.id).slice(0,6):"?")};}};
CH.load();
'''
between('const FLOW={any:["reel","clip"]','function playlist(){',CH)
rep('function playlist(){DAY=DAYNOW();/* every mode runs the same stripped loop for now; the old per-mode line-ups below are unused */return flowToday().map(k=>()=>FLOWFN[k]());',
    'function playlist(){DAY=DAYNOW();/* every mode runs the channel blocks; the old per-mode line-ups below are unused */return CH.block();')
rep('if(sc&&sc.id!==lastId)return {sc,f,snap};','if(sc&&(sc.id!==lastId||sc.rep))return {sc,f,snap};')
rep('function rebuild(h){const cur=clone(IX);IX=clone(h.snap);let sc=null;try{sc=h.f();}catch(e){}IX=cur;return sc;}',
    'function rebuild(h){const cur=clone(IX);IX=clone(h.snap);let sc=null;CH.rb=true;try{sc=h.f();}catch(e){}CH.rb=false;IX=cur;return sc;}')

# ---------- two preloading YouTube players ----------
YT=r'''/* YouTube clips load hidden in the background, two at a time: the clip that plays next, and the one after it.
   A clip only comes on screen once it is buffered, so there is no loading screen and no dead wait between clips. */
function mkYT(n){return {n,state:"idle",t:null,player:null,bufT:0,onEnd:null,w:null,f:null,o:null,to:0,ee:0,iv:0,want:false,hold:0,
  box(){if(this.w)return;const st=document.getElementById("stage");if(!st)return;this.w=document.createElement("div");this.w.className="ytpre";this.w.innerHTML='<div class="f"></div><div class="ovl"></div>';
    let vc=document.getElementById("vcover");if(!vc){vc=document.createElement("div");vc.id="vcover";st.appendChild(vc);}st.insertBefore(this.w,vc);
    this.f=this.w.querySelector(".f");this.o=this.w.querySelector(".ovl");},
  load(t,want){if(this.state!=="idle")this.kill();this.box();if(!this.w)return;this.t=t;this.want=!!want;this.state="loading";const self=this,t0=Date.now();let pb=false,rdy=0,lastSt="none";
    this.f.innerHTML="";const b=document.createElement("div");this.f.appendChild(b);
    try{this.player=new YT.Player(b,{videoId:t.id,width:WEAKTV?854:1920,height:WEAKTV?480:1080,host:YTHOST,playerVars:{autoplay:1,mute:1,controls:0,rel:0,modestbranding:1,playsinline:1,iv_load_policy:3,disablekb:1,fs:0,cc_load_policy:0,start:(t.s||0)},events:{
      onReady:e=>{try{if(WEAKTV){const fr=e.target.getIframe();[["position","absolute"],["left","0"],["top","0"],["right","auto"],["bottom","auto"],["width","854px"],["height","480px"],["transform","scale(2.2484)"],["transform-origin","0 0"]].forEach(([k,v])=>fr.style.setProperty(k,v,"important"));}rdy=Date.now();e.target.mute();e.target.playVideo();}catch(x){}},
      onStateChange:e=>{const p=e.target;lastSt=e.data;
        if(self.state==="live"){if(e.data===3&&!self.bufT)self.bufT=Date.now();if(e.data===1)self.bufT=0;if(e.data===0&&self.onEnd)self.onEnd();return;}
        if(self.state==="loading"&&self.t===t&&e.data===1&&!pb){pb=true;const t1=Date.now();try{p.pauseVideo();}catch(x){}
          clearInterval(self.iv);self.iv=setInterval(()=>{if(self.state!=="loading"||self.t!==t){clearInterval(self.iv);return;}try{const d=p.getDuration()||150,ahead=(p.getVideoLoadedFraction()||0)*d-(t.s||0);
            if(ahead>=8||Date.now()-t1>12000){clearInterval(self.iv);try{p.seekTo(t.s||0,true);p.pauseVideo();}catch(x){}self.state="ready";clearTimeout(self.to);delete CH.st.bad[t.id];CH.wait(Math.round((Date.now()-t0)/1e3));
              if(self.want){self.want=false;pushScreen("trailer","yt:"+t.id);}}}catch(x){}},500);}},
      onError:e=>{if(self.t===t)self.fail("err"+(e&&e.data));}}});}catch(x){this.fail("throw");return;}
    /* a player that is ready but has not started gets a nudge every 4s; no start within 25s = give up on this try and load again */
    clearInterval(this.iv);this.iv=setInterval(()=>{if(self.state!=="loading"||self.t!==t||pb){if(!pb)clearInterval(self.iv);return;}if(rdy){try{self.player.mute();self.player.playVideo();}catch(x){}}},4000);
    clearTimeout(this.to);this.to=setTimeout(()=>{if(self.state==="loading"&&self.t===t&&!pb)self.fail("timeout "+(rdy?"st"+lastSt:"notready"));},25000);},
  /* a clip that fails twice in a row sits out for 10 minutes so it cannot hold the channel up */
  fail(why){const id=this.t&&this.t.id;if(id){CH.st.nf=(CH.st.nf||0)+1;CH.st.bad[id]=(CH.st.bad[id]||0)+1;CH.st.err=why+" "+id+" @"+new Date().toTimeString().slice(0,5);if(CH.st.bad[id]>=2){CH.bench[id]=Date.now()+10*60000;CH.st.bad[id]=0;}}this.kill();setTimeout(()=>{try{YTM.sync();}catch(x){}},500);},
  kill(){clearInterval(this.iv);clearInterval(this.ee);clearTimeout(this.to);try{this.player&&this.player.destroy();}catch(x){}this.player=null;if(this.f)this.f.innerHTML="";if(this.o)this.o.innerHTML="";if(this.w)this.w.classList.remove("on");this.state="idle";this.t=null;this.bufT=0;this.want=false;this.onEnd=null;this.hold=0;},
  scene(){const self=this,t=this.t;this.hold=Date.now()+6000;const el=$('<section class="scene trailer ytp"></section>');let d=0;try{d=this.player.getDuration()||0;}catch(x){}
    /* run for the clip's real length (never cut a trailer short); a clip with no end time is capped at 5 minutes */
    const len=Math.min(300,Math.max(0,(t.e||d||0)-(t.s||0)))||170;
    const sc={id:"trailer",rep:true,chrome:"cinema",dur:len+8,el,manual:true};let T2=[],done=false;
    const end=()=>{if(done)return;done=true;T2.forEach(x=>{clearTimeout(x);clearInterval(x);});sc.onEnd&&sc.onEnd();};
    el._start=()=>{if(self.state!=="ready"||self.t!==t){end();return;}self.onEnd=end;self.show();T2.push(setTimeout(end,(len+6)*1000));T2.push(setInterval(()=>{if(self.bufT&&Date.now()-self.bufT>8000){CH.st.stall++;CH.st.err="stall "+t.id;end();}},1000));};
    el._cleanup=()=>{T2.forEach(x=>{clearTimeout(x);clearInterval(x);});if(self.t===t)self.hide();};return sc;},
  show(){const t=this.t,p=this.player;this.state="live";this.bufT=0;this.hold=0;
    const dd=(()=>{if(!t.rel)return"";const a=new Date(t.rel+"T00:00:00"),n=now(),b=new Date(n.getFullYear(),n.getMonth(),n.getDate()),d=Math.round((a-b)/864e5);return d>0?`<span class="d"><b>${d}</b> ${d===1?"day to go":"days to go"}</span>`:`<span class="d">In theatres now</span>`;})()||(t.when?`<span class="d">${esc(t.when)}</span>`:"");
    this.o.innerHTML=`<div class="lt"><p>${esc(t.sub||"Official trailer")}</p><h2>${esc(t.t)}</h2>${dd}</div><div class="tie"></div>`;
    findBooks(t.kw||t.t,8).then(bs=>{bs=bs.filter(p=>p.price>=5).sort((a,b)=>b.price-a.price);if(!bs.length||this.state!=="live"||this.t!==t)return;const q=bs[0],u=qrURL(link(q,"trailer"));const tie=this.o.querySelector(".tie");if(tie)tie.innerHTML=`<img class="tc" src="${img(q.img,300)}" alt=""><div><span>In the shop now</span><b>${esc(splitT(q.title)[0])}</b><em>${money(q.price)}</em></div>${u?`<img class="tq" src="${u}" alt="">`:""}`;}).catch(()=>{});
    LASTTR=Date.now();CURPL=p;CURV=null;clearTimeout(YTM.rd);Radio.duck(true);this.w.classList.add("on");clearInterval(this.ee);this.ee=setInterval(()=>{try{const d=p.getDuration(),c=p.getCurrentTime();if(d>10&&c>((t.e||d)-1.6)&&this.onEnd)this.onEnd();}catch(x){}},500);try{p.seekTo(t.s||0,true);p.playVideo();}catch(x){}
    setTimeout(()=>{if(TVOL>0&&this.t===t){try{p.unMute();p.setVolume(TVOL);}catch(x){}}},350);setTimeout(()=>{try{YTM.sync();}catch(x){}},1200);},
  /* the radio only comes back if no other clip starts straight after this one */
  hide(){if(CURPL===this.player)CURPL=null;this.kill();clearTimeout(YTM.rd);YTM.rd=setTimeout(()=>{if(!YTS.some(y=>y.state==="live"))Radio.duck(false);},1500);setTimeout(()=>{try{YTM.sync();}catch(x){}},300);}};}
const YTS=[mkYT(0),mkYT(1)];
const YTM={rd:0,
  ok(){return !IS_REMOTE&&YTREADY&&typeof YT!=="undefined"&&!!YT.Player&&!window.DEADTAB;},
  find(id,st){return YTS.find(y=>y.t&&y.t.id===id&&(!st||y.state===st));},
  sync(){if(!this.ok())return;const want=TRON===false?[]:CH.plan();
    YTS.forEach(y=>{if((y.state==="loading"||y.state==="ready")&&!y.want&&!(y.hold>Date.now())&&!want.some(t=>t.id===y.t.id))y.kill();});
    want.forEach(t=>{if(this.find(t.id))return;const y=YTS.find(y=>y.state==="idle");if(y)y.load(t);});},
  sceneFor(id){const y=this.find(id,"ready");return y?y.scene():null;},
  /* someone asked for one clip from the remote: load it now and put it up the moment it is ready */
  demand(id){if(!this.ok())return;const t=[...((MARKET&&MARKET.trailers)||[]),...CLIPS].find(x=>x.id===id);if(!t)return;
    let y=this.find(id);if(y){if(y.state==="ready")pushScreen("trailer","yt:"+id);else if(y.state==="loading")y.want=true;return;}
    y=YTS.find(y=>y.state==="idle")||YTS.find(y=>y.state!=="live");if(!y)return;y.kill();y.load(t,true);},
  killAll(){YTS.forEach(y=>y.kill());}};
'''
between('/* YouTube trailers load hidden in the background while other screens play.','addEventListener("resize",fit);fit();',YT)
rep('window.onYouTubeIframeAPIReady=()=>{YTREADY=true;try{YTP.prep();}catch(x){}};','window.onYouTubeIframeAPIReady=()=>{YTREADY=true;try{YTM.sync();}catch(x){}};')

# ---------- S.trailer: remote "put this clip on" goes through the same players ----------
rep('''    if(i==="yt")return YTP.state==="ready"?YTP.scene():null;
    if(typeof i==="string"&&i.indexOf("yt:")===0){const id=i.slice(3);if(YTP.state==="ready"&&YTP.t&&YTP.t.id===id)return YTP.scene();YTP.kill();YTP.prep(id,true);return null;}
    if(TRON===false)return null;const MP=ALL.filter(x=>x.mp4);
    if(i!=null){const x=ALL[i%ALL.length];if(x&&!x.mp4){if(YTP.state==="ready"&&YTP.t&&YTP.t.id===x.id)return YTP.scene();YTP.kill();YTP.prep(x.id,true);return null;}}
    if(i==null&&Date.now()-LASTTR<TRGAP)return null;
    if(i==null&&YTP.state==="ready"&&(!MP.length||nx("trk",2)===0))return YTP.scene();
''','''    if(typeof i==="string"&&i.indexOf("yt")===0){const id=i.slice(3);if(!id)return null;const sc=YTM.sceneFor(id);if(sc)return sc;YTM.demand(id);return null;}
    if(TRON===false)return null;const MP=ALL.filter(x=>x.mp4);
    if(i!=null){const x=ALL[i%ALL.length];if(x&&!x.mp4){const sc=YTM.sceneFor(x.id);if(sc)return sc;YTM.demand(x.id);return null;}}
''')

# ---------- reports back over the relay ----------
rep('ytp:YTP.state,','ytp:YTS.map(y=>y.state.slice(0,2)+(y.t?":"+y.t.id.slice(0,6):"")).join(" "),ch:CH.stats(),app:(()=>{try{return window.CaptCanTVApp?CaptCanTVApp.info():"";}catch(x){return "";}})(),')
rep('Radio.el().pause();YTP.kill();}catch(x){}','Radio.el().pause();YTM.killAll();}catch(x){}')

# ---------- keep the players fed, tell the app the page is alive, recover after sleep ----------
rep('setInterval(()=>{try{YTP.prep();}catch(x){}},20000);',
 '''setInterval(()=>{try{YTM.sync();}catch(x){}},3000);
  /* inside the CaptCan TV app: sound and full screen need no button press, and the app reloads the page if these beats stop */
  if(window.CaptCanTVApp){GEST=true;setInterval(()=>{try{if(paused||Date.now()-startedAt<curMs+60000)CaptCanTVApp.beat();}catch(x){}},20000);}
  /* back from sleep: drop any half-loaded clip, bring the radio back and move straight to the next screen */
  let HIDAT=0;document.addEventListener("visibilitychange",()=>{if(document.hidden){HIDAT=Date.now();return;}if(HIDAT&&Date.now()-HIDAT>60000){try{YTM.killAll();Radio.ducked=false;Radio.play();go(1);}catch(x){}}HIDAT=0;});''')

# ---------- remote: the Lineup tab shows the channel ----------
LU=r'''function lineupHTML(){const TY={trl:"Trailer",c:"Cartoon opening",s:"Movie scene",k:"Talking clip"};
  const pools={},per={};Object.keys(KINDS).forEach(k=>pools[k]=CH.pool(k));BLOCKS.forEach(b=>b.forEach(k=>per[k]=(per[k]||0)+1/BLOCKS.length));
  const blockSec=Object.keys(per).reduce((a,k)=>a+(pools[k].length?per[k]*KSEC[k]:0),0),blockMin=Math.round(blockSec/60);
  const mins=m=>m<90?Math.round(m)+" min":(Math.round(m/6)/10)+" hours";
  const every=k=>{const n=pools[k].length;if(!n||!per[k])return "";if(k==="trl"){const rest=pools.trl.filter(x=>x.id!==LEADTR).length,gap=blockSec/60/per.trl;return pools.trl.some(x=>x.id===LEADTR)?"Avengers: Doomsday final trailer about every "+mins(gap*(rest?2:1))+(rest?", the others about every "+mins(gap*2*rest):""):"Each about every "+mins(gap*n);}
    return "Each one comes back about every "+mins(n/per[k]*blockSec/60);};
  const len=x=>x.e?Math.round(((x.e||0)-(x.s||0))/6)/10+" min":(x.ty?"plays in full":"full trailer");
  const chip=k=>`<span class="${pools[k].length?"":"off"}">${KINDS[k]}</span>`;
  const clipGrid=k=>`<div class="lugrid">${pools[k].map(x=>`<div class="luc" data-p="trailer:yt:${x.id}" role="button" tabindex="0"><img src="https://i.ytimg.com/vi/${x.id}/mqdefault.jpg" alt=""><b>${esc(x.t)}</b><span>${esc(x.sub||"")} · ${len(x)}</span></div>`).join("")}</div>`;
  const empty=Object.keys(SCREENS).filter(k=>!pools[k].length).map(k=>KINDS[k]);
  return `<style>.blk{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:8px 0 12px}.blk i{font-style:normal;font-weight:800;color:#b5b5be;font-size:13px;margin-right:4px}.blk span{background:#1b1b1f;border:1px solid #34343c;border-radius:999px;padding:7px 12px;font-size:13px;font-weight:700}.blk span.off{opacity:.38;border-style:dashed;font-weight:500}</style>
   <h3>How the channel runs</h3>
   <p class="lunote">The TV plays in blocks of about ${blockMin} minutes and the two blocks take turns. Each kind of screen has its own shuffled pile, so nothing repeats until everything else of its kind has played. The next two clips load in the background while the TV plays, so there is no waiting screen.</p>
   ${BLOCKS.map((b,j)=>`<div class="blk"><i>Block ${j+1}</i>${b.map(chip).join("")}</div>`).join("")}
   ${empty.length?`<p class="lunote">Faded slots (${empty.join(", ")}) are built into the channel and skipped until those screens are approved.</p>`:""}
   <h3>Art reels (${REELS.length})</h3><p class="lunote">Each one comes back about every ${mins(pools.reel.length/per.reel*blockSec/60)}. Tap one to put it on the TV now.</p>
   <div class="lugrid">${REELS.map(r=>`<div class="luc" data-p="reel:${r.k}" role="button" tabindex="0"><img src="v/${r.k}.jpg" alt=""><b>${r.n}</b><span>${Math.round(r.d)} sec</span></div>`).join("")}</div>
   ${["trl","c","s","k"].map(k=>`<h3>${TY[k]}s (${pools[k].length})</h3><p class="lunote">${every(k)}.</p>${clipGrid(k)}`).join("")}
   <h3>Not in the channel</h3><p class="lunote">Every other screen (Hot this week, staff picks, games, market, services and the rest) only shows when someone puts it up from the Screens tab.</p>`;}
'''
between('function lineupHTML(){const F=flowToday()','function remoteUI(){',LU)
rep('    return flowToday().map(k=>()=>FLOWFN[k]());}','    return CH.block();}')
rep('const ms=hold?hold*1000:sc.dur*1000*SPEED;','const ms=hold?hold*1000:sc.dur*1000*(sc.manual?1:SPEED);')
left=[m for m in re.findall(r'YTP\.\w+|flowToday|FLOWINFO|FLOWFN|#ytpre|"ytpre"',s)]
print('leftover refs:',set(left))
open(sys.argv[2],'w').write(s)
print('ok',len(src),'->',len(s))
