class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for strg in strs:
            code = ''.join(sorted(strg))
            dictionary.setdefault(code, []).append(strg)
        return list(dictionary.values())

        