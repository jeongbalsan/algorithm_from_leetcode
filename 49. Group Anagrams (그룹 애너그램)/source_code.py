import collections

class Solution:
    def groupAnagrams_self(self, strs: list[str]) -> list[list[str]]:

        a = {}

        for st in strs:

            sort_st = ''.join(sorted(list(st)))

            if sort_st not in a.keys():
                temp = []
                temp.append(st)
                a[sort_st] = temp

            else:
                st_values = a.get(sort_st)
                st_values.append(st)
                a[sort_st] = sorted(st_values)

        save = []

        for v in a.values():
            save.append(v)

        return save


    def groupAnagrams_1(self, strs: list[str]) -> list[list[str]]:
        
        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()




if __name__=='__main__':

    strs = ["eat","tea","tan","ate","nat","bat"]

    s = Solution()

    #print(s.groupAnagrams_self(strs))

    print(s.groupAnagrams_1(strs))