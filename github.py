# def fib(n):
#     if n < 2:
#         return n
#     else:
#         return (fib(n-1) + fib(n-2))

# n = 10
# for i in range(1, n+1):
#     print(n,":" , fib(i) )

# def sum(n):
#     if n == 0:
#         return n
#     else:
#         return n+sum(n-1)

# print('The sum is:',sum(5))

# def grid_path(n,m):
#     if n == 1 or m == 1:
#         return 1
#     else:
#         return grid_path(n, m-1) + grid_path(n-1, m)
# print(grid_path(3, 3))
    


# use recursion to reverse a string

# def reverse(s1):
#     if s1 == '':
#         return s1
#     else:
#          return  s1[-1] + reverse(s1[:-1])
#         #   return  reverse(s1[1:]) +s1[0]
   
    
# def main():
#     s = 'hello'
#     word=reverse(s)
#     print(word)
# main()

# def ispalindrome(s):
#     # base case
#     if len(s) <= 0:
#         return True 
#     elif s[0] == s[-1]:
#         return ispalindrome(s[1:-1])
#     else:
#         return False

# def main():
#     print(ispalindrome('yuy'))
# main()


# def covert_to_binary(num):
#     result = ''
#     if num == 0:
#         return ''
#     else:
#         result = covert_to_binary((num // 2))+ str(num % 2)
#     return result
       
# def main():
#     print(covert_to_binary(8))
# main()
