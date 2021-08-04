"""
Complete the factorial function in the editor below. Be sure to use recursion.

factorial has the following paramter:

int n: an integer
Returns

int: the factorial of n
Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial, you will get a score of .

Input Format

A single integer, n (the argument to pass to factorial).

Constraints
2 <= n <=12
Your submission must contain a recursive function named factorial.

Recursive Method for Calculating Factorial     


Sample Input

3
Sample Output

6
"""

n=int(input())
def factorial(a):
    if a==0:
        return 1
    return a * factorial(a-1)
print(factorial(n))
