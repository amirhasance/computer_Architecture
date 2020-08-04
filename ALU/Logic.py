from Multiplexer import Multiplexer

class Logic():
    
    
    def __init__(self , a , b  , multiplexer):
        
        self.a = a 
        self.b = b
        self.multiplexer = Multiplexer(4)
        self.output = None
    
    def AND(self):
        return self.a & self.b
    
    
    def XOR(self):
        return self.a ^ self.b

    
    def OR(self):
        return self.a | self.b
    
    def complement(self):
        
        if a :
            return 0
        return 1
    
    def LogicMUX( self,*select):
        self.multiplexer.clearMUX()
        self.multiplexer.setInMUX(self.AND)
        self.multiplexer.setInMUX(self.OR)
        self.multiplexer.setInMUX(self.XOR)
        self.multiplexer.setInMUX(self.complement)
        self.output = self.multiplexer(*select)
        
    
        
