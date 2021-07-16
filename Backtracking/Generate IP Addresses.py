class Solution:
    def isValid(self, segment):
        if len(segment) == 0:
            return False

        if len(segment) > 1 and segment[0] == '0': # a segment can be "0" but cannot start with zero
            return False                           # i.e. "0" is a valid segment but "031" is an invalid segment

        segmentNum = int(segment)

        if segmentNum < 0 or segmentNum > 255:
            return False

        return True

    def generateIP(self, start, s,segcount,currentIP, res):
        if segcount == 0:
            x = "".join(currentIP)
            if x == s:
                IP = ".".join(currentIP)
                res.append(IP)
            return

        for end in range(start, start + 4):

            segmentString = s[start:end]  # since end index is not included in the list slicing so next call can be made with start = end

            if self.isValid(segmentString) is True:
                currentIP.append(segmentString)
                self.generateIP(end, s,segcount-1, currentIP, res) # since end was not included in the last segement because list slicing me end index nhi include hoti
                currentIP.pop()

    def genIp(self, s):
        res = []
        currentIP = []
        start = 0
        self.generateIP(0, s,4, currentIP, res)
        res = set(res)
        return sorted(res)


sObj = Solution()
s1 = "50361"
print(sObj.genIp(s1))
