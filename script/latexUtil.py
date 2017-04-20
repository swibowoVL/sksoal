#import subprocess
#commandstr='pdflatex ./latex/top.tex'
#proc=subprocess.Popen(commandstr,shell=True)
class LatexUtil:
	def __init__(self):
		pass
	def setup(self):
		self.fileString=[]
		fileTop=open('./latex/top.tex','r')
		topString=fileTop.read()
		fileString.append(topString)
		fileTop.close()
		fileMid=open('./latex/mid.tex','r')
		topString=fileMid.read()
		fileString.append(topString)
		fileEnd=open('./latex/end.tex','r')
		topString=fileEnd.read()
		fileString.append(topString)
		print(fileString)

if '__name__'=='__main__':
	c=LatexUtil()
	c.setup()
	print('ok')

