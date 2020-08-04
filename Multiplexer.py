from methods import binary_to_decimal

class Multiplexer():
    
    def __init__(self , size ):
        
        self.size = size 
        
        self.input_array = []
        
        def setInMUX(new_value):
            self.input_array.append(new_value)
            
        def MUX( self,*select):
            
            return self.input_array(binary_to_decimal(*select))   
        
        def clearMUX(self):
            self.input_array = []
        
        
        
        
    
        