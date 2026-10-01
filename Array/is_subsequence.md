<!-- Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false -->


This problem was very easy , i think it tested your coding fundamentals of the key words break and continue
so we are going to loop through the character of t, if that character is in s then we append it to character_order(this is a variable to track how records appear), then you just compare s and the character order and return that after the loop



