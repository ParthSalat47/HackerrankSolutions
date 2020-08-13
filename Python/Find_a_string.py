def count_substring(string, sub_string):
    list_string = list(string)
    list_substring = list(sub_string)
    letter = 0
    count = 0
    
    for i in range(len(string)-len(sub_string)+1):
        letter = 0
        for j in range(len(sub_string)):
            if list_string[i+j] == list_substring[j]:
                letter += 1
            if letter == len(sub_string):
                count+=1
        
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
