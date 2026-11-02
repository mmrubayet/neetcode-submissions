class Solution:

    def encode(self, strs: List[str]) -> str:
        new_strs = ''
        for i in strs:
            new_strs += f"{i}💀"
        return new_strs

    def decode(self, s: str) -> List[str]:
        new_list = s.split("💀")
        new_list.pop()
        return new_list