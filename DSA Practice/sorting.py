class Solution:
    def selectionSort(self, nums,n):
        for i in range(0,n-2+1):
            min=i
            for j in range(i,n-1+1):
                if nums[j]<nums[min]:
                    min=j
            temp=nums[min]
            nums[min]=nums[i]
            nums[i]=temp
        return nums
sol=Solution()
arr=[7, 4, 1, 5, 3]
n=len(arr)
print(sol.selectionSort(arr,n))


class Solution:
    def bubbleSort(self, nums,n):
        for i in range(n-1,0,-1): #n-1 to 1(py 0 reverse)
            already=0 #already sorted
            for j in range(0,i+1-1): #0 to i(py i+1) we have to do -1 because of last element
                if nums[j]>nums[j+1]:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
                    already=1
            if already==0:
                break
        return nums
sol=Solution()
arr=[7, 4, 1, 5, 3]
n=len(arr)
print(sol.bubbleSort(arr,n))


class Solution:
    def insertionSort(self, nums,n):
        for i in range(0,n-1+1):# i from 0 to n-1 every element
            j=i
            #not last element because if it takes then j-1 index out of bound so take
            #second last element.
            while(j>0 and nums[j-1]>nums[j]): 
                temp=nums[j-1]
                nums[j-1]=nums[j]
                nums[j]=temp
                j=j-1
        return nums

sol=Solution()
arr=[7, 4, 1, 5, 3]
n=len(arr)
print(sol.insertionSort(arr,n))



class Solution:
    def mergeSort(self, arr,low,high):
        if low==high:
            return
        mid=(low+high)//2
        self.mergeSort(arr,low,mid)
        self.mergeSort(arr,mid+1,high)
        self.merge(arr,low,mid,high)
    def merge(self,arr,low,mid,high):
        temp=[]
        left=low
        right=mid+1
        while(left<=mid and right<=high):
            if(arr[left]<=arr[right]):
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while(left<=mid):
            temp.append(arr[left])
            left+=1
        while(right<=high):
            temp.append(arr[right])
            right+=1
        for i in range(low,high+1):  #i=low , i<=high , i++
            arr[i]=temp[i-low]
        
sol=Solution()
arr=[7, 4, 1, 5, 3]
n=len(arr)
sol.mergeSort(arr,0,n-1)
print(arr)

class Solution:
    def quickSort(self, arr, low, high):
        if low < high:
            partition = self.part(arr, low, high)  # Get partition index
            self.quickSort(arr, low, partition - 1)  # Sort left subarray
            self.quickSort(arr, partition + 1, high)  # Sort right subarray
        return arr

    def part(self, arr, low, high):
        pivot = arr[low]  # Choose first element as pivot
        i = low  # Start from element
        j = high

        while True:
            # Find element > pivot from the left
            while i <= j and arr[i] <= pivot:
                i += 1
            # Find element < pivot from the right
            while i <= j and arr[j] > pivot:
                j -= 1
            if i >= j:  # If pointers cross, break
                break
            # Swap elements at i and j
            arr[i], arr[j] = arr[j], arr[i]

        # Swap pivot (arr[low]) with arr[j] (correct position)
        arr[low], arr[j] = arr[j], arr[low]
        return j  # Return partition index

sol = Solution()
arr = [7, 4, 1, 5, 3]
n = len(arr)
print(sol.quickSort(arr, 0, n - 1))  # Output: [1, 3, 4, 5, 7]
