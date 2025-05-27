class Solution:
    def reverseNumber(self, n):
        rev=0
        while(n>0):
            ld=n%10
            rev=rev*10+ld
            n=n//10
        print(rev)
sol=Solution()
sol.reverseNumber(1236)

class Solution:
    def isPalindrome(self, n):
        num=n
        rev=0
        while(n!=0):
            ld=n%10
            rev=rev*10+ld
            n=n//10
        if num==rev:
            print("Palindrome")
        else:
            print("No it's not")
sol=Solution()
sol.isPalindrome(121)


class Solution:
    def GCD(self, n1, n2):
        while n2 != 0:
            rem = n1 % n2  # Calculate remainder first
            if rem == 0:
                return n2  # Better to return than print
            n1 = n2
            n2 = rem
        return n1  # Handle case when n2 was initially 0

sol = Solution()
print(sol.GCD(4, 6))  # Output: 2

class Solution:
    def countDigit(self, n):
        num=n
        count=0
        while n>0:
            count+=1
            n=n//10
        print("There are",count,"digits in",num)
sol = Solution()
sol.countDigit(13)

class Solution:
    def isArmstrong(self,n):
        count=0
        sum1=0
        nm=n
        num=n
        while nm>0:
            count+=1
            nm=nm//10
        while num!=0:
            digit=num%10
            sum1+=digit**count
            num=num//10
        if sum1==n:
            return True
sol=Solution()
print(sol.isArmstrong(153))

class Solution:
    def divisors(self, n):
        div=[]
        for i in range(1,n+1):
            if n%i==0:
                div.append(i)
        print(div)
sol=Solution()
sol.divisors(6)


class Solution:
    def isPrime(self, n):
        for i in range(2,n):
            if (n%i)==0:
                print("Not Prime")
                break
            else:
                print("Prime")
                break
sol=Solution()
sol.isPrime(8)