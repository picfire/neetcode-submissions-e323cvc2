from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def merge_sort_consecutive(arr):
            if len(arr) <= 1:
                return arr, 1 if arr else 0

            mid = len(arr) // 2
            left_sorted, left_longest = merge_sort_consecutive(arr[:mid])
            right_sorted, right_longest = merge_sort_consecutive(arr[mid:])

            merged = []
            i = j = 0
            while i < len(left_sorted) and j < len(right_sorted):
                if left_sorted[i] < right_sorted[j]:
                    merged.append(left_sorted[i])
                    i += 1
                else:
                    merged.append(right_sorted[j])
                    j += 1
            merged.extend(left_sorted[i:])
            merged.extend(right_sorted[j:])

            longest = max(left_longest, right_longest)
            current = 1

            for k in range(1, len(merged)):
                if merged[k] == merged[k - 1]:
                    continue  
                elif merged[k] == merged[k - 1] + 1:
                    current += 1
                    longest = max(longest, current)
                else:
                    current = 1

            return merged, longest

        if not nums:
            return 0

        _, longest = merge_sort_consecutive(nums)
        return longest
