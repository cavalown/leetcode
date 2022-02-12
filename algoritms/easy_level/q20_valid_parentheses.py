class Solution:
    def isValid(self, s: str) -> bool:
        """Sample Answer:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
        """
        symble_stack = []
        symble_dict = {"[": "]", "(": ")", "{": "}"}
        s = s.replace(' ', '')
        count_dict = dict()
        for symble in s:
            count_dict[symble] = count_dict.get(symble, 0)+1
        for item in ["{", "[", "("]:
            if count_dict.get(item):
                if count_dict.get(symble_dict[item]) and count_dict[item] == count_dict[symble_dict[item]]:
                    continue
                else:
                    return False
        for item in s:
            if item in ["{", "[", "("]:
                symble_stack.append(symble_dict[item])
            else:
                if symble_stack and item == symble_stack[-1]:
                    symble_stack.pop()
                else:
                    return False
        return True
