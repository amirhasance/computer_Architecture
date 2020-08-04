
# *select is a seri of s0 , s1 , ... that they are binary 
# in this function we convert these series to an decimal number

def binary_to_decimal(*select):
    
    stroutput = ''
    
    for x in select:
        stroutput += str(x)
    
    return int(stroutput , 2)

    
        