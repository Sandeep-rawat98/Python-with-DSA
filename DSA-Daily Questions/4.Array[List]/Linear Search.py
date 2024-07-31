class Solution:
    ##Complete this function
    def searchInSorted(self, arr, N, K):
        for i in range(0, len(arr)):
            if arr[i] == K:
                return 1
        return -1


##TC - O(N), SC - O(1)
