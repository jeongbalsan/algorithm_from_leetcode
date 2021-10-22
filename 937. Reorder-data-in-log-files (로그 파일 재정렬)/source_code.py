from dataclasses import dataclass

@ dataclass
class Solution:

    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        
        letters, digits = [], []

        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        logs = letters + digits

        print(logs)


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

s = Solution()
s.reorderLogFiles(logs)

