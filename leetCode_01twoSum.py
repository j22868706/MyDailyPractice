class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


# The time complexity of this solution is O(n)
            
''' enumerate(iterable, start=0)
Return an enumerate object. iterable must be a sequence, an iterator, or some other object which supports iteration. 
The __next__() method of the iterator returned by enumerate() returns a tuple containing a count (from start which defaults to 0)
and the values obtained from iterating over iterable.

'''