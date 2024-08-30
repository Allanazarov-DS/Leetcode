import os 
os.system("cls")

# 14. Longest Common Prefix
# def funk(v):
#     ans = ''
#     v = sorted(v)
#     first = v[0]
#     last = v[-1]
#     print(first, last)
#     for i in range(min(len(first), len(last))):
#         if first[i] != last[i]:
#             return ans
#         ans+=first[i]
#     return ans
# v = ["flower", "flow", "flight", 'flogan']
# print(funk(v))


# def last_element(s: str) -> int:
#     ls = []
#     res = ''
#     for i in s:
#         if i != " ":
#             res+=i
#         else:
#             if res != '':
#                 ls.append(res)
#                 res = ''
    
#     ls.append(res)
#     last = len(ls[-1])
#     print(ls)
#     return last

# s = "fly me   to   the moonaa Oloniya sad" 
# print(last_element(s))

# N3
# son = int(input())
# if son % 2 == 0 and son != 0:
#     print('Juft')
# elif son == 0:
#     print('son 0 ga teng')
# else:
#     print('toq')

# N4
# n1, n2 = map(int, input("ikta son kiriting:").split())
# print((n1 + n2) / 2)


# N5
# belgi = input('Belgi:')
# son = int(input("Son = "))

# print(belgi * son)

# N6
# strs = input()
# print(len(strs))

# N7
# str1, str2 = map(str, input("ikta belgi:").split())
# print(str1, str2)
# print(type(len(str1) / len(str2)))

# N8  ceil funksiyasi
# import math
# n1, n2 = map(int, input("ikta son:").split())
# print(math.ceil(n1 / n2))

# N10 floor function
# import math
# n1, n2 = map(int, input("ikta son:").split())
# print(math.floor(n1 / n2))

# N11
# n = input("r:")
# print(f"int tipida - {int(n)}\nfloat tipida - {float(n)}\nboolean tipida - {bool(n)}")

# N13 isapha()
# s = input("symbol:")
# if s.isalpha():
#     print("harf")
# else:
#     print('harf emas')

# N14
# son = input("son:")
# son = [int(x) for x in son]
# print(sum(son))


# N15
# son = 75
# son = str(son)
# son = son[::-1]
# print(son)

# N16
# num = input("7 xonali son:")
# num = num[::-1]
# print(num)

# N17
# n = int(input("son:"))
# for x in range(n):
#     if x % 2 == 0:
#         print(x, end = ' ')

# N18
# name = input("Ismingizni kiriting:")
# age = int(input("Yosh:"))
# print(f'Mening ismim {name} yoshim {age}')

# N19

# time = int(input('Sekundlarni kiriting:'))
# hour = time // 3600
# time = time // 3600
# minut = time // 60
# time = time // 60
# print(f'{hour} soat {minut} minut {time} sekund')


# N20

# word = 'Chelsia'
# word = [x for x in word]
# word[0], word[-1] = word[-1], word[0]
# word = ''.join(x for x in word)
# print(word)

# N21

# str1, str2 = map(str, input().split(' '))
# str1 = str1[:len(str1)//2] + str2 + str1[len(str1)//2:]
# print(str1)

# N22

# strs = input()
# if len(strs) % 4 == 0:
#     print(strs[:len(strs)//2] + strs[len(strs)//2:][::-1])

# U2
# ls = ["ada", 212, False, 4567, "aziza"]
# for x in ls:
#     if str(x) == str(x)[::-1]:
#         print(f"{x} -> polindrom")
#     else:
#         print(f'{x} polindrom emas')

# U3
# ls =  ['abc', 'xyz', 'bolib','aba', '1221']
# count = 0
# for x in ls:
#     if len(x) >= 2 and x[0] == x[-1]:
#         count+=1
# print(count)

# U4
# ls = [23, 44, 56, 99, 111, 23, 54]
# i = 0
# while i < len(ls):
#     if ls[i] % 2 == 0:
#         ls.pop(i)
#     i+=1
# print(ls)

# ls = [87, 42, 0, 62, 124, 0, 58, 37, 74, 94, 182, 74, 94, 182, 23, 17, 62, 29, 17, 82, 54, 0, 45]
# ls = sorted(ls)
# print(ls)

# def singleNumber(nums) -> int:
#     for x in nums:
#         for xs in nums:
#             if xs == x:
#                 for xs in nums:
#                     nums.remove(xs)
#     return nums
# def single_number(nums):
    # res = "".join(str(x) for x in nums)
    # l = []
    # for x in res:
    #     if res.count(x) == 1:
    #         l.append(int(x))   
    # return l
    # ls = []
    # res = 0
    # for x in nums:
    #     res ^= x
    #     ls.append(res)
    # print(ls, res)
    # return res
# ls = [4,1,2,1,2, 4, 5, 5, 7]
# single_number(ls)
# print(singleNumber(ls))

# st = '3.6trln'
# st = int(round(float(st[:-4])))
# print(st)


# def intersect(nums1, nums2):
#     ls = []
#     for x in nums1:
#         if x in nums2:
#             ls.append(x)
#             nums2.remove(x)
#     return ls

# nums1 = [1,2]
# nums2 = [1,1]
# print(intersect(nums1, nums2))

# s = "aabb"

# for x in s:
#     count = 0 
#     for xs in s:
#         if x == xs:
#             count += 1

#     if count == 1:
#         print(x)
#         break

# def majorityElement(nums) -> int:
#     for x in nums:
#         count = 0
#         for xs in nums:
#             if x == xs:
#                 count += 1
#                 print(count)
#         if count > len(nums):
#             return x

# nums = [3,2,3]
# print(majorityElement(nums))

# n , m = map(int, input().split())
# print(n , m)

# nums = [5,3,2,4]
# i = 3
# while i:
#     n , m = map(int, input().split())
#     indeks = nums.index(n)
#     nums[indeks] = m
#     i-=1
# print(max(nums) - min(nums))

# nums = [-106, ]

# dct = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6:'mno', 7: 'pqrs', 8:'tuv', 9:'wxyz'}
# number = "23"
# ls = []
# for key, vaule in dct.items:
#     if key in number:

# candidates = [2,3,6,7] 
# target = 7
# ls = []
# for x in range(len(candidates) + 1):
#     for xs in range(1, len(candidates) + 1):
#         p = 1
#         for n in candidates[x:xs]:
#             p *= n
#         if p == target:
#             ls.extend(candidates[x:xs])

