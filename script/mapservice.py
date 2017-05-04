from configmap import mapSoal,mapSolusi,mapCol2
class MapService:
    def __init__(self):
        self.template={};
        self.template[1]=mapSoal
        self.template[2]=mapSolusi
        self.template[3]=mapCol2
	self.afterSoal={};
	self.afterSoal[1]='./latex/source/soal/after.tex'
	self.afterSoal[3]='./latex/source/col2/after.tex'
    def getListFile(self,listNumber,templateId):
        #mapEntity=self.template[templateId]
        listOut=[]
        listOut.append(self.template[templateId]['head'])
        for i in range(0,len(listNumber)):
            if listNumber[i] in self.template[templateId]:
                listOut=self.appendFile(listOut,listNumber[i],templateId)
        listOut.append(self.template[templateId]['tail'])
        return listOut
    def appendFile(self,listIn,num,templateId):
        listOut=listIn
        if templateId==1 or templateId==3:
            listOut.append(self.template[templateId][num])
            listOut.append(self.afterSoal[templateId])
            return listOut
        elif templateId==2:
            listOut.append(self.template[1][num])
            listOut.append(self.template[templateId][num])
            return listOut
    def process(self,input):
        listNum=input['listNumber']
        templateId=input['templateId']
        return self.getListFile(listNum,templateId)
                

        
        
