from Multiplexer import Multiplexer
from FullAdder import FullAdder
class Arithmetic1():
    
    
    def __init__(self , a , b ):
        self.a = a 
        self.b = b 
        self.multiplexer = Multiplexer(4)
        self.sum = 0
        self.cout = 0
        self.cin = 0
        
        
        