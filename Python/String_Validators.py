if __name__ == '__main__':
    s = input()
    
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        if any(eval("c." + test + "()") for c in s):
            print("True")
        else:
            print("False")
            
            
        
