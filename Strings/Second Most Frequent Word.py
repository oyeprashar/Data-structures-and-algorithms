
class Item:

    def __init__(self, word, freq):
        self.word = word
        self.freq = freq

    def __lt__(self, other):
        return self.freq >= other.freq


class Solution:
    def secFrequent(self, arr):

        if len(set(arr)) < 2:
            return -1

        freq = {}
        for word in arr:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1

        items = []
        for word in freq:
            items.append(Item(word, freq[word]))


        frequencies = set()
        for item in items:
            frequencies.add(item.freq)


        if len(frequencies) < 2:
            return -1

        frequencies = list(frequencies)
        frequencies = sorted(frequencies, reverse = True)

        return frequencies[1]
