class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numBoat = 0
        left, right = 0, len(people) - 1
        people.sort()

        while left <= right:
            if people[left] + people[right] <= limit:
                left, right = left + 1, right - 1

            else:
                right -= 1

            numBoat += 1

        return numBoat

