import re

def encode(s):
    return '/'.join([bin(ord(c)).replace('0b', '') for c in s])




def decode(s):
    st=''
    for i in range(len(s)//20):
        # print(i)
        if(not '1' in str(s[i*20:(i+1)*20])):
            break
        st+=((chr(int(s[i*20:(i+1)*20],2))))

    return st



# sub = '/'
# loca = [substr.start() for substr in re.finditer(sub, somestr)]
# print(loca[1])

def repair(s):
    sub = '/'
    sf=''
    loca = [substr.start() for substr in re.finditer(sub, s)]
    # print(len(loca))
    for i in range(len(loca)):
        loca = [substr.start() for substr in re.finditer(sub, s)]
        # print(loca)
        if(i==0):
            sf+=s[:loca[i]].rjust(20,'0')
            # print(s[:loca[i]].rjust(20,'0'))
        else:
            # print(s[loca[i-1]+1:loca[i]].rjust(20,'0'))
            sf+=s[loca[i-1]+1:loca[i]].rjust(20,'0')
            if(i==len(loca)-1):
                # print(len(s))
                # print(s[loca[i]+1:len(s)].rjust(20,'0'))
                sf+=s[loca[i]+1:len(s)].rjust(20,'0')
                # print(s[loca[i]+1:len(s)].ljust(20,'0'))
    return sf

def encrypt(code_ex,text):

    sf=''
    for i in range(len(text)//20):
        for j in range(20):
            t=int(code_ex[j])^int(text[i*20+j])
            # print(code_ex[j],text[i*20+j],t,'ok')
            sf+=str(t)
    return sf








if __name__ == "__main__":
  somestr = encode('你好啊abc123,')
  print(somestr)
  print('原文')
  print(repair(somestr))
  # print(decode(repair(somestr)))
  print('加密后')
  t = encrypt('10100010110000101010', repair(somestr))
  t2=encrypt('10100010110000101010',t)
  t3=decode(t2)
  print(t)
  print('解密后')
  print(t2)

  print(t3)