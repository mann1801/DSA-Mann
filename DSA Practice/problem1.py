import numpy as np
class Solution:
    def whichWeekDay(self, day):
        match day:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case 8:
                print("Invalid")
            case _:
                print("Enter proper input")

day=int(input("enter day : "))
arr=np.array([1,2,3,4,5])
print(arr[0])
for i in np.arange(1,11):
    print(i)
i=0
while i<=10:
    if (i==10):
        print("Done")
        break
    i+=1
solution = Solution()  # Create an instance of Solution
solution.whichWeekDay(day)
