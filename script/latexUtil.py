import time
import random
import subprocess
from .streamfileservice import StreamFileService
from .mapservice import MapService
from subprocess import Popen
import logging
log = logging.getLogger('main.'+__name__)
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
                log.info('preparing latex process')
                filepath=self.direcLatex+namefile+'.tex'
                #cmdlist=['latexmk', '-xelatex', '-silent', '-interaction=batchmode', '-pdf', '-jobname='+self.direcPdf+namefile,filepath]
                cmdlist=['latexmk', '-xelatex', '-silent', '-interaction=nonstopmode', '-pdf', '-jobname='+self.direcPdf+namefile,filepath]
                proc=Popen(cmdlist,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
                #proc=Popen(cmdlist,stdout=subprocess.DEVNULL)
                #proc=Popen(cmdlist)
                log.info('starting shell process')
                return True,proc
            except Exception as e:
                log.exception('gt exception')
                return False, None
    def process(self,listNumber):
        listFile=self.mp.process(listNumber)
        filename=self.sfs.process(listFile)
        result,proc=self.texToPdf(filename)
        #strContent=self.assemble(listNumber)
        #name=self.writeToFile(strContent)
        #res=self.texToPdf(name)
        if result:
            return self.direcPdf,filename+'.pdf',proc
        else:
            return '',''

if __name__=="__main__":
    #c=LatexUtil()
    #c.direcLatex='../latex/outtex/'
    #c.direcPdf='../latex/outpdf/'
    #c.setup()
    dictInput={}
    #dictInput['listNumber']=[3,1,2,5,6,7,8,9,10]
    #dictInput['listNumber']=[3,1,2,5,6,7,8,9,10,4]
    #dictInput['templateId']=2
    #print(c.mp.process(dictInput))
    #print(c.process(dictInput))
    #strContent=c.assemble([1,1,1])
    #print(strContent)
    #name=c.writeToFile(strContent)
    #c.texToPdf(name)
