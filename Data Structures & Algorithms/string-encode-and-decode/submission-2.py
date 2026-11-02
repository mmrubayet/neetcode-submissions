class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for string in strs:
            encoded.append(f"{len(string)}#{string}")
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0

        while i < len(s):
            j = s.index("#", i)
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            decoded.append(s[start:end])
            
            i = end

        return decoded