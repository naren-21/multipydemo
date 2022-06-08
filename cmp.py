def big_no(x,y,z):
    
    if x>y:
        return x
    elif y>z:
        return y
    else:
        return z
x,y,z = [16,7,8]
print("big no is", big_no(x,y,z))
