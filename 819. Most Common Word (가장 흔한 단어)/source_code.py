import re
from collections import Counter

class Solution:
    def mostCommonWord_solved_self(self, paragraph: str, banned: list[str]) -> str:
        
        new_paragraph = re.sub(r"[^a-zA-Z0-9]", " ", paragraph)
        
        split_new_paragraph_lower = [np.lower() for np in new_paragraph.split()]
        
        counter_split_new_paragraph_lower = Counter(split_new_paragraph_lower)
       
        for banned_word in banned:
            del counter_split_new_paragraph_lower[banned_word]
    
        most_common_word = counter_split_new_paragraph_lower.most_common(1)[0][0]
        
        return most_common_word

    def mostCommonWord_1(self, paragraph: str, banned: list[str]) -> str:

        split_paragraph = [word for word in re.sub(r"[^\w]", " ", paragraph).lower().split() if word not in banned]
        
        return Counter(split_paragraph).most_common(1)[0][0]
            
            
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
s = Solution()
#print(s.mostCommonWord(paragraph, banned))

print(s.mostCommonWord_1(paragraph, banned))