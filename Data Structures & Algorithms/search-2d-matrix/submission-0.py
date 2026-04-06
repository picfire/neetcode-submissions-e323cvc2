class Solution:
    def search_binary(self, l: int, r: int, matrix: List[List[int]], target:int, n: int):
        if l > r:
            return False
        

        midpoint = l + (r - l) // 2

        row = midpoint // n
        col = midpoint % n

        midval = matrix[row][col]

        if midval == target:
            return True
        if midval < target:
            return self.search_binary(midpoint + 1, r,matrix, target,n)
        else:
            return self.search_binary(l, midpoint -1,matrix, target, n)
        


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        return self.search_binary(0, (m*n) - 1, matrix,target,n)