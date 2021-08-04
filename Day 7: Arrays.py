"""
Objective
In this challenge, we use a Regular Expression to evaluate a string.

Task
Complete the function in the editor below by returning a RegExp object, re, 
that matches any string s that begins and ends with the same vowel. 
Recall that the English vowels are a, e, i, o, and u.

Constraints
The length of string s is =>3 .
String s consists of lowercase letters only (i.e., [a-z]).
Output Format
The function must return a RegExp object that matches any string s beginning with and ending in the same vowel.
"""

n = int(input())
arr = list(map(int,input().split(" ")))
reversed_arr = arr[::-1]
for i in reversed_arr:
    print(i,end=' ')