# print(ls)
# x = 2
# n = 10
# for i in range(n):
#     print(i)
#     x *= x

# nums = [2,0,1]
# for i in range(len(nums)):
#     for l in range(len(nums)):
#         if nums[i] <= nums[l]:
#             temp = nums[i]
#             nums[i] = nums[l]
#             nums[l] = temp
# print(nums)

# word1 = "abcdf"
# word2 = "pqr"
# sub = max(word1, word2, key=len)[min(len(word1), len(word2)):]
# res = ''
# for i in range(min(len(word1), len(word2))):
#     res += word1[i] + word2[i]
# print(res + sub)

# word1 = "abcdf"
# word2 = "pqr"

# interleaved = ''.join([w1 + w2 for w1, w2 in zip(word1, word2)])

# z = zip(word1, word2)
# print(z)
# remaining = max(word1, word2, key=len)[min(len(word1), len(word2)):]

# result = interleaved + remaining

# print(result)
# from itertools import zip_longest

# word1 = "abcdf"
# word2 = "pqr"

# result = ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))

# print(result)

# result = ''.join(a + b for a, b in zip_longest(word1, word2, fillvalue=''))
#         return result

# s = "helloA"
# vowels = ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']
# ls = ''

# for i in s:
#     if i in vowels:
#         ls += i

# new = ''
# for i in s:
#     if i in vowels:
#         new += ls[-1]
#         ls = ls[:-1]
#     else:
#         new += i
# print(new)

# nums = [0,1,0,3,12]
# left = 0
# for i in range(len(nums)):
#     if nums[i] != 0:
#         nums[left], nums[i] = nums[i], nums[left]
#         left += 1
# print(nums)

# nums1 = [-68,-80,-19,-94,82,21,-43]
# nums2 = [-63]
# diff1 = [num for num in nums1 if num not in nums2]
# diff2 = [num for num in nums2 if num not in nums1]
# print([diff1, diff2])
# ls = []
# ls1 = []
# ls2 = []
# for i in range(len(max(nums1, nums2, key = len))):
#     if nums1[i] not in nums2 and nums1[i] not in ls1:
#         print(nums1[i])
#         ls1.append(nums1[i])
#     if nums2[i] not in nums1 and nums2[i] not in ls2:
#         ls2.append(nums2[i])
# ls.extend([ls1, ls2])
# print(ls)

# numsm = [1,2,3,0,0,0]
# m = 3
# numsn = [2,5,6]
# n = 3

# numsm = numsm[:m]
# numsn = numsn[:n]

# numsm.extend(numsn)
# numsm = sorted(numsm)
# print(numsm)

# x = 8?"z" for x in range(x))
# i = 1
# t = 0
# while i < x + 1 and x != 0:
#     s = i * i
#     if s == x:
#         print(x)
#         t = i
#         break
#     elif s > x:
#         t = i - 1
#         break
#     i += 1
# print(t)

# num = 9996
# num = str(num)
# num = num.replace(num[num.find('6')], '9', 1)
# num = int(num)
# print(num)

# ls = [1, 2, 3, 4, 5]
# l = []
# n = 2
# i = 0
# count = 1
# while len(ls) != 0:
#     if count == n:
#         print(ls.pop(count - 1))
#         # print(ls)
#         count = 0
#     if i >= len(ls):
#         i = abs(n - i)
#     l.append(ls[i]) 
#     count += 1
#     print(ls[i])

# s = "abcdefg"
# k = 2
# print(s[:k][::-1]+s[k:])

# s = "zaz"
# sum = 0
# for i in range(len(s)):
#     if i == len(s) - 1:
#         sum += abs(ord(s[i]) - ord(s[i]))
#         break
#     sum += abs(ord(s[i]) - ord(s[i + 1]))
# print(sum)
# print(ord(s[0]))

# num = 199
# while num > 9:
#     sum1 = 0
#     while num:
#         a = num % 10
#         sum1 += a
#         num = num // 10
#     num = sum1
# print(sum1)


# while n != 1 and n != 2:
#     n = n % 3
#     if n == 0:
#         print(True)
#         quit()
# print(False)

# if n <= 0: 
#     return Fals
# e

# n = 60000
# sum1 = 0
# while (n-1):
#     if n%3 != 0:
#         pass
#     n//=3
#     sum1 += 1

# n = 60000
# sum1 = 0
# for i in range(n):
#     if 3**i == n:
#         print(True)
#         quit()
#     elif 3**i > n:
#         print(sum1)
#         quit()
#     sum1 += 1
# # print(False)
# print(sum1)

# s = "abcd"
# m = s
# m = list(m)
# # sr = s[::-1]
# for i in m:
#     for l in m:
#         g = s[::-1] + i
#         if g == g[::-1]:
#             print(g)
#             break

# n = 2
# count = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#        count += 1
# if count == 3:
#     print(True) 
# else:
#     print(False)

# num = "35427"
# while len(num):
#     if int(num) % 2 != 0:
#         print(num)
#         quit()
#     num = num[:-1]
# print("")

# num = 687

# num = sorted(list(str(num)))
# sum1 = ''
# sum2 = ''
# for i in range(len(num)):
#     if i % 2:
#         sum1 += num[i]
#     else:
#         sum2 += num[i]
# print(int(sum1) + int(sum2))

# board = [
#         [".",".",".",".","5",".",".","1","."],
#         [".","4",".","3",".",".",".",".","."],
#         [".",".",".",".",".","3",".",".","1"],
#         ["8",".",".",".",".",".",".","2","."],
#         [".",".","2",".","7",".",".",".","."],
#         [".","1","5",".",".",".",".",".","."],
#         [".",".",".",".",".","2",".",".","."],
#         [".","2",".","9",".",".",".",".","."],
#         [".",".","4",".",".",".",".",".","."]
#         ]

# c = 0
# count = 0
# for i in board:
#     c += 1
#     for m in range(len(i)):
#         if i[m] != '.' and i.count(i[m]) != 1:
#             print(False)
#             quit()
#     for l in board[c:]:
#         for x in range(len(i)):
#             if l[x] == i[x] and l.index(i[x]) == i.index(l[x]) and i[x] != '.':
#                 print(i.count(i[x]), i[x])
#                 print(l[x], i[x], l.index(i[x]), i.index(l[x]))
#                 print(False)
#                 quit()
# print(True)

