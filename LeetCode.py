
#CeilValue of target-----------------------------------------------------------------

# Leet: 744
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/

# first applied the binary search method
# then removed one condition that was "mid equals to target" 
# and for the last element if its same as the target we have to find then i returned the first element of array as the letters wrap around 





#Solution

# def nextGreatestLetter(letters,target):
#     start=0
#     end=len(letters)-1

#     while start<=end:
#         mid=start+(end-start)//2
#         if target<letters[mid]:
#             end=mid-1
#         else:
#             start=mid+1
#     return letters[start%len(letters)]

#Did this with same method as to find the ceilOf number in given array...instead of  












#LEET 34
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# first approach is same i.e with binary search we found the the occurence of the target element
# after that we have to traverse and get the left most and right most element in that array
# i did this in 2 parts :
# Part 1: finding the left most occurence of the same element
# Part2 : finding the right most occurence of the same element

# to find left occurence
# instead of returning the mid element with binary search...i searched for the element again in the left side with BS
# to find right occurence i did the same 



#Solution
# def searchRange(self, nums, target):
#     def firstoccurence(nums,target,findStartIndex:True):
#         ans=-1
#         start=0
#         end=len(nums)-1
#         while start<=end:
#             mid=start+(end-start)//2
#             if target>nums[mid]:
#                 start=mid+1
#             elif target<nums[mid]:
#                 end=mid-1
#             else:
#                 ans=mid
#                 if findStartIndex:
#                     end=mid-1
#                 else:
#                     start=mid+1
#         return ans
#     ans=[-1,-1]
#     ans[0]=firstoccurence(nums,target,True)
#     ans[1]=firstoccurence(nums,target,False)

    # return ans




















# LEET 852: Peak Index in the Mountain Array
# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/


# Solution

# do a binarySearch as usual but the conditions will differ
# we dont have target in this
# we would check if the middle element is greater than mid+1 element

# if mid > mid+1 : that means we are in descending array i.e right side of the mountain or at the top
# now we will check if the right side have bigger element of not

# condition 2: if mid < mid+1: that means we are in the ascending part of mountain or at peak

# now wehn the loop breaks the start and end will be equal 


# code:=>

# class Solution:
#     def peakIndexInMountainArray(self, arr):
#         start= 0
#         end= len(arr)-1

#         while end!=start:
#             mid=start+(end-start)//2
#             if arr[mid]>arr[mid+1]:
#                 end = mid
#             else:
#                 start = mid +1
#         return start
# new=Solution()
    
# arr=[1,2,3,4,3,2,1]
# print(new.peakIndexInMountainArray(arr))









