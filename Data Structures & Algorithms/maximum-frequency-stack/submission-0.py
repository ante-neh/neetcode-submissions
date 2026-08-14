class FreqStack:

    def __init__(self):
        self.valFreqMap = defaultdict(int)
        self.freqValMap = defaultdict(list)
        self.maxFreq =  0

    def push(self, val: int) -> None:
        self.valFreqMap[val] += 1
        freqKey = self.valFreqMap[val]
        self.freqValMap[freqKey].append(val)
        self.maxFreq = max(self.maxFreq, self.valFreqMap[val])


    def pop(self) -> int:
        top = self.freqValMap[self.maxFreq].pop()
        self.valFreqMap[top] -= 1
        
        if not self.freqValMap[self.maxFreq]:
            self.maxFreq -= 1

        return top


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()