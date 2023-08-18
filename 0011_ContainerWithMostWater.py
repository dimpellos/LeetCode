class Solution:
    def maxArea(self, A: list[int]) -> int:
        left = 0
        right = len(A)-1
        m_area = 0
        while left < right:
            m_area = max(min(A[right], A[left]) * (right - left), m_area)
            if A[right] > A[left]:
                left += 1
            else:
                right -= 1
        return m_area
                