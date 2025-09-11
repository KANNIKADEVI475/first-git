def invert_dict(d):
    inverted={}
    for key,value in d.items():
     if value in inverted:
        inverted[value].append(key)
     else:
        inverted[value]=[key]

    return inverted
d={"k":2,"a":2,"n":2,"i":2,"d":1,"e":1,"v":1}    
i_d=invert_dict(d)
print(i_d)