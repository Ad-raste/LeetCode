""" Leetcode: 1598. Crawler Log Folder
10/07/24"""

class Solution:
    def minOperations(self, logs: list[str]) -> int:
        time = 0
        for item in logs:
            if item == "../" and time > 0:
                time -= 1
            elif item != "../" and item != "./" :
                time += 1
        
        return time

sol = Solution()

print(sol.minOperations(["d1/","d2/","../","d21/","./"]))
print(sol.minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(sol.minOperations(["d1/","../","../","../"]))
print(sol.minOperations(["./","../","./"]))
