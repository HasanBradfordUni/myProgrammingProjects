#Bank for storing leetcode problem solutions
class Solutions:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                bad_idx = i

            if num == mink:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
        
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.at_most(nums, k) - self.at_most(nums, k-1)
    
    def at_most(self, nums, k):
        hm = {}
        l = 0
        cnt = 0
        for r in range(len(nums)):
            hm[nums[r]] = hm.get(nums[r], 0) + 1
            while len(hm) > k:
                hm[nums[l]] -= 1
                if hm[nums[l]] == 0:
                    hm.pop(nums[l])
                l += 1
            cnt += r - l + 1
        return cnt
        
    def isGood(self, nums: List[int]) -> bool:
        result = False
        numToCheck = max(nums)
        appMaxNums = nums.count(numToCheck)
        nums.sort()
        if len(nums) - 1 == numToCheck and appMaxNums == 2:
            if len(nums) > 2:
                for i in range(len(nums)-2):
                    if nums[i] == nums[i+1]:
                        result = False
                        break
                    result = True
            else:
                result = True
        else:
            result = False
        return result

    def isSymmetric(self, root):
        # Special case...
        if not root:
            return true;
        # Return the function recursively...
        return self.isSame(root.left, root.right)
        
    # A tree is called symmetric if the left subtree must be a mirror reflection of the right subtree...
    def isSame(self, leftroot, rightroot):
        # If both root nodes are null pointers, return true...
        if leftroot == None and rightroot == None:
            return True
        # If exactly one of them is a null node, return false...
        if leftroot == None or rightroot == None:
            return False
        # If root nodes haven't same value, return false...
        if leftroot.val != rightroot.val:
            return False
        # Return true if the values of root nodes are same and left as well as right subtrees are symmetric...
        return self.isSame(leftroot.left, rightroot.right) and self.isSame(leftroot.right, rightroot.left)
