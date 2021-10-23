## 819. Most Common Word
## 819. 가장 흔한 단어

<br>

### 문제 : 

**Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.**
**The words in paragraph are case-insensitive and the answer should be returned in lowercase.**

**금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.**

--------------------------------------

**예제 1:**

**Input:** paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]

**Output:** "ball"

**Explanation:**

"hit" occurs 3 times, but it is a banned word.

"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 

Note that words in the paragraph are not case sensitive,

that punctuation is ignored (even if adjacent to words, such as "ball,"), 

and that "hit" isn't the answer even though it occurs more because it is banned.



**예제 2:**

**Input:** paragraph = "a.", banned = []

**Output:** "a"