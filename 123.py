l = [1, [3, 5, [6, 1]], 7, 29]
def suma(l,count=0):
    for element in l:
        if isinstance(element,int):
            print(element)
            count+= element
        else:
            count+= suma(element,count)
        print(count,"__")
    return count
print(suma(l))


    # suma = sum(l)
    # return suma
