class Solution:     
    def NnumbersSum(self, N):
        if N<1:
            return 0
        return N+self.NnumbersSum(N-1)
sol=Solution()

print(sol.NnumbersSum(4))


class Solution:
    def reverse(self, arr, n):
        self.arr = arr  
        self.rev(0, n-1)  
        return self.arr  
    
    def rev(self, l, r):
        if l >= r:
            return
        self.arr[l], self.arr[r] = self.arr[r], self.arr[l]
        self.rev(l+1, r-1)

sol = Solution()
print(sol.reverse([1, 2, 3, 4, 5], 5)) 



class Solution:
    def fib(self, n):
        if n == 0:
            return 0  
        elif n == 1:
            return 1  
        return self.fib(n-1) + self.fib(n-2)

sol = Solution()
print(sol.fib(7)) 


class Solution:
    def fact(self, n):
        if n == 0:
            return 1  
        elif n == 1:
            return 1  
        return n*self.fact(n-1)

sol = Solution()
print(sol.fact(5)) 

class Solution:     
    def palindromeCheck(self, s):
        if len(s)==0:
            return s
        return s[-1] + self.palindromeCheck(s[0:-1])

sol = Solution()
pal="helo"
print(pal==sol.palindromeCheck(pal)) 

class Solution:    
    def palindromeCheck(self, s):
        if len(s)==0:
            return s
        return self.palindromeCheck(s[1:]) + s[0]

sol = Solution()
pal="aba"
print(pal==sol.palindromeCheck(pal))

class Solution:     
    def reverse(self, s,n):
        self.s = s  
        self.n=n 
        return self.palindromeCheck(s,n) 

    def palindromeCheck(self, s,n):
        if len(s)==0:
            return s
        return s[len(s)-n]+self.palindromeCheck(s[0:-1],n)

sol = Solution()
pal="abababa"
n=1
print(pal==sol.reverse(pal,n)) 


class Solution:
    def mostFrequentElement(self, arr):
        dict={}
        for num in arr:
            if num in dict:
                dict[num]+=1
            else:
                dict[num]=1
        print(dict)
        max1=0
        result=None
        for index,val in dict.items():
            if val>max1:
                max1=val
                result=index
        print(f"Maximum frequency is {max1} for number {result}")
sol = Solution()
arr = [1, 2, 2, 3, 3, 3]
sol.mostFrequentElement(arr)