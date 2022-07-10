class Solutions():
    def fillCups(self,amount):
        count = 0
        while amount[0]>0 or amount[1]>0 or amount[2]>0:
            amount.sort(reverse=True)
            if amount[0]>0:
                amount[0] -= 1
                if amount[1]>0:
                    amount[1] -= 1
                elif amount[2]>0:
                    amount[2] -= 1
            count += 1
        return count

amount = [5,0,0]
x = Solutions()
print(x.fillCups(amount))
