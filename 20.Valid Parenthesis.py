class Solution:
    @staticmethod
    def isValid(s):
        lefty = '([{'
        righty = ')]}'
        stack=[]
        for c in s:
            if c in lefty:
                stack.append(c)
            elif c in righty:
                if not stack:
                    return False
                top=stack.pop()
                if lefty.index(top)!=righty.index(c):
                    return False
        return not stack
