class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ''
        for i in strs:
            new_strs += f"{i}০"
        return new_strs

    def decode(self, s: str) -> List[str]:
        new_list = s.split("০")
        new_list.pop()
        return new_list