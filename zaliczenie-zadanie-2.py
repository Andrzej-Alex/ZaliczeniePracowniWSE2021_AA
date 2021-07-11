for i in range(1, 100):
    
    if (i % 3 == 0):
        print (i, "GOOD")
    elif (i % 5 == 0):
        print (i, "BETTER")
    elif (i % 5 == 0 and i % 3 == 0):
        print (i, "BEST")
    else:
        print (i)