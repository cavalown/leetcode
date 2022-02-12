class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ''
        index = 0
        for index in range(len(sorted(strs)[0])):
            word_set = set(item[index] for item in strs)
            if len(word_set) != 1:
                break
            else:
                common_prefix += strs[0][index]
        return common_prefix
