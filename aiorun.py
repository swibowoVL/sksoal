from pathlib import Path
import json
from script.latexUtil import LatexUtil
from aiohttp import web
import asyncio
import time
import random
import traceback
import jinja2
import aiohttp_jinja2
import logging

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
    log.info('request from %s' %(request.host))
    context = {}
    response = aiohttp_jinja2.render_template("soal.html", request, context)
    return response

async def check(request):
    log.info('request from %s' %(request.host))
    return web.Response(text='ok')


async def submit(request):
    try:
        log.info('request from %s' %(request.host))
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
        filePath=Path('./latex/outpdf/'+fileN)
        if filePath.is_file():
            return web.Response(text=urlRedirect)
        else:
            return web.Response(text="http://"+host+'/page/404.html')
    except Exception as e:
        log.exception('exception')
        return web.Response(text="RESPON FAILED")

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
#--------------
log = logging.getLogger('main')
log.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('server.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s -%(funcName)10s()- %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
log.addHandler(handler)

#--------------
app = web.Application()
aiohttp_jinja2.setup(app,loader=jinja2.FileSystemLoader('./templates/'))
app.router.add_static('/page', './page/', show_index=True)
app.router.add_static('/static', './static/', show_index=True)
app.router.add_static('/pdf', './latex/outpdf/', show_index=True)
app.router.add_post('/submit', submit)
app.router.add_get('/', rootPage)
app.router.add_get('/check',handle)
web.run_app(app,host='0.0.0.0',port=80)

