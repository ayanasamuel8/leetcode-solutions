class Solution:
    def convertToTime(self, hrBit, minBit):
        hr = str(int(hrBit, 2))
        minu = str(int(minBit, 2)) if len(str(int(minBit, 2))) > 1 else '0' + str(int(minBit, 2))
        return hr + ':' + minu
    def buildPossibleBits(self, numBit, maxLen, current):
        if len(current) > maxLen:
            return []
        if numBit <= 0:
            return [current + '0' * (maxLen - len(current))]
        ans = []
        ans.extend(self.buildPossibleBits(numBit - 1, maxLen, current + '1'))
        ans.extend(self.buildPossibleBits(numBit, maxLen, current + '0'))
        return ans
    
    def cleanTime(self, arr):
        ans = []
        for item in arr:
            minute = item[0]
            hr = item[1]
            newmin = []
            newhr = []
            for minu in minute:
                if int(minu, 2) <= 59:
                    newmin.append(minu)
            for h in hr:
                if int(h, 2) <= 11:
                    newhr.append(h)
            ans.append([newhr, newmin])
        return ans


    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(turnedOn + 1):
            ans.append([self.buildPossibleBits(i, 6, ''), self.buildPossibleBits(turnedOn - i, 4, '')])
        ans = self.cleanTime(ans)
        ret = []
        for item in ans:
            hr = item[0]
            minute = item[1]
            for h in hr:
                for minu in minute:
                    ret.append(self.convertToTime(h, minu))
        return ret