class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        d = {a,b}
        c = sum(d)
        print c

tmp = Solution()
print tmp.getSum(2,3)

