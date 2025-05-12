class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        Problem Description: Given an array nums of size n, return the majority element. The majority 
        element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
        element always exists in the array.

        Clarification:
        You can't have more than 1 majority element since the majority element happens more than
        half of the time
        
        Edge case: size of nums, empty array, whether the majority element always exists.
        contain other than number, range of the number in the list... etc

        Solution: in this case, you only have to track the element that appears the most time.
        Easiest -> for loop, go over each element, count how many times the element appear using
        dictionary and output the most occuring  as soon as the number repeat more than length//2
        return. 

        Time complemxity O(N). 
        Optimizing Space:  Could you solve the problem in linear time and in O(1) space?

        """
        major_count = len(nums)//2+1 # majority element mut have count more than this.
        element_counts = dict()

        for iteration in range(len(nums)):
            element = nums[iteration]
            if element not in element_counts:
                element_counts[element] = 0
            element_counts[element]+= 1
            if element_counts[element] == major_count:
                return element
        
        # O(1) space algorithm by niits. Moore Voting Algorithm 
        # https://www.geeksforgeeks.org/boyer-moore-majority-voting-algorithm/
        # res = majority = 0

        # for n in nums:
        #     if majority == 0: # change the majority number b/c 
        #         res = n
        #     majority +=1 if n ==res else -1
        # return res
        # cancel majority element with nonmajority element -> there still has to be 
        # one more majority element 

        