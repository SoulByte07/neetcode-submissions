class Solution:

    def encode(self, strs: List[str]) -> str:
        encoder_str=''
        for s in strs:
           # curr_str_len=len(s)
           # encoder_str+=str(curr_str_len)+'•'
           # encoder_str+=s 
           encoder_str+=s+'•'
        return encoder_str


    def decode(self, s: str) -> List[str]:
        decoder_str_array=list(map(str,s.split('•')))
        return decoder_str_array[:-1]


