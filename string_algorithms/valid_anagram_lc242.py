class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """ 
        Problem description: Given two strings s and t, return true if t is an anagram of s, and false otherwise

        Note: Anagram is word or phrase that can be rearranged to different form
        Space and dash doesn't count. 
        
        Edge case questions: length of string s and t, containing other than english letter. uppercase lower case distinction. e.g. unicode? what to do for empty string? 
        
        Solution:
        1. Easiest case: if the length of two string not same, return false
        2. The solution
           - idea: count each letter, store in dictionary and compare == works in python
           - go over for loop each letter
        return s_letters == t_letters
        """
        if len(s) != len(t): # can't be anagram
            return False
        
        # s and t have the same length
        s_letters = dict()
        t_letters = dict()

        for char_count in range(len(s)):
            s_char = s[char_count]
            t_char = t[char_count]
            
            if s_char not in s_letters:
                s_letters[s_char] = 1

            if t_char not in t_letters:
                t_letters[t_char] = 1
            
            s_letters[s_char] +=1
            t_letters[t_char] +=1
        
        return s_letters == t_letters
