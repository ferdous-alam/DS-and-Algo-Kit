
# Solution 2 is often asked in interviews, it is O(n) 
# solution 1: using heapq and counter of python
"""
Complexity Analysis
Time Complexity: O(NlogN), where N is the length of strs, and K is the maximum length of a string in strs. .
Space Complexity: O(N), the total information content stored in the return array                
"""       

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = collections.Counter(nums)
        res = heapq.nlargest(k, vals.keys(), key=vals.get) 
        return res

"""
Complexity Analysis
Time Complexity: O(Nlogk), where N is the length of strs, and K is the maximum length of a string in strs. .
Space Complexity: O(N + k), the total information content stored in the return array                
"""       



# solution 2: using bucket sort for ---> O(n) complexity
class Solution:
    # appraoch 2: bucket-sort
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first define a hasmap with counts
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # initialize an empty bucket of length of nums
        freq = [[] for k in range(len(nums) + 1)]
        
        # now iterate over count to populate freq
        for n, c in count.items(): 
            freq[c].append(n)   # frequency is the index of freq
            
        # we need to flatten freq from reverse
        res = []
        for i in range(len(freq)-1, 0, -1):
            res += freq[i]
            if len(res) == k:
                break
        return res
        
        