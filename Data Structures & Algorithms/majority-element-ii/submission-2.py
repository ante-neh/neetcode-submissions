class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        threshold, result = len(nums) / 3, []

        for num in nums:
            if num == candidate1:
                count1 += 1
            
            elif num == candidate2:
                count2 += 1

            elif count1 == 0:
                candidate1 = num
                count1 = 1

            elif count2 == 0:
                candidate2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        for candidate in [candidate1, candidate2]:
            if (candidate is not None) and nums.count(candidate) > threshold:
                result.append(candidate)

        return result


        # time complexity O(n)
        # space complexity O(1)

#The critical mathematical insight here is: There can be at most 2 majority elements that appear more than n/3 times in an array of size n.To see why: if there were 3 elements each appearing more than n/3 times, their combined count would be greater than 3 * (n/3) = n, which is impossible!

# Majority Element K 
# Threshold => > n / k
# Max Candidates => K - 1 candidates
# Counters Needed => K - 1 counters