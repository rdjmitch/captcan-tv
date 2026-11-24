const { chromium } = require('playwright');const http=require('http'),fs=require('fs'),path=require('path');
const srv=http.createServer((q,r)=>{const f=path.join('.',decodeURIComponent(q.url.split('?')[0]));if(!fs.existsSync(f)){r.writeHead(404);return r.end();}r.writeHead(200);fs.createReadStream(f).pipe(r);}).listen(8771);
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1920,height:1080}});p.on('pageerror',e=>console.log('ERR',e.message));
 await p.goto('http://localhost:8771/wall3.html?c='+process.argv[2]);await p.waitForFunction('window.READY===1');await p.waitForTimeout(500);
 const mode=process.argv[3];
 if(mode==='stills'){for(const t of JSON.parse(process.argv[4])){await p.evaluate(t=>render(t),t);await p.screenshot({path:`out/s_${String(t).replace('.','_')}.jpg`,type:'jpeg',quality:88});}}
 else{const fps=30,T=await p.evaluate(()=>TOTAL),n=Math.round(T*fps);for(let i=0;i<n;i++){await p.evaluate(t=>render(t),i/fps);await p.screenshot({path:`frames/f${String(i).padStart(4,'0')}.jpg`,type:'jpeg',quality:94});}console.log('frames',n);}
 await b.close();srv.close();})();
