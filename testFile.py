class Mobile :
    def __init__(self,brand,case):
        self.brand=brand
        self.case=case
    def display(self):
        print( self.case._Case__color)
class Case:
    def __init__(self,color) -> None:
        self.__color=color            
c1= Case('Black')    
c2= Case('White')
m1=Mobile('Honey',c1)
c1.__color='Green'
m1.display()     