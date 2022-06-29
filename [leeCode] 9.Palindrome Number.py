class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        alist = list(str(x))
        print(alist)
        answer = True
        for i in range(int(len(alist)/2)):
            #두개씩 짝지어서 같은 값인지 확인
            if alist[i] != alist[len(alist)-1-i]: 
                answer = False
        return answer