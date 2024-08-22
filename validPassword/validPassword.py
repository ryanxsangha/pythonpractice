import random

c, l, s, n = 0, 0, 0, 0 #initialize count for uppercase, lowercase, special chars, nums

newpassword = input('Enter password: ')
capletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowerletters = 'abcdefghijklmnopqrstuvwxyz'
specialchar = '!@#$%^&*()?'
nums = '1234567890'

if(len(newpassword) >= 10):
    for i in newpassword:
        if(i in capletters):
            c+=1
        if(i in lowerletters):
            l+=1
        if(i in specialchar):
            s+=1
        if(i in nums):
            n+=1

if(c>0 and l>0 and s>0 and n>0 and c+l+s+n == len(newpassword)):
    print('Valid password')
else:
    print('Password must contain a capital and lowercase letter, digit, a special character, and be at least 10 characters. Try again')