# b = [[".",".",".",".","5",".",".","1","."],
#      [".","4",".","3",".",".",".",".","."],
#      [".",".",".",".",".","3",".",".","1"],
#      ["8",".",".",".",".",".",".","2","."],
#      [".",".","2",".","7",".",".",".","."],
#      [".","1","5",".",".",".",".",".","."],
#      [".",".",".",".",".","2",".",".","."],
#      [".","2",".","9",".",".",".",".","."],
#      [".",".","4",".",".",".",".",".","."]]



# num1 = "3" 
# num2 = "6"
# sum1 = 0
# sum2 = 0
# for i in range(len(num1)):
#     x = num1[0]
#     sum1 += (ord(x) - 48) * 10**len(num1) // 10
#     num1 = num1[1:]

# for i in range(len(num2)):
#     x = num2[0]
#     sum2 += (ord(x) - 48) * 10**len(num2) // 10
#     num2 = num2[1:]

# print(sum1 * sum2)

# customers = [[5,2],[5,4],[10,3],[20,1]]
# # ls = [sum(customers[0])]
# sum1 = 0
# sum2 = customers[0][0]
# for i in range(1, len(customers)):
#     sum2 += customers[i][0]
#     customers[i][0] = sum(customers[i-1])
#     sum1 += sum(customers[i-1]) + customers[i][1]
# print((sum1 + customers[-1][1] - sum2) / len(customers))

# dct = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6':'mno', '7': 'pqrs', '8':'tuv', '9': 'wxyz'}

# logs = ["./","wz4/","../","mj2/","../","../","ik0/","il7/"]
# count = 0
# for i in logs:
#     if i == '../':
#         count -= 1
#     elif i == './':
#         continue
#     else:
#         count += 1
#     if count < 0:
#         count = 0
# print(count)

# words = ["cat","bt","hat","tree"]
# chars = "atach"
# c = chars
# count = 0
# for i in words:
#     chars = c
#     for l in range(len(i)):
#         if i[l] in chars:
#             chars.replace(chars.find(i[l]), '', 1)
#             count += 1
#             print(chars)
#             quit()
# print(count)

# matrix = [[1,2,3],
#           [4,5,6],
#           [7,8,9]]

# ls = []
# k = []
# start = -1
# for m in matrix:
#     start += 1
#     for i in matrix:
#         for l in range(len(i)):
#             ls.append(i[l])
#             break
#     k.append(ls)
# print(k)

# names = ["Alice","Bob","Bob"]
# heights = [180,165,170]
# m = list(zip(names, heights))
# sorted_tuple = sorted(m, key = lambda x: x[1], reverse=True)
# ls = [i[0] for i in sorted_tuple]
# print(ls)
# for i in range(len(names)):
#     mdct[names[i]] = heights[i]
# print(mdct)
# dct = dict(sorted(m.items(), key = lambda item: item[1], reverse=True))
# ls = []
# for key, value in dct.items():
#     ls.append(key)
# print(ls)

# mountain = [2,4,4]
# ls = []
# for i in range(1, len(mountain) - 1):
#     if mountain[i] > mountain[i+1] and mountain[i] > mountain[i-1]:
#         ls.append(i)

# print(ls)

# mat = [[1,2],[3,4]]
# r = 1
# c = 4


# a = -2147483648
# b = -1
# print(a // b)

# g = [1,2] 
# s = [1,4,3]
# count = 0


# s = "(ed(et(oc))el)"
# c = s.count('(')
# print(s.find(')', c))
# c2 = 0
# res = ''
# for i in s:
#     if i == '(':
#         c2 += 1
#     if i == '(' and c == c2:
#         for l in s[s.index(i):]:
#             if l == ')':
#                 res += s[:s.index(i)] + s[:s.index(l)][::-1]
#                 print(res)
                        
# s = "(()[]{})"
# b = 0
# if s.count('(') != s.count(')'):
#     return False
# if s.count('[') != s.count(']'):
#     return False
# if s.count('{') != s.count('}'):
#     return False
# n = 3
# p = ['((()))']

# for i in nums:
#     if nums.count(i) == 1:
#         ls.append(i)
# print(ls)
# l = []
    # c = 0
    # for l in nums:
    #     if i == l:
    #         c += 1
    # if c == 1:
    #     ls.append(i)

# nums = [1,2,1,3,2,5]
# ls = []
# res = 0
# for i in nums:
#     res ^= i
#     print(res) 
# print(ls)

# words = ["i","love","leetcode","i","love","coding"]
# k = 2
# dct = {}
# for i in set(words):
#     dct[i] = words.count(i)

# sorted_dct = sorted(dct.items(), key = lambda x: x[1])
# print(sorted_dct)
# ls = [x[0] for x in sorted_dct[-1:k:-1]]
# print(ls)

# for x in range(len(ls), -1, -1):
#     print(ls[x])

# s1 = "this apple is sweet".split()
# s2 = "this apple is sour".split()
# s1 += s2
# ls = []
# for i in s1:
#     if s1.count(i) == 1:
#         ls.append(i)
# print(ls)

# arr = [37,12,28,9,100,56,80,5,12]
# arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
# print(arr)
# arr = sorted(arr)[(len(arr) * 5) // 100:(len(arr) * 95) // 100]
# print(sum(arr) / len(arr))
 

# s = "Myself2 Me1 I4 and3".split()
# s = list(sorted(s, key = lambda x: int(x[-1])))
# s = ' '.join(list(map(lambda x: x[:-1], s)))
# print(s)

# nums = [1,3,6,10,12,15]
# sumx = 0
# count = 0
# for i in nums:
#     if i % 3 == 0 and i % 2 == 0:
#         sumx += i
#         count += 1
# print(sumx // count)

# nums = [1,2,5,2,3]
# target = 2
# nums = sorted(nums)
# ls = []
# for i in range(len(nums)):
#     if nums[i] == target:
#         ls.append(i)
# print(ls)

# num = 30
# summ = 0
# for i in range(2, num + 1):
#     summa = 0
#     i = list(str(i))
#     for l in i:
#         summa += int(l)
#     if summa % 2 == 0:
#         summ += 1
# print(summ)

# num = 4
# count = 0
# for i in range(2, num + 1):
#     summa = 0
#     i = list(str(i))
#     for l in i:
#         summa += int(l)
#     if summa % 2 == 0:
#         count += 1
# return count

# words = ["cool","lock","cook"]

# ls = []
# for i in words[0]:
#     count = 0 
#     for l in words:
#         if i in l:
#             count += 1
#     if count == len(words):
#         ls.append(i)
# print(ls)

