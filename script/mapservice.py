#from configmap import mapSoal,mapSolusi,mapCol2
from .configmap import config
class MapService:

	def __init__(self):
		self.template={}
		self.afterSoal={}
		n=1
		for key in config:
		    self.template[key]=config[key]
		    self.afterSoal[key]=config[key]['after']
		    n+=1
       
	def getListFile(self,listNumber,templateId):
		listOut=[]
		listOut.append(self.template[templateId]['head'])
		for i in range(0,len(listNumber)):
			if listNumber[i] in self.template[templateId]:
				listOut=self.appendFile(listOut,listNumber[i],templateId)
		listOut.append(self.template[templateId]['tail'])
		return listOut

	def appendFile(self,listIn,num,templateId):
		if templateId==2:
		    listIn.append(self.template[1][num])
		    listIn.append(self.template[templateId][num])
		    return listIn
		else:
		    listIn.append(self.template[templateId][num])
		    listIn.append(self.afterSoal[templateId])
		    return listIn
	'''
        if templateId==1 or templateId==3:
            listOut.append(self.template[templateId][num])
            listOut.append(self.afterSoal[templateId])
            return listOut
        elif templateId==2:
            listOut.append(self.template[1][num])
            listOut.append(self.template[templateId][num])
            return listOut
	'''

	def process(self,input):
		listNum=input['listNumber']
		templateId=input['templateId']
		return self.getListFile(listNum,templateId)
                

        
 
