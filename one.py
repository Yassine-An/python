# for i in range(2,0,-1):
#     for j in range(i,0,-1):
#         print(" ",end="")
#     for k in range(0,(5-i)*2):
#         print("*",end="")
#     print()
# for i in range(1,3):
#     for j in range(4-i,1,-1):
#         print("*",end="")
#     print()
#     for k in range(0,i):
#         print("*",end="")
#     print()
# /////////////////////////////
for i in range(6):
    for j in range(8):
        if(i==0 and j in [1,2,5,6]) or (i==1 and j in [0,3,4,7]) or (i==2 and j in [0,7]) or (i==3 and j in [1,6]) or (i==4 and j in [2,5]) or (i==5 and j in [3,4]):
            print("*",end="")
        else:
            print(" ",end="")
    print()
    