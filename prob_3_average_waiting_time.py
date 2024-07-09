"""Leetcode : 1701. Average Waiting Time
09/07/24"""
class Solution:
    def averageWaitingTime(self, customers: list[list[int]]) -> float:
        number_of_customer = len(customers)
        time = 0
        wait_time = []
        total_time = 0

        for item in customers:
            if item[0] > time:
                time = item[0]
                

            time += item[1]

            total_time += time - item[0]
            #print(time - item[0])

            """wait_time.append(time - item[0])
        
        for item in wait_time():
            total_time += item"""
        
        avrage_wait = total_time / number_of_customer

        return avrage_wait
        
sol = Solution()
print(sol.averageWaitingTime([[1,2],[2,5],[4,3]]))
print(sol.averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
print(sol.averageWaitingTime([[50,2],[55,4],[100,3],[200,1]]))
print(sol.averageWaitingTime([[5,2],[5,4],[70,3],[200,1]]))
