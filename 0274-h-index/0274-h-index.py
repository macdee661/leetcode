
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 
        h_index = 0
        print(citations)
        
        for i, citation in enumerate(citations):
            if citation >= i + 1:
                h_index = i + 1
            else:
                break 
                
        return h_index




