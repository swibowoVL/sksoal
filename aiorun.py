import json
from script.latexUtil import LatexUtil
from aiohttp import web
import asyncio
import time
import random
import traceback
import jinja2
import aiohttp_jinja2
#import util.logMe

async def rp(dictData):
    p,folderName,fileName=genFile(dictData)
    n=0
    limt=120 #2 minutues
    while True:
        n=n+1
        if p.poll() is not None:
            print('job is ready')
            break
        elif n>120:
            return 'Gagal generate tolong coba lagi'
        else:
            #print('wait and leave',n)
            await asyncio.sleep(1)
    return folderName,fileName
def genFile(dictInput):
    c=LatexUtil()
    folderName,fileName,procName=c.process(dictInput)
    return procName,folderName,fileName

async def handle(request):
    if random.randint(1, 100000) >=00000:
        folderN,fileN= await rp()
    else:
        text = "Hello, "
    return web.Response(text=folderN+fileN)

async def rootPage(request):
    context = {}
    response = aiohttp_jinja2.render_template("soal.html", request, context)
    return response

async def check(request):
    return web.Response(text='ok')


async def submit(request):
    try:
        #get content
        content=request.content

        #read content
        jsonR=await content.read()

        #decode the byte
        strJsonR=jsonR.decode("utf-8") 

        dictData=byteify(json.loads(strJsonR))

        #run latex process
        folderN,fileN= await rp(dictData)

        #get host and url redirect
        host=request.host
        urlRedirect="http://"+host+"/pdf/"+fileN
        return web.Response(text=urlRedirect)
    except Exception as e:
        traceback.print_exc()
        print(Exception)
        return "RESPON FAILED"

def byteify(input):
    return input
    if isinstance(input, dict):
        return {byteify(key): byteify(value) 
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
#logging.config.fileConfig('logging.ini')
#log=logging.getLogger(__name__)
#logger.info('jj')
app = web.Application()
aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader('./templates/'))
#app.router.add_static('/templates', './templates/', show_index=True)
app.router.add_static('/static', './static/', show_index=True)
app.router.add_static('/pdf', './latex/outpdf/', show_index=True)
app.router.add_post('/submit', submit)
app.router.add_get('/', rootPage)
app.router.add_get('/check',handle)
web.run_app(app,host='0.0.0.0',port=80)

