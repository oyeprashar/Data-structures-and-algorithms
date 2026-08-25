"""
Rotation : A string is a rotation of another if it can be formed by moving characters from the start to the end (or vice versa)
without rearranging them

All rotations of s1 = s1 + s1

So we just need to check if s2 is in s1 + s1
"""


class Solution:
    def areRotations(self, s1, s2):

        if len(s1) != len(s2):
            return False

        if s2 not in s1 + s1:
            return False

        return True
