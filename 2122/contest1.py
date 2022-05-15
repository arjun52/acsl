sec = 0
sikkalist = []
fibonacci = [1,1,2,3,5]
arjunlist = [] 
for x in range (0,5):
                == "R": if cstr[x]
         sec = sec + 3600*int(fibonacci[x])
    if cstr[x]
         sec = sec + 3900*int(fibonacci[x])
    if cstr[x] == "G":
         sec = sec + 300*int(fibonacci[x])
    if cstr[x] == "C":
         sec = sec + 305*int(fibonacci[x])
    if cstr[x]
         sec = sec + 5*int(fibonacci[x])
    if cstr[x]
         sec = sec + 3605*int(fibonacci[x])
                 == "Y":
                 == "B":
                 == "M":
arjunlist.append (str(sec//3600))
if int(arjunlist[0]) >= 12:
    arjunlist[0] = str(int(arjunlist[0])%12)
arjunlist.append (str((sec%3600)//60))
arjunlist.append (str((sec%3600)%60))
return(f"{int(arjunlist[0]):02d}" + ":" + f"{int(arjunlist[1]):02d}" + ":" + f"{int(arjunlist[2]):02d}")
                   
                                                                                        
