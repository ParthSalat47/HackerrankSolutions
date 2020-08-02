from sys import stdin, stdout

def isPalindrome(s): 
    return s == s[::-1] 

def get_array(): return list(map(int, stdin.readline().strip().split())) 


num = int(input())
array =  get_array()
#print(array)
all_array = []
any_array = []


for i in range(int(num)):
    value = array[i]
    if value >= 0:
        all_array.append(True)
    else:
        all_array.append(False)


for i in range(int(num)):
    value = array[i]
    if isPalindrome(str(value)):
        any_array.append(True)
    else:
        any_array.append(False)



#print(save)
#true_false = all(save)


if all(all_array) and any(any_array):
    print('True')
else:
    print('False')