# nums = [3,1,2,10,1]
# for i in range(1, len(nums)):
#     nums[i] += nums[i-1]
# print(nums)


# title =  "L hV".split()
# res = ''
# for i in title:
#     if len(i) > 2:
#         res += i.title() + " "
#     else:
#         res += i.lower() + " "
# print(res[:-1])

    
# s = "cb34"
# s = list(s)
# for i in s:
#     if i.isdigit():

# arr = [-3,0,1,-3,1,1,1,-3,10,0]
# ls = []
# for i in set(arr):
#     if arr.count(i) in ls:
#         print(False)
#         quit()
#     ls.append(arr.count(i))
# print(True)

# dct = {'I': 1, 'V': 5, "X":10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# s = list("MCMXCIV")
# summa = 0
# for i in range(len(s)):
#     if i + 1 < len(s) and dct[s[i]] < dct[s[i + 1]]:
#         summa -= dct[s[i]]
#     else:
#         summa += dct[s[i]]

# print(summa)

# text = "loonbalxballpoon"

# balloon = 'balloon'
# count = 0
# for i in balloon:
#     if i in text:
#         text.replace('', i)
#         count += 1
# print(text)

# nums = [12,345,2,6,7896]
# count = 0
# for i in nums:
#     if len(str(i)) % 2 == 0:
#         count += 1
# print(count)
# count2 = 0
# for i in nums:
#     count = 0
#     for l in str(i):
#         if int(l) % 2 == 0: 
#             count += 1
#     if count == len(str(i)):
#         count2 += 1
# print(count2)

# arr = [17,18,5,4,6,1]
# for i in range(len(arr) - 1):
#     arr[i] = max(arr[i+1:])
# arr[-1] = -1
# print(arr)

# grid = [[4,3,2,-1],
#         [3,2,1,-1],
#         [1,1,-1,-2],
#         [-1,-1,-2,-3]]

# count = 0
# for i in grid:
#     for l in i:
#         if l < 0:
#             count += 1
# print(count)

# num = 7
# count = 0
# for i in list(str(num)):
#     if not num % int(i):
#         count += 1
# print(count)
# count = 1
# for i in range(1, num//2):
#     if not num % i:
#         count += 1
# print(count)

# n = 10000
# m = n
# count = 0
# count2 = 0
# while n != 1:
#     if n % 2:
#         n = n + 1
#         count += 1
#     else:
#         n = n // 2
#         count += 1

# while m != 1:
#     if m % 2:
#         m = m - 1
#         count2 += 1
#     else:
#         m = m // 2
#         count2 += 1

# print(min(count, count2))


# n = 5 
# m = 1
# num1 = 0
# num2 = 0
# for i in range(n + 1):
#     if i % m:
#         num1 += i
#     else:
#         num2 += i
# print(num1-num2)

# nums = [2,3,1,3,2]
# nums = sorted(nums, reverse = True)
# # print(nums)
# ls = sorted(nums, key = lambda x: nums.count(x))
# print(ls)

# n = 11
# res = ''
# while n:
#     res += str(n % 2)
#     n = n // 2
# print(res.count('1'))

# ls = []
# n = 15
# for i in range(1, n + 1):
#     if i % 15 == 0:
#         ls.append('FizzBuzz')
#     elif i % 3 == 0:
#         ls.append('Fizz')
#     elif i % 5 == 0:
#         ls.append('Buzz')
#     else:
#         ls.append(i)
# print(ls)

# mat = [[0,0,0],[0,1,1]]
# ls = []
# for i in range(len(mat)):
#     ls.append([i, mat[i].count(1)])
# ls = sorted(ls, key = lambda x: x[1], reverse=True)
# print(ls[0])

# s = "cb34"
# sl = 'salom'
# ls = []
# # print(sl.lstrip(''))
# for i in range(len(s)):

#     if s[i].isdigit() and i != 0:
#       ls.extend([i, i-1])
# print(ls)
# 
# nums = [1,1,2,4,9]
# k = 1
# count = 0
# for i in nums:
#     if i < k:
#         count += 1
# print(count)  

# nums = [1,1,1,1]
# if len(nums) % 2 == 0:
#     for i in set(nums):
#         if nums.count(i) > 2:
#             print(False)
#             quit()
#     print(True)
#     quit()
# print(False) 
        # print(f"{matrix[l][i]} = [{l}, {i}]")
        # print(f"{matrix[i][l]} = {matrix[l][i]}")
        # print(f"{matrix[i][l]} = [{i}, {l}]")

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
# matrix2 = []
# ls = []
# for i in range(len(matrix)):
#     ls = []
#     for l in range(len(matrix[i])-1, -1, -1):
#         ls.append(matrix[l][i])
#     matrix2.append(ls)
    
# for i in range(len(matrix)):
#     for l in range(len(matrix2)):
#         matrix[i][l] = matrix2[i][l]

# n = len(matrix)
# for i in range(0, n):
#     for j in range(i+1, n):
#         matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
#         print(j)


# print(matrix)
# for i in range(n):
#         matrix[i].reverse()

# items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]] 
# ruleKey = "type"

# ruleValue = "phone"
# if ruleKey == 'type':
#     ruleKey = 0
# elif ruleKey == 'color':
#     ruleKey = 1
# else:
#     ruleKey = 2


# count = 0
# for i in items:
#     if ruleValue == i[ruleKey]:
#         count += 1
# print(count)

# s = "string"
# res = ''
# for i in range(len(s)):
#     if s[i] == 'i':
#         # print(s)
#         res = res[::-1]
#     else:
#         res += s[i]
# print(res)


# board = [["5","3",".",".","7",".",".",".","."],
#          ["6",".",".","1","9","5",".",".","."],
#          [".","9","8",".",".",".",".","6","."],
#          ["8",".",".",".","6",".",".",".","3"],
#          ["4",".",".","8",".","3",".",".","1"],
#          ["7",".",".",".","2",".",".",".","6"],
#          [".","6",".",".",".",".","2","8","."],
#          [".",".",".","4","1","9",".",".","5"],
#          [".",".",".",".","8",".",".","7","9"]]

# nums = [1,2,0]
# for i in range(1, max(nums) + 1):
#     if i not in set(nums):
#         print(i)
#         quit()
# print(max(nums) + 1)

