#import subprocess
#commandstr='pdflatex ./latex/top.tex'
#proc=subprocess.Popen(commandstr,shell=True)
if True:
# class LatexUtil:
    def __init__(self):
        pass
    # def setup(self):
    def setup():
        mapNumber={1:'./latex/top.tex',2:'./latex/mid.tex',3:'./latex/end.tex'} 
        mapString={}
        # self.fileString=[]
        fileString=[]
        for key in mapNumber.keys():
            filePath=mapNumber[key]
            try:
                fileHandler=open(mapNumber[key],'r')
                mapString[key]=fileHandler.read()
                fileHandler.close()
            except Exception as e:
                print(str(e))
                mapString[key]=''
        print(mapString[3])

    def assemble(listNumber):
        outStr=''
        for i in listNumber:
            try:
                outStr+=mapString[i]
            except Exception as e:
                print(str(e))
setup()

# if '__name__'=='__main__':
    # print('ok')
    # c=LatexUtil()
    # c.setup()
