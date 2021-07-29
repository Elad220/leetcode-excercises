class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(list)-1):
            if list[i] == list[i+1]:
                list[i].remove()

