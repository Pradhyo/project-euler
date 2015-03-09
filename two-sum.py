""" Given an array of integers, find two numbers such that they add up to a 
specific target number.

The function twoSum should return indices of the two numbers such that they 
add up to the target, where index1 must be less than index2. Please note that
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution:
    # return a tuple, (index1, index2) whos values add up to target

    def twoSum(self,num,target):
    	if target % 2 == 0 and num.count(target/2) > 1:
    		index1 = num.index(target/2)+1
    		num = num[index1:]
    		return index1, num.index(target/2)
    	num_hash = {}
    	for i in range(len(num)):
    		num_hash[num[i]] = i
    	for i in range(len(num)):
    		if target - num[i] in num_hash and target/2 != num[i]:
    			return i+1, num_hash[target-num[i]]+1
    	

input1 = Solution()
print input1.twoSum([3,2,4,0,0,1,1], target=2)




