from ast import List
matrix = [[-1]]
rowsize = len(matrix)
sumx=[[0]*rowsize for _ in range(rowsize)]
print(sumx)
for row in range(rowsize):
    for col in range(rowsize):
        print(row,col,matrix[row][col])
        sumx[row][col] = matrix[row][col]
        if(row>0):
            sumx[row][col] += sumx[row-1][col]
        if(col>0):
            sumx[row][col] += sumx[row][col-1]
        if(row >0 and col >0):
            sumx[row][col] -= sumx[row-1][col-1]
    print(sumx)
    #break        
#print(sumx)         