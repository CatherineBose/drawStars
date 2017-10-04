x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(arr):
    for i in arr:
        # arrpos1=[]
        # for j in (1, i+1):
        #     arrpos1.append(*)
        isIntNo = isinstance( i, int )
        isIntString = isinstance(i, str)
        if (isIntNo):
            print "*" * i
        elif(isIntString):
            # print "i[0].lower() ::" ,i[0].lower() 
            print i[0].lower() * len(i)
draw_stars(y)
