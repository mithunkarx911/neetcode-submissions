from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # stores indices
        res = []

        for r in range(len(nums)):
            # 1. Remove elements smaller than current from the back
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            q.append(r)

            # 2. Remove indices that fall outside the window [r - k + 1, r]
            if q[0] < r - k + 1:
                q.popleft()

            # 3. Add max value to result once we have a full window
            if r >= k - 1:
                res.append(nums[q[0]])

        return res

        