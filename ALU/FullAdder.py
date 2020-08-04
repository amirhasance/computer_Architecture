class FullAdder():
    def __init__(self , a , b  , cin) :
        self.a = a 
        self.b = b 
        self.cin = cin
    
    
    def Sum(self):
        sum = (self.a)^(self.b)^(self.cin)
        return sum 
    
    def Cout(self):
        cout = ((self.a)^(self.b))&(self.cin) | ((self.a) & self.b)
        return cout 
    