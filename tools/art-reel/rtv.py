import asyncio,sys,json
from playwright.async_api import async_playwright
async def main(page,ts,out):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--allow-file-access-from-files'])
        pg=await b.new_page(viewport={'width':1920,'height':1080})
        pg.on('pageerror',lambda e: print('ERR',e))
        await pg.goto(page if page.startswith('http') else 'file://'+page); await pg.wait_for_function('window.READY===1'); await pg.wait_for_timeout(1500)
        for i,t in enumerate(ts):
            await pg.evaluate(f"render({t})")
            await pg.screenshot(path=out.format(i=i,t=t),type='jpeg',quality=93)
        await b.close()
asyncio.run(main(sys.argv[1],json.loads(sys.argv[2]),sys.argv[3]))