# s = "aacecaaa"
# p = ''
# for i in range(len(s)-1, -1, -1):
#     p += s[i]
#     a = s[:i]
#     if a == a[::-1]:
#         for l in range(len(p)-1, -1, -1):
#             s = p[l] + s
#             if s == s[::-1]:
#                 print(s)
#                 quit() 
        
# s = "(1+(4+5+2)-3)+((6+8)) - 12"

# max_sum = 0
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# for i in range(len(nums)):
#     if sum(nums[:i]) > max_sum:
#         max_sum = sum(nums[:i])
#         part = nums[:i]
# print(part)

# matrix = [[1,1,1],
#           [1,0,1],
#           [1,1,1]]
# for i in matrix:
#     for l in range(len(i)):
#         if l == 0:

# ls = []
# for i in nums:


# nums = [1,2,3]

# result = [[]]
# for num in nums:
#     result += [i + [num] for i in result]
# print(result)

# from  itertools import combinations

# n = 4
# k = 2
# ls = [list(comb) for comb in combinations(range(1, n + 1), k)]


# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# set2 = set(nums1).intersection(set(nums2))
# print(list(set2))

# nums1 = [1,2,3]
# nums2 = [2,4]

# # set2 = set(nums1).intersection(set(nums2))
# print(min(list(set(nums1).intersection(set(nums2)))))

# nums = [3,1,2,4]

# for i in nums:
#     if i % 2 == 0:
#         print(i)
#         nums.insert(0, i)
# print(nums)


# def to_decimal_sum(binary):
#     sum = 0
#     n = len(binary)
#     for i in range(len(binary)):
#         n = n - 1
#         if binary[i] != '0':
#             sum += 2 ** n
#     return sum

# def to_binary(num):
#     res = ''
#     while num:
#         res += str(num % 2)
#         num //= 2
#     return str(res[::-1])

# a = "1010"
# print(to_binary(to_decimal_sum(a)))
# b = "1011"
# num = to_decimal_sum(a) + to_decimal_sum(b)
# print(to_binary(num))

# haystack = "sdbutsd"
# needle = "sad"
# print(haystack.find(needle))

# nums = [3,30,34,5,9]
# nums = sorted(nums, key = lambda x: int(str(x)[0]), reverse = True)
# nums
# from functools import cmp_to_key

# # Custom comparator function
# def compare(x, y):
#     if str(x) + str(y) > str(y) + str(x):
#         return -1
#     else:
#         return 1

# nums = [10, 2]
# nums = sorted(nums, key=cmp_to_key(compare))
# print("".join(str(x) for x in nums))

# s = ["h","e","l","l","o"]
# s2 = s[::-1]

# for i in range(len(s)):
#     s[i] = s2[i]

# jewels = "aA" 
# stones = "aAAbbb"
# count = 0

# for i in stones:
#     if i in jewels:
#         count += 1
# print(count)
# print(len(stones))

# s = "RLRRLLRLRL"
# s2 = s
# c = 0
# i = 2
# a = s
# while len(s) != 0:
#     if a.count('R') == a.count('L'):
#         c += 1
#         print(s)
#         s = s[i:]
#     i += 1
#     a = s[:i]
# print(c)

# nums = [1,2,1]
# nums = nums + nums
# print(nums)

# nums = [3,6,9]
# c = 0
# for i in nums:
#     if i % 3:
#         c+=1
# print(c)

# left = 47
# right = 85

# ls = []
# for i in  range(left, right + 1):
#     count = 0
#     for l in str(i):
#         if '0' in str(i):
#             break
#         if i % int(l) == 0:
#             count += 1
#     if count == len(str(i)):
#         ls.append(i)
# print(ls)

# "dcbaefd"
# word = "abcd"
# ch = "z"
# if ch in word:
#     n = word.find(ch)
#     word = word[:n+1][::-1] + word[n+1:]
#     print(word)
# else:
#     print(word)

# nums = [0,0,1,1,1,2,2,3,3,4]
# n = len(nums)
# nums = list(set(nums))
# u = n - len(nums)
# while u != 0:
#     nums.append('_')
#     u -= 1
# print(nums)

# digits = [1,2,3]

# ls = [int(l) for l in (str(int(''.join(str(x) for x in digits)) + 1))]


# nums = [1,2,3,4,5,6,7]
# k = 3
# nums = nums[k+1:] + nums[:k+1]
# print(nums)


# s = "RLRRLLRLRL"
# count = 0
# i = 1
# while len(s) != 0:
#     if s[:i].count('R') == s[:i].count('L'):
#         count += 1
#         s = s[i:]
#     i += 1
# # if s.count('R') == s.count('L'):
# #     count += 1
# print(count)

# sentence = "thequickbrownfoxjumpsoverthelazydog"
# a1 = 'abcdefghijklmnopqrstuvwxyz'
# sentence = ''.join(sorted(set(sentence)))
# # print(len(sentence[:26]))
# if len(sentence) <= 26 and sentence[:26] == a1:
#     print(True)
#     quit()
# print(False)

# details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
# # count = 0
# # for i in details:
# #     if int(i[11:13]) >= 60:
# #         count += 1
# # print(count)

# print(sum(1 for i in details if int(i[11:13]) >= 60))

# nums = [-1,1,2,3,1]
# target = 2
# count = 0
# for i in range(len(nums)):
#     for l in range(1, len(nums)):
#         if nums[i] + nums[l] < target and i < l:
#             count += 1
# print(count)

# nums = [10,4,8,3]

# leftSum = [0]
# rightSum = [0]
# for i in range(len(nums) - 1):
#     leftSum.append(leftSum[-1] + nums[i])
#     rightSum.append(rightSum[-1] + nums[::-1][i])

# rightSum = rightSum[::-1]

# answer = [abs(l - r) for l, r in zip(leftSum, rightSum)]
# print(answer)

# n = 3
# summa = 0
# for i in range(n // 2):
#     summa += n - (i * 2 + 1)
# print(summa)

# nums = [2,2,2]

# for i in set(nums):
#     nums.append(int(str(i)[::-1]))
# print(len(set(nums)))

# nums = [5,7,7,8,8,10]
# target = 8  

# def return_target_index(nums, target):
#     left, right = 0, len(nums) - 1

#     ls = []
#     while left <= right:
#         mid = (left + right) // 2
#         mid_value = nums[mid]
        
#         if mid_value == target:
#             return mid
#         elif mid_value < target:
#             left = mid + 1
#         else:
#             right -= 1
#     return [-1, -1]

# i = 2
# ls = []
# while i != 0:
#     n = (return_target_index(nums, target)[0])
#     nums.pop(n)
#     ls.append(n)
#     i -= 1
# print(ls)

