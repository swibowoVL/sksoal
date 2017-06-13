import time
import random
import subprocess
import os
from .streamfileservice import StreamFileService
from .mapservice import MapService
#from . import StreamFileService
#from . import MapService
class LatexUtil:
    def __init__(self):
        self.mp=MapService()
        self.sfs=StreamFileService()
        self.direcLatex='./latex/outtex/'
        self.direcPdf='./latex/outpdf/'
        pass
    def texToPdf(self,namefile):
        if namefile is not None:
            try:
                filepath=self.direcLatex+namefile+'.tex'
                #commandstr='pdflatex -interaction=nonstopmode --output-directory='+self.direcPdf+' '+filepath
                commandstr='latexmk -interaction=nonstopmode -pdf -jobname='+self.direcPdf+namefile+' '+filepath
                print(commandstr)
                proc=os.system(commandstr)
                return True
            except Exception as e:
                print(str(e))
                return False
    def process(self,listNumber):
        listFile=self.mp.process(listNumber)
        filename=self.sfs.process(listFile)
        res=self.texToPdf(filename)
        #strContent=self.assemble(listNumber)
        #name=self.writeToFile(strContent)
        #res=self.texToPdf(name)
        if res:
            return self.direcPdf,filename+'.pdf'
        else:
            return '',''

if __name__=="__main__":
    c=LatexUtil()
    #c.setup()
    dictInput={}
    #dictInput['listNumber']=[3,1,2,5,6,7,8,9,10]
    dictInput['listNumber']=[3,1,2,5,6,7,8,9,10,4]
    dictInput['templateId']=2
    #print(c.mp.process(dictInput))
    print(c.process(dictInput))
    #strContent=c.assemble([1,1,1])
>>>>>>> f41f50e017db8aa0d4dd665e3e5fe3e7ca4e1519
    #print(strContent)
    #name=c.writeToFile(strContent)
    #c.texToPdf(name)
