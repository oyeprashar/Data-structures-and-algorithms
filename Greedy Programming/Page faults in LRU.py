class Solution:
    def pageFaults(self, N, C, pages):

        LRU = []
        faults = 0

        for page in pages:

            if page not in LRU:

                if len(LRU) == C:
                    LRU.pop(0)
                    LRU.append(page)
                else:
                    LRU.append(page)

                faults += 1

            else:
                LRU.remove(page)
                LRU.append(page)

        return faults
