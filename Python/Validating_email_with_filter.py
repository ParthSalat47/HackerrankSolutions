def fun(s):
    # return True if s is a valid email, else return False
    l = list(s)
    true_false = []
    right = -1

    for i in l:
        if i == '@':
            pos_at = l.index(i)
            #print(pos_at)
            right += 1
        if i == '.':
            pos_dot = l.index(i)
            right += 1

    if right == 1:
        true_false.append(True)
        user = []
        web = []
        ext = []
        
        for i in range(0,pos_at):
            user.append(l[i])
        if len(user) == 0:
            return False
        
        for i in range(pos_at+1,pos_dot):
            web.append(l[i])
        if len(web) == 0:
            return False
        
        dot = 0
        for i in l:
            if dot == 1:
                ext.append(i)
            if i == '.':
                dot = 1
        #breakpoint()
        if len(ext) > 3 or len(ext) == 0:
            return False
    
    else:
        return False        #1st cond.


    for i in user:  
        #print(user)
        #print(ord(i))    
        if (ord(i) < 123 and ord(i) > 96) or (ord(i) < 91 and ord(i) > 64) or (ord(i) < 58 and ord(i) > 47) or ord(i) == 95 or ord(i) == 45:
            true_false.append(True)   
            
        else:
            return False        #2nd cond
            
    for i in web:       
        if (ord(i) < 123 and ord(i) > 96) or (ord(i) < 91 and ord(i) > 64) or (ord(i) < 58 and ord(i) > 47):
            
            true_false.append(True)   
     
        else:
            return False        #3rd cond


    return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
