#coding:utf-8
"""
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。 例如 a b c e s f c s a d e e 这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        assistMatrix = [True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if(self.hasPathAtAStartPoint(matrix,rows,cols, i, j, path, assistMatrix)):
                    return True
        return False

    def hasPathAtAStartPoint(self, matrix, rows, cols, i, j, path, assistMatrix):
        if not path:
            return True
        index = i*cols+j
        if i<0 or i>=rows or j<0 or j>=cols or matrix[index]!=path[0] or assistMatrix[index]==False:
            return False
        assistMatrix[index] = False
        if(self.hasPathAtAStartPoint(matrix,rows,cols,i+1,j,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i-1,j,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i,j-1,path[1:],assistMatrix) or
               self.hasPathAtAStartPoint(matrix,rows,cols,i,j+1,path[1:],assistMatrix)):
            return True
        assistMatrix[index] = True
        return False
