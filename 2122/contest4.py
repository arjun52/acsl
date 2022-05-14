def numFibonacciCycles(realPartLL, imagPartLL, realPartUR, imagPartUR, incr):
    
    fib = [1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377] #list of fib num to 500
    finalcounter = 0 #amount of numbers that cycle for fib number times
    pointset = []
    for x in range(0,round((realPartUR - realPartLL) / incr) +1):
      ko = imagPartLL
      for y in range(0,round((imagPartUR - imagPartLL) / incr) +1):
        pointset.append(complex(round(realPartLL,3), round(ko,3)))
        ko+=incr
      realPartLL+=incr
    for C in pointset:
          cyclelist = []
          v = C
          while abs(C) < 4 and cyclelist.count(C) < 2:
              Ctemp = C*C + v
              C = complex(round(Ctemp.real,3),round(Ctemp.imag,3))
              cyclelist.append(C)
          if cyclelist.count(C) > 1:
              repeat1 = cyclelist.index(C)
              repeat2 = len(cyclelist) 
              cyclelength = int(repeat2 - repeat1 - 1)
              if cyclelength in fib:
                  finalcounter += 1
    return int(finalcounter)
