class employer:
    def __init__(self,ref,nom,chiffr,vill,gender,niveau):
        self.ref=ref
        self.nom=nom
        self.__chiffr=chiffr
        self.vill=vill
        self.gender=gender
        self.niveau=niveau
    def getChiffr(self):
        return self.__chiffr
    def setChiffr(self,x):
        x=self.__chiffr