# nums = [7,8,3,4,15,13,4,1]
# n = len(nums) // 2
# avg = []
# while n != 0:
#     minimum = min(nums)
#     maximum = max(nums)
#     avg.append((maximum + minimum) / 2)
#     nums.remove(maximum)
#     nums.remove(minimum)
#     n -= 1
# print(min(avg))

# nums = [1, 2, 3, 4, 10, 12]
# summa = sum(x for x in nums if x > 9)
# print(summa)
    
# x = 18
# s = sum(int(i) for i in str(x))
# print(x % s == 0)

# s = "abccbaacz"
# res = ''
# for i in s:
#     if i not in res:
#         res += i
#     else:
#         print(i)
#         quit()

# def detec(s):
#     if s.isupper():
#         return True
#     elif s.islower():
#         return True
#     elif s[0].isupper():
#         b = True
#         for i in range(1, len(s)):
#             if s[i].isupper():
#                 b = False
#                 break
#         return b


# s = 'SaLom'
# print(detec(s))


# words = ["$easy$","$problem$"]
# separator = "$"
# ls = [x for i in words for x in i.split(separator) if x != '']
# print(ls)

# s = list("abacbc")
# n = s.count(s[0])
# for i in set(s):
    
# s = "1 box has 3 blue 4 red 6 green and 12 4 yellow marbles".split()
# ls = [int(i) for i in s if i.isdigit()]
# for i in range(len(ls) - 1):
#     if ls[i] >= ls[i+1]:
#         print(False)
#         quit()
# print(True)

# words = ["are","amy","u"]
# left = 0
# right = 2
# vowels = ['a', 'o', 'e', 'i', 'u']
# count = 0
# while left <= right:
#     if words[left][0] in vowels and words[left][-1] in vowels:
#         count += 1
#     left += 1
# print(count)


# words = ["blue","green","bu"]

# ls = []
# for i in range(len(words)):
#     for l in range(len(words)):
#         if words[l] in words[i] and i != l:
#             ls.append(words[l])
# print(ls) 

# nums = [3,3]
# nums.sort()
# minn, maxx = nums[0], nums[-1]
# i = minn
# while i > 0:
#     if maxx % i == 0 and minn % i == 0:
#         print(i)
#     i -= 1

# nums = [1,2,3,2]

# count = {}
# for num in nums:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# print(sum(i for i, cnt in count.items() if cnt == 1))

# nums = nums = [1,2,3,4]

# count = {}

# for num in nums:
#     if num in count:
#         count[num] += 1
#     else:
#         count[num] = 1

# for num, cnt in count.items():
#     if cnt % 2:
#         print(False)
#         quit()
# print(True)

# from collections import Counter


# words1 = ["a","b","ab"]
# words2 = ["a","a","a","ab"]
# count1 = Counter(words1)
# count2 = Counter(words2)

# count = 0
# for word in count1:
#     if count1[word] == 1 and count2[word] == 1:
#         count += 1
# print(count)

# nums = [4,1,2,3]
# nums = sorted(nums, key = lambda x: nums.index(x) % 2 == 0)
# nums = sorted(nums, key = lambda x: nums.index(x) % 2)
# print(nums)

# nums = [16, 16]
# n = len(nums)
# dct = {}
# index = 0
# for i in nums:
#     index += 1
#     dct[index] = i

# summa = 0
# for key, index in dct.items():
#     if n % key == 0:
#         summa += index ** 2
# print(summa)

# print(nums)

# nums = [13,25,83,77]
# # nums = [int(x) for x in list(("".join(str(i) for i in nums)))]
# # nums = [int(x) for x in ''.join([str(i) for i in nums])]
# res = ""
# for i in nums:
#     res += str(i)
# res = [int(x) for x in res]
# print(res)

# mat = [
#         [1, 2, 3, 4],
#         [5, 6, 7, 8],
#         [9,10,11,12],
#         [13,14,15,16]
#                     ]

# for i in range(len(mat)):
#     for l in range(len(mat)):
#         if mat:
#             print(mat[i][l])

# words = ["abc","car","adja","racjecar","cool"]
# for i in words:
#     if i == i[::-1]:
#         print(i)
#         quit()
# print("")

# nums1 = [1,3,4] 
# nums2 = [1,3,4]
# k = 1
# count = 0
# for i in nums2:
#     for l in nums1:
#         if l % (i * k) == 0:
#             count += 1
# print(count)

# sentence = "Leetcode is cool".split(' ')
# count = 0
# for i in range(-1, len(sentence) - 1):
#     if sentence[i][-1] == sentence[i+1][0]:
#         count += 1
# if count == len(sentence):
#     print(True)
#     quit() 
# print(False)

# s = "abab"
# for i in range(len(s) - 1):
#     if s[i] == 'b' and s[i + 1] == 'a':
#         print(False)
#         quit()
# print(True)


# strs = ["alic3","bob","3","4","00000", 'olim']
# ls = []
# for x in range(len(strs)):
#     if strs[x].isdigit():
#         ls.append(int(strs[x]))
#     else:
#         l = [len(strs[x])]
#         for xs in range(len(strs[x])):
#             if strs[x][xs].isdigit():
#                 l.append(int(xs))
#         ls.append(max(l))
# print(max(ls))


# words = ["alice","bob","charlie"]
# res = ''
# for i in words:
#     res += i[0]
# print(res)

# s = "abc"

# num = "0051230100"
# res = ''
# for i in range(len(num)):
#     if num[i] != '0':
#         res += num[i:]
#         print(res)
#         quit()

# n = 10
# letters = 'abc'
# res = ''
# if n % 2:
#     res += (letters[0] * (n // 2)) + (letters[1] * (n // 2)) + letters[2]
# else:
#     res += (letters[0] * (n - 1)) + (letters[1])
# print(res) 

# a = [[1, 2], 
#      [2, 4],
#      [1, 8]]

# b = [1, 2]
# ls = []


# if sum(len(x) for x in a) / len(a) == len(b):
#     for i in a:
#         res = 0
#         for x in range(len(i)):
#             res += i[x] * b[x]
#         ls.append(res)
#     print(ls)
# else:
#     print(-1)

# s = "textbook"
# v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# a = s[:len(s)//2]
# b = s[len(s)//2:]
# ca = 0
# cb = 0
# for i in range(len(a)):
#     if a[i] in v:
#         ca += 1
#     if b[i] in v:
#         cb += 1
# print(ca == cb)

