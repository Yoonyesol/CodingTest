class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = int("".join(map(str, digits))) + 1
        return list(str(a))