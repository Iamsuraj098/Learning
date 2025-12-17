def hcf(x, y):
    if(x == 0): 
        return y
    else: 
        z = y%x
        y = x
        x = z
        return hcf(x, y)
    
def hcf_2_way(x, y):
    if(x == 0): 
        return y
    else: 
        return hcf(y, y%x)
    
print(hcf(3, 4))
print(hcf_2_way(3, 4))