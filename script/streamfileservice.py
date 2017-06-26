import time
import random 
import logging
log = logging.getLogger('main.'+__name__)

class StreamFileService:
    def __init__(self):
        self.direcLatex='./latex/outtex/'

    def assemble(self,listFile):
        outStr=''
        for file in listFile:
            try:
                log.info('preparing assemble file')
                fileHandler=open(file,'r')
                tempStr=fileHandler.read()
                outStr+=tempStr
                fileHandler.close()
                log.info('success read all file')
            except Exception as e:
                log.exception('exception')
        return outStr

    def writeToFile(self,strContent):
        curtime=str(int(round(time.time()*1000)))
        randInt=str(int(round(random.random()*10000)))
        namefile=curtime+'XX'+randInt
        if strContent != '':
            try:
                log.info('preparing assemble write to file')
                filepath=self.direcLatex+namefile+'.tex'
                fileHandler=open(filepath,'w')
                fileHandler.write(strContent)
                fileHandler.close()
                log.info('success writ to file')
                return namefile
            except Exception as e:
                log.exception('exception')
                return None
        else:
            return None

    def process(self,listNumber):
        outStr=self.assemble(listNumber)
        filename=self.writeToFile(outStr)
        return filename

if __name__=="__main__":
    sts=StreamFileService()
    sts.direcLatex='./'
    obj='../latex/source/itemsoal/head.tex'
    lst=[]
    for i in range(0,1000):
        lst.append(obj)
    #lst=['../latex/source/itemsoal/head.tex','../latex/source/itemsoal/11.tex']
    #outStr=str.assemble(lst)
    sttime=time.time()
    out=sts.process(lst)
    elptime=time.time()-sttime
    print(elptime)
    #time.sleep(3)
    #print(out)
    
