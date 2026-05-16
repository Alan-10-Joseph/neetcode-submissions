class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq=Counter(nums)
        sorted_freq=dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        ot=list(sorted_freq.keys())
        return ot[:k]