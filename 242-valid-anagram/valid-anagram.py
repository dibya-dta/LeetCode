class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for item1 in s:
            if s.count(item1) == t.count(item1):
                pass
            else:
                print('step2')
                return False
        print('final')
        return True
        # seen={}

        # s_dict = dict(enumerate(s))
        # for item in t:
        #     if item in s_dict:
        # print(s_dict)
