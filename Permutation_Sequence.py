class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def getFirstElement(a, k1, result):
            len_a = len(a)
            if len_a == 1:
                result.append(str(a[0]))
                return
            avg_len = 1
            for i in range(1, len_a):
                avg_len *= i
            index = int(ceil(k1 / float(avg_len)) - 1)
            result.append(str(a[index]))
            a.remove(a[index])
            getFirstElement(a, k1-index*avg_len, result)
        
        a = [i+1 for i in range(n)]
        result = []
        getFirstElement(a, k, result)
        return ''.join(result)