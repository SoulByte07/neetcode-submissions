class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = set("([{")
        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in opening:
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if mapping[ch] != top:
                    return False

        return len(stack) == 0