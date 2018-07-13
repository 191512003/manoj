
def smaller(lst):
     
    for i,n in enum(lst): 
         
        if n != '0': 
             
            tmp = lst.pop(i)
            break
     
   
    return str(tmp) + ''.join(lst) 
 
 

if __name__ == '__main__':
     
    lst = list(str(570107))
    lst.sort()
     
    print smaller(lst)
