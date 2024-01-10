class Solution():
    def getRow(self, rowIndex):
        row = [1] * (rowIndex+1)
        for i in range(1, rowIndex):
            j = i
            while j > 0:
                row[j] =  row[j] + row[j-1]
                j -=1


        return row

obj = Solution()
obj.getRow(4)
