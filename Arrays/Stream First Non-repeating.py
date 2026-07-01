"""
Process the input string like a stream of char and output first non repeating char till now. if multiple char are non repeating then output the first by index

Approach
  - Use queue to keep track of the order we saw the char
  - Use hashmap to keep track of the frequencies

  1. Add the current char in the freq hashmap and the queue
  2. Remove the repeating characters from the queue (pop the zeroth char)
  3. If queue is empty, add # to the res if not append the queue[0] to res
"""

class Solution:

    def firstNonRepeating(self, s):

        # use queue to manage the order
        # use hash map to count the frequency

        queue = []
        freq = {}
        res = ""

        for char in s:

            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

            queue.append(char)
          
            while len(queue) > 0 and freq[queue[0]] > 1:
                queue.pop(0)
              
            if len(queue) == 0:
                res += "#"
            else:
                res += queue[0]

        return res
