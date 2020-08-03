/*
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

Input:
The first line of input contains an integer T denoting the number of test cases.  Each test case consists of a string of expression, in a separate line.

Output:
Print 'balanced' without quotes if the pair of parenthesis is balanced else print 'not balanced' in a separate line.

Constraints:
1 ≤ T ≤ 100
1 ≤ |s| ≤ 105

Example:
Input:
3
{([])}
()
([]

Output:
balanced
balanced
not balanced

** For More Input/Output Examples Use 'Expected Output' option **
*/







def func(s):
    stack = []
    d = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in d.values():
            stack.append(c)
        elif not stack or stack.pop() != d[c]:
            return False
    return True if not stack else False

for _ in range(int(input())):
    s = input()
    
    if func(s):
        print("balanced")
    else:
        print("not balanced")
