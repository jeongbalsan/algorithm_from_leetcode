class Solution:

    def longestPalindrome(self, s: str) -> str:

        def work(s: str) -> str:

            if len(s) <= 1 or s == s[::-1]:
                return s

            if len(s) % 2 == 1:

                middle_value = int(len(s)/2)

                max_palindromic = s[middle_value]

                start_value = middle_value - 1

                end_value = -(middle_value)

                while start_value >= 0:

                    try:

                        if s[start_value:middle_value+1] == "".join(list(reversed(s[middle_value:end_value+1]))):

                            max_palindromic = s[start_value:end_value+1]

                            start_value -= 1

                            end_value += 1
                        
                        else:

                            return max_palindromic

                    except:

                        return max_palindromic

            else:

                start_value = int(len(s)/2) - 1

                end_value = int(len(s)/2)

                max_palindromic = s[start_value]

                if s[start_value] != s[end_value]:
                    
                    return max_palindromic

                max_palindromic = s[start_value:end_value+1]

                while start_value >= 0:
                    
                    try:
                        if s[start_value-1:start_value+1] == s[end_value:end_value+2]:
                            
                            max_palindromic = s[start_value-1:end_value+2]

                            start_value -= 1

                            end_value += 1

                        else:

                            return max_palindromic

                    except:

                        return max_palindromic


        if len(s) <= 1 or s == s[::-1]:
            return s

        result = []
        ngrams = []

        for i in range(len(s), 1, -1):

            ngrams = list(zip(*[s[j:] for j in range(i)]))

            for ngram in ngrams:
                gram = "".join(ngram)
                result.append(work(gram))

        return max(result, key=len)

    def longestPalindrome_1(self, s: str) -> str:

        def expand(left: int, right: int) -> str:

            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1

            return s[left+1:right-1]

        if len(s) < 2 or s == s[::-1]:
            return s

        result = ''
        for i in range(len(s) - 1):
            result = max(result, 
                            expand(i, i+1), 
                            expand(i, i+2), 
                            key=len)

        return result


    def longestPalindrome_2(self, s: str) -> str:

        def get_palindrome(s: str, l: int, r: int) -> str:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        p = ""

        for i in range(len(s)):
            p1 = get_palindrome(s, i, i+1)
            p2 = get_palindrome(s, i, i)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p    




if __name__=='__main__':
    
    s = "ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"

    s_c = Solution()

    #print(s_c.longestPalindrome(s))

    #print(s_c.longestPalindrome_1(s))

    print(s_c.longestPalindrome_2(s))