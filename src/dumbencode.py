__d = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','*','.',',',';','\'']

def dumb_encode(s):
    output = ""
    for c in s:
        if c.isdigit():
            output += '1' + c
        else:
            output += str(__d.index(c) + 10)
    return output

def dumb_decode(s):
    output = ""
    for i in xrange(0, len(s), 2):
        output += __d[int(s[i:i+2]) - 10]
    return output

def test():
    import random
    for i in range(100):
        rand_str = ''.join(random.SystemRandom().choice(__d) for i in range(30))
        temp = dumb_encode(rand_str)
        temp = dumb_decode(temp)
        print rand_str
        print temp
        if rand_str != temp:
            print "Test failed."
            return
    print "All tests passed."
    return