class Solution:
    def fillCups(self, amount):
        count = 0
        while amount[0] > 0 or amount[1] > 0 or amount[2] > 0:
            amount.sort()
            amount.reverse()
            if amount[0] > 0:
                amount[0] -= 1
            if amount[1] > 0:
                amount[1] -= 1
            elif amount[0] < 1 and amount[1] < 1:
                amount[2] -= 1
            count += 1
        print(count)
amount = [5,4,4]
x= Solution()
x.fillCups(amount)
