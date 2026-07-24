class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        anagramsGroup = []
        for word in strs:
            key = "".join(sorted(word))
            anagramMap[key].append(word)

        for key, value in anagramMap.items():
            anagramsGroup.append(value)


        return anagramsGroup

    # space complexity O(n)
    # time complexity O(n * m) where n is the length of strs where as m is the length of strs[i]