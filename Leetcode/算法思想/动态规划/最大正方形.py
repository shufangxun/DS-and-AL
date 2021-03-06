class Solution1(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0]) # m为行数 n为列数
        dp = [[0] * n for _ in range(m)]
        size = 0 # 边长
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '0' or i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j]) - 0
                else:
                    dp[i][j] = int(min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])) + 1
                size = max(dp[i][j], size)
        return size * size

# 优化
class Solution2(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0]) # m为行数 n为列数
        dp = [0] * n
        size = 0 # 边长
        prev = 0
        for i in range(0, m):
            for j in range(0, n):
                tmp = dp[j]
                if matrix[i][j] == '0' or i == 0 or j == 0:
                    dp[j] = int(matrix[i][j]) - 0
                else:
                    dp[j] = int(min(dp[j], dp[j - 1], prev)) + 1
                size = max(dp[j], size)
                prev = tmp
        return size * size