# s = "abcdefghi"
# s = "abcdefghikd"
# k = 3
# fill = "x"
# s += fill * 0 if (len(s) % k) == 0 else fill * (k - (len(s) % k))
# count = 0
# ls = []
# res = ''
# for i in s:
#     count += 1
#     res += i
#     if count == 3:
#         ls.append(res)
#         res = ''
#         count = 0
# print(ls)



# import pandas as pd
# import numpy as np

# a = pd.DataFrame(a)
# a = (a.T)
# a =  a.values.tolist()
# print(a)

# a = [[1,2],
#      [3,4],
#      [5,6]]

# k = []
# for i in range(len(a)):
#     res = []
#     for l in range(len(a)):
#         res.append(a[i][l])
#     k.append(res)
# print(k)

# ls = []
# for i in zip(*a):
#     ls.append(list(i))
# print(ls)

# matrix = [[2, 1], 
#           [1, 2]]

# b = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] 
# print(D) 

# A = [
#     [1,2],
#     [2,4]]

# B = [
#     [2,1],
#     [3,4]]

# # if len(A[0]) != len(B):
# #     print(-1)
# #     quit()
# # else:
# for i in zip(A, B):
#     print(i)

# nums = [-4,-1,0,3,10]
# print(sorted([x**2 for x in nums], key = lambda x: x))


# paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."[:-1].lower.split()
# banned = ["hit"]
# print(paragraph)
# for i in paragraph:
#     if 


# s = "x"

# start = 0
# end = 3
# count = 0
# while end != len(s) + 1:
#     if len(set(list(s[start:end]))) == len(s[start:end]):
#         count += 1
#     start += 1
#     end += 1
# print(count)

# print(len(set(list(s))))

# num ="222"
# ls = []
# if len(num) >= 3:
#     start = 0
#     end = 3
#     count = 0
#     while end != len(num) + 1:
#         if len(set(list(num[start:end]))) == 1:
#             ls.append(int(num[start:end]))
#         start += 1
#         end += 1
#     if len(ls) == 0:
#         print("")
#         quit()
#     print(max(ls) if max(ls) != 0 else '000')
# else:
#     print('')

# v = "aeiou"

# words = ["cat","bt","hat","tree"]
# chars = "atach"

# count = 0

# for i in words:
#     for l in i:

# arr = [1,4,2,5,3]

# summa = 0

# k = 0
# while k < len(arr):
#     for i in range(len(arr) - k):
#         summa += sum(arr[i:k+i+1])
#     k += 2
# print(summa)

# nums = [2,5,1,3,4,7]
# ls = [item for pair in zip(nums[:len(nums)//2], nums[len(nums)//2:]) for item in pair]
# print(ls)

# hours = [0,1,2,3,4]
# target = 2
# count = 0
# for i in hours:
#     if i >= target:
#         count += 1
# print(count)

# sum(1 for i in hours if i >= target)

# nums1 = [2,3,2]
# nums2 = [1,2]

# count1 = 0
# count2 = 0
# for i in range(len(nums1)):
#     if nums1[i] in set(nums2):
#         count1 += 1

# for i in range(len(nums2)):
#     if nums2[i] in set(nums1):
#         count2 += 1

# print([count1, count2])

# mat = [[1,2,3],
#        [4,5,6],
#        [7,8,9]]

# n = len(mat)
# total_sum = 0
# for i in range(len(mat)):
#     total_sum += mat[i][i] + mat[i][n - i - 1]

# if n % 2:
#     total_sum -= mat[n // 2][n // 2]

# print(total_sum)

# s = "yo|uar|e**|b|e***au|tifu|l".split('|')
# res = ""
# for i in range(0, len(s), 2):
#     res += s[i]
# print(res.count('*'))

# s = list("cb34")
# for i in s:
#     if i.isdigit():
        
# words = ["ab","ba","cc"]
# count = 0
# ls = []
# for i in range(len(words)):
#     for j in range(len(words)):
#         if words[i] == words[j][::-1] and j not in ls:
#             print(words[i], words[j][::-1])
#             ls.append(i)
#             count += 1
# print(count)

# s = "baabb"
# if s == s[::-1]:
#     print(1)
#     quit()
# print(len(set(s)))
# count = 0
# i = len(s)
# while i != 0:
#     if s[:i] == s[:i][::-1]:
#         count += 1
#         s = s[i:]
#         i = len(s) + 1
#     i -= 1
# print(count)

# s = "RLRRRLLRLL"
# count = 0
# ans = 0
# for i in range(len(s) - 1, -1, -1):
#     count += 1
#     if s[i] == 'L':
#         count -= 1
#     if count == 0:
#         ans += 1
# print(ans)

# words = ["cool","lock","cook"]
# ans = []
# for i in words[0]:
#     count = 0
#     for l in words:
#         if i in l:
#             count += 1

# nums = [1,2,2,3,1,4]
# ans = 0
# ls = []
# for i in set(nums):
#     ls.append(nums.count(i))
# print(sum(i for i in ls if i == max(ls)))

# nums = [1,15,6,3]
# ans = 0
# for i in nums:
#     for x in list(str(i)):
#         ans += int(x)
# print(abs(sum(nums) - ans))


# s = "(()[]{})"
# for i in list(set(s)):
#     print(s.count(i))


# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
# ls = []
# count = 0

# nums4 = [nums1, nums2, nums3]
# # print(nums4)
# for i in nums4:
#     for l in i:

# matrix = [[0,1,2,0],
#           [3,4,5,2],
#           [1,3,1,5]]

# s = "cars"
# words = ["car","ca","rs"]

# s = "abc"
# t = "ahbgdc"
# s = "leeeeetcode"

# t2 = t
# for i in t:
#     if i not in s:
#         t2 = t2.replace(i, "", 1)
# print(len(set(t2)) == len(set(s)) or s in t2)
# print(t2)

# source = ["/*Test program */", 
#           "int main()", 
#           "{ ", "  // variable declaration ", 
#           "int a, b, c;", "/* This is a test", 
#           "   multiline  ", "   comment for ", 
#           "   testing */", "a = b + c;", "}"]
# res = ' '.join(source)
# print(res)


# s = "TO BE OR NOT TO BE".split()
# ls = []
# res = ""
# for l in range(len(max(s))):
#     res = ''
#     for i in s:
#         if i[l]:
#             res += i[l]
#         else:
#             res += " "
#     ls.append(res)
# print(ls)

