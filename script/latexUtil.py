import time
import random
import subprocess
import os
class LatexUtil:
    def __init__(self):
        pass
    # def setup(self):
    def setup(self):
        self.mapNumber={1:'./latex/top.tex',2:'./latex/mid.tex',3:'./latex/end.tex'} 
        self.mapString={}
        # self.fileString=[]
        fileString=[]
        for key in self.mapNumber.keys():
            filePath=self.mapNumber[key]
            try:
                fileHandler=open(self.mapNumber[key],'r')
                self.mapString[key]=fileHandler.read()
                fileHandler.close()
            except Exception as e:
                print(str(e))
                self.mapString[key]=''
        self.direcLatex='./latex/outtex/'
    def assemble(self,listNumber):
        outStr=''
        for i in listNumber:
            try:
                outStr+=self.mapString[i]
            except Exception as e:
                print(str(e))
        return outStr
    def writeToFile(self,strContent):
        curtime=str(int(round(time.time()*1000)))
        randInt=str(int(round(random.random()*10000)))
        namefile=self.direcLatex+curtime+'XX'+randInt+'.tex'

        try:
            fileHandler=open(namefile,'w')
            fileHandler.write(strContent)
            fileHandler.close()
            return namefile
        except Exception as e:
            print(str(e))
            return None
    def texToPdf(self,namefile):
        try:
            commandstr='pdflatex --output-directory=./latex/outpdf '+namefile
            print(commandstr)
            proc=os.system(commandstr)
	    return True
        except Exception as e:
            print(str(e))
            return False
   def process(listNumber):
        strContent=self.assemble(listNumber)
        name=self.writeToFile(strContent)
        res=texToPdf(name)

#setup()

if __name__=="__main__":
    c=LatexUtil()
    c.setup()
    strContent=c.assemble([1,2,3])
    #print(strContent)
    name=c.writeToFile(strContent)
    c.texToPdf(name)
