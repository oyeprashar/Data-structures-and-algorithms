"""
When a customer arrives first, we assign them a computer if available
When a customer departs, and we had assigned them a computer, we take it back

The most important is there can be a customer who came, but we did not assign them a computer and we should not
increment available computers when they leave



"""


class Solution:
    def solve(self, numOfComputers, customerString):

        seen = set()
        unservedCustomers = 0
        customersUsingComputer = set()
        availableComputers = numOfComputers

        for customer in customerString:

            seen.add(customer)

            if customer not in seen:
                if availableComputers > 0:
                    availableComputers -= 1
                    customersUsingComputer.add(customer)
                else:
                    unservedCustomers += 1

            else:
                if customer in customersUsingComputer:
                    customersUsingComputer.remove(customer) # because we dont want to increment when we find a customer jisse we didnt give a computer
                    availableComputers += 1

        return unservedCustomers


s = Solution()
print(s.solve(numOfComputers = 3, customerString = "GACCBDDBAGEE"))
