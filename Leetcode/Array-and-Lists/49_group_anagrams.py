
# solution 1: using hashmap
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        words = {}
        for s in strs:
            if tuple(sorted(s)) not in words:
                words[tuple(sorted(s))] = [s]
            else:
                words[tuple(sorted(s))].append(s)
                
        return words.values()


# solution 2: using defaultdict of python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words = collections.defaultdict(list)
        for s in strs:
            words[tuple(sorted(s))].append(s)
            
        return words.values()


"""
Complexity Analysis
Time Complexity: O(NKlogK), where N is the length of strs, and K is the maximum length of a string in strs. .
Space Complexity: O(NK), the total information content stored in the return array                
"""       

# solution 3: using counts
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        words  = collections.defaultdict(list)

        for s in words:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            words[tuple(count)].append(s)

        return words.values()

"""
Complexity Analysis
Time Complexity: O(NK + NA) --> O(NK), where N is the length of strs, and K is the maximum length of a string in strs. .
Space Complexity: O(NK + NA) --> O(NK), the total information content stored in the return array                
"""       