# s = list("abcde")
# goal = "abced"
# n = len(s)
# while n > 0:

# num = 526
# num = str(num)
# print(len(str(num)) == len(str(int(str(num)[::-1]))))

# n = 13
# ls = []
# for i in range(1, n + 1):
#     ls.append(sum(int(x) for x in list(str(i))))
# # print(ls.count(1))
# print(max(ls, key = lambda x: ls.count(x)))

# n = 11
# res = ''
# for i in range(1, n + 1):
#     res += str(i)
# print(res[11 - 1])

# from itertools import combinations

# word = list("aba")
# a = combinations(word, 2)
# print(list(a))



# rings = "G4"
# numbers = []
# for l in rings:
#     if l.isdigit():
#         numbers.append(l)
# numbers = list(set(numbers))

# colors = "BGR"
# ls = []
# for i in range(0, len(rings), 2):
#     a = (rings[i] + rings[i + 1])
#     ls.append(a)
# ls2 = []

# for x in numbers:
#     res = []
#     for xs in range(len(ls)):
#         if ls[xs][1] == x:
#             res += ls[xs][0]
#     ls2.append("".join(sorted(list(set(res)))))

# count = 0
# for k in ls2:
#     if k == colors:
#         count += 1
# print(count)

# vowels = 'aeiou'
# s = list("lEetcOde")

# ans = sorted(s, key = lambda x: x if x.lower() in vowels)

# vowels = 'aeiou'
# s = list("lEetcOde")

# ans = sorted(s, key=lambda x: (x.lower() not in vowels, x.lower()))
# print(ans)

# s = "abc"
# t = "ahbgdc"

# heights = [1,1,4,2,1,3]
# print(sum(1 for x, y in zip(heights, sorted(heights)) if x != y))


# nums = [-1,0,1,2,-1,-4]
# ls = []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         for k in range(len(nums)):
#             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0 and [nums[i], nums[j], nums[k]] not in ls:
#                 ls.append([nums[i], nums[j], nums[k]])
# print(ls)

# matrix = [[0,1,2,0],
#           [3,4,5,2],
#           [1,3,1,5]]

# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         a = i
#         if matrix[i][j] == 0:

# nums = [5,7,7,8,8,10]
# target = 8

# dictionary = ["cat","bat","rat"]
# sentence = "the cattle was rattled by the battery".split()
# ls = []
# for j in sentence:
#     for i in dictionary:

# for j in sentence:
#     for i in dictionary:
#         if j.startswith(i):
#             ls.append(i)
#         else:
#             ls.append(j)
# print(" ".join(ls))

# text = "Keep calm and code on".split()
# print(" ".join(sorted(text, key = lambda x: len(x))).capitalize())

# s = "icodeinpython"
# s = list(s)
# spaces = [1,5,7,9]
# i = 0
# while i < len(spaces):
#      s.insert(spaces[i] + i, " ")
#      i += 1
# print("".join(s))

# word = "aba"
# substrings = []
# res = ''
# vowels = 'aouie'
# for i in range(len(word)):
#     for j in range(i + 1, len(word) + 1):
#         res += (word[i:j])

# count = 0
# for i in res:
#     if i in vowels:
#         count += 1
# print(count)

# word = "aba"
# vowels = 'aouie'

# count = sum(1 for i in range(len(word)) for j in range(i + 1, len(word) + 1) for c in word[i:j] if c in vowels)

# print(count)

# n = 2
# commands = ["RIGHT","DOWN"]


# grid = [[1,1,1,1,1],
#         [1,1,1,1,1],
#         [1,1,2,1,1],
#         [1,1,1,1,1],
#         [1,1,1,1,1]]

# submatrices = []

# for i in range(len(grid) - 2): 
#     for j in range(len(grid) - 2): 
#         submatrix = max([row[j:j+3] for row in grid[i:i+3]])
        
#     submatrices.append(submatrix)

# print(submatrices)

# grid = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 2, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1]
# ]

# max_matrix = []

# for i in range(len(grid) - 2): 
#     row_max = []
#     for j in range(len(grid) - 2): 
#         row_max.append(max([item for sublist in [row[j:j+3] for row in grid[i:i+3]] for item in sublist]))
#     max_matrix.append(row_max)
# print(max_matrix)

# n = 5
# count = 0
# i = 1
# do
#     i *= 2
#     count += 1
#     print(i)
# while n > i:
# # print(count)

# s = "abcde"
# t = "edbac"
# print(sum(abs(i - s.index(t[i])) for i in range(len(s))))

# s = "RLRRRLLRLL"
# count = 0
# res = ''
# for i in s:
#     res += i
#     if res.count('R') == res.count('L'):
#         res = ""
#         count += 1
# print(count)

# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# res = ''
# for i in indices:
#     res += s[i]
# print(res)

# s = "abcd"
# s = "egcfe"
# s2 = list(s)
# for i in range(len(s)):
#     if s2 == s2[::-1]:
#         print("".join(s2))
#         quit()
#     if s2[i] != s2[len(s2)-1-i] and ord(s2[i]) < ord(s2[len(s2)-1-i]):
#         s2[len(s2)-1-i] = s2[i]
#     if s2[i] != s2[len(s2)-1-i] and ord(s2[i]) > ord(s2[len(s2)-1-i]):
#         s2[i] = s2[len(s2)-1-i]
# print("".join(s2))
            
# s = "a1c1e1"
# s = "a1b2c3d4e"
# res = ''
# for i in range(len(s)):
#     if s[i].isdigit():
#         res += chr(ord(s[i-1]) + 1)
#     else:
#         res += s[i]
# print(res)

# s = list("42")
# ans = 0
# n = len(s)
# i = 0
# while n:
#     ans += (ord(s[i]) - 48) * 10
#     print(ans)
#     i+=1
#     n-=1
# print(ans)

# s = "K1:L2"
# # s = "A1:F1"
# # s = "U7:X9"
# ans = []
# n = int(s[-1])
# m = int(s[1])
# a = ord(s[0])
# b = ord(s[3])
# for x in range(a, b + 1):
#     i = m
#     while i <= n:
#         ans.append(chr(x) + str(i))
#         i += 1
# print(ans)

# s = "ELELEEL"
# count = 0
# ls = []
# for i in s:
#     if i == 'E':
#         count += 1
#         ls.append(count)
#     else:
#         count -= 1
#         ls.append(count)
# print(ls)
