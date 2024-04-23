# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6

# rows = 5
# for i in range(rows+2):
    # for j in range(i):
        # print(i,end=' ')
    # print(' ')


# 1  
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# rows=6
# for i in range(1,rows):
    # for j in range(1,i+1):
        # print(j,end=' ')
    # print(' ')
# 


# 1 1 1 1 1  
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# rows=6
# for i in range(1,rows):
    # for j in range(i,rows):
        # print(i,end=' ')
    # print(' ')



# 5 5 5 5  
# 5 5 5
# 5 5
# 5
# rows=5
# num=rows
# for i in range(rows,0,-1):
    # for j in range(0,i):
        # print(num,end=' ')
    # print(' ')


# 0 1 2 3 4 5 
# 0 1 2 3 4 
# 0 1 2 3 
# 0 1 2 
# 0 1
# rows=6
# for i in range(rows,0,-1):
    # for j in range(0,i+1):
        # print(j,end=' ')
    # print(' ')


m1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
m2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        # result[i][j]=m1[i][j]+m2[i][j] (add two elements)
        # result[i][j]=m1[i][j]*m2[i][j] (multiply two elements)

for r in result:
    print(r)