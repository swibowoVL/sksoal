class MapService:
    def __init__(self):
        self.template={};
        mapSoal={1:'./latex/source/soal/1.tex',2:'./latex/source/soal/2.tex',3:'./latex/source/soal/3.tex','head':'./latex/source/soal/uashead.tex','tail':'./latex/source/soal/uastail.tex'} 
        mapSolusi={1:'./latex/source/solusi/1sol.tex',2:'./latex/source/solusi/2sol.tex',3:'./latex/source/solusi/3sol.tex','head':'./latex/source/solusi/kuncihead.tex','tail':'./latex/source/solusi/kuncitail.tex'}
        self.template[1]=mapSoal
        self.template[2]=mapSolusi
        self.afterSoal='./latex/source/soal/after.tex'
    def getListFile(self,listNumber,templateId):
        #mapEntity=self.template[templateId]
        listOut=[]
        listOut.append(self.template[templateId]['head'])
        for i in range(0,len(listNumber)):
            if listNumber[i] in self.template[templateId]:
                listOut=self.appendFile(listOut,listNumber[i],templateId)
                #listOut.append(self.template[templateId][listNumber[i]])
        #elif templatId==2:
            #for i 
        listOut.append(self.template[templateId]['tail'])
        return listOut

    def appendFile(self,listIn,num,templateId):
        listOut=listIn
        if templateId==1:
            listOut.append(self.template[templateId][num])
            listOut.append(self.afterSoal)
            return listOut
        elif templateId==2:
            listOut.append(self.template[1][num])
            listOut.append(self.template[templateId][num])
            return listOut
        
    def process(self,input):
        listNum=input['listNumber']
        templateId=input['templateId']
        return self.getListFile(listNum,templateId)
                

        
        