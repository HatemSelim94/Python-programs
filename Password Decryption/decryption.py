def decryptPassword(s):
    zeros_num = s.count('0')
    zeros_replacments = list(s[0:zeros_num])
    decrypted_password = []
    j = 0
    for i in range(zeros_num,len(s)):
        i = j+i
        if(i>=len(s)):
            break
        if s[i] == '0':
           decrypted_password.append(zeros_replacments.pop(-1))
        elif s[i].isalpha() and i+2 < len(s) and s[i+2] == '*':
                decrypted_password.append(s[i+1])
                decrypted_password.append(s[i])
                j += 2
        else:
            decrypted_password.append(s[i])
    decrypted_password = "".join(decrypted_password)
    return decrypted_password