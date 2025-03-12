# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=list(s)
        i,j=0,len(st)-1
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        while(i<j):
            if st[i] in vowels:
                if st[j] in vowels:
                    c=st[i]
                    st[i]=st[j]
                    st[j]=c
                    i=i+1
                    j=j-1
                else:
                    j=j-1
            else:
                i=i+1
        return "".join(st)
        