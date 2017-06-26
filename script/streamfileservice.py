import time
import random 
class StreamFileService:
    def __init__(self):
        self.direcLatex='./latex/outtex/'

    def assemble(self,listFile):
        outStr=''
        for file in listFile:
            try:
                fileHandler=open(file,'r')
                tempStr=fileHandler.read()
                outStr+=tempStr
                fileHandler.close()
            except Exception as e:
                print(str(e))
        return outStr

    def writeToFile(self,strContent):
        curtime=str(int(round(time.time()*1000)))
        randInt=str(int(round(random.random()*10000)))
        namefile=curtime+'XX'+randInt
        if strContent != '':
            try:
                filepath=self.direcLatex+namefile+'.tex'
                fileHandler=open(filepath,'w')
                fileHandler.write(strContent)
                fileHandler.close()
                return namefile
            except Exception as e:
                print(str(e))
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
    
