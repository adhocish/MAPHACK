import random
import string

def lzw_encode(s,d):
    output = ""
    w = ""
    while len(s) > 0:
        k = s[0]
        s = s[1:]
        wk = w + k
        if wk in d:
            w = wk
        else:
            output += str(d.index(w))
            d.append(wk)
            w = k
    return output

def lzw_decode(st,d):
    output = ""
    idx = len(d)-1
    code = st[:2]
    st = st[2:]
    s = d[int(code)]
    output += s
    while len(st) > 0:
        s_prev = s
        code = st[:2]
        st = st[2:]
        if code == idx:
            s = s_prev + s_prev[0]
            print "wtf"
        else:
            s = d[int(code)]
        output += s
        d.append(s_prev + s[0])
        idx += 1

    return output

def dumb_encode(s,d):
    output = ""
    for c in s:
        if c.isdigit():
            output += '0' + c
        else:
            output += str(d.index(c))
    return output

def dumb_decode(s,d):
    output = ""
    for i in xrange(0, len(s), 2):
        output += d[int(s[i:i+2])]
    return output
d = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','*','.',',',';',':','\'']
s = '104pembertonavetorontocanada*90ruesaintpaulomontrealcanada'

dumbstr = dumb_encode(s,d)
print dumbstr
print "length of dumbstr: " + str(len(dumbstr))
print dumb_decode(dumbstr,d)

lzwstr = lzw_encode(s,d)
print lzwstr
print "length of lzwstr: " + str(len(lzwstr))
print lzw_decode(lzwstr,d)

# dumb_per = 0
# lzw_per = 0
# for i in range(1000):
#     rand_str = ''.join(random.SystemRandom().choice(d) for i in range(50))
#     dumbstr = dumb_encode(rand_str,d)
#     lzwstr = lzw_encode(rand_str,d)
#     dumb_per += len(dumbstr)*1.0/len(rand_str)
#     lzw_per += len(lzwstr)*1.0/len(rand_str)

# print "average dumb compression: " + str(dumb_per / 1000)
# print "average lzw compression: " + str(lzw_per / 1000)

# for i in range(100):
#     rand_str = ''.join(random.SystemRandom().choice(d) for i in range(30))
#     temp = dumb_encode(rand_str,d)
#     temp = dumb_decode(temp,d)
#     if rand_str != temp:
#         print "failed"
#         break;
