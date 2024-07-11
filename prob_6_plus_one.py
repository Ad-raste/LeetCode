"""Leetcode : 66. Plus One
10/07/24"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] == 9:
            digits.reverse()
            for item in range(len(digits)):
                if digits[item] == 9 :
                    digits[item] = 0
                elif digits[item] < 9:
                    digits[item] += 1
                    digits.reverse()
                    break
                if item == len(digits)-1:
                    digits.append(1)
                    digits.reverse()
                    break
        else:
            digits[-1] += 1
        
        return digits

if __name__ == "__main__":
    sol = Solution()
    print(sol.plusOne([1,2,3]))
    print(sol.plusOne([4,3,2,1]))
    print(sol.plusOne([9]))
    print(sol.plusOne([9,9,9,9]))
    print(sol.plusOne([0]))
    print(sol.plusOne([1,0,0,0,0,0,0]))