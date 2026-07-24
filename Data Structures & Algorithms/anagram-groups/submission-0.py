class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqToWords = defaultdict(list)

        for word in strs:
          count = "".join(sorted(word))
          freqToWords[count].append(word)


        return freqToWords.values()
