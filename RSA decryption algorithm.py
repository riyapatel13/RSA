# decoded message: why study when you can watch game of thrones

def ext_euclid(A, B):
    if (A % B == 0):
        return (B, 0, 1)
    else:
        (G, k, l) = ext_euclid(B, A%B)
        return (G, l, k - l*(A//B)) 

def find_e_inv(e, n):
    (G, k, l) = ext_euclid(e, n)
    # making it positive 
    if (k < 0):
        k += n
    return k

# returns the reversed binary representation of n
# in a list format where the 0th index is the 0th place
# ex: dec_to_bin(47) = [1,0,1,0,0,1]
def dec_to_bin(n, l):
    l.append(n % 2)
    if n > 1:
        dec_to_bin(n//2, l)
    return l

def fast_exp(base, exp, n): 
    # turn exp to binary to find what powers to compute
    pow_list = dec_to_bin(exp, [])

    # list of 2^powers we need to calculate
    for i in range(len(pow_list)):
        if pow_list[i] == 1:
            pow_list[i] = i
        else:
            pow_list[i] = None
    
    # filter out all Nones
    pow_list = list(filter(lambda x : x != None, pow_list))

    # multiply them until we get all powers mod n
    base_list = []
    for i in pow_list:
        b = base % n
        while(i > 0):
            b *= (b % n)
            i -= 1
            
        base_list.append(b % n)
    
    # multiply all powers mod n
    res = 1
    for b in base_list:
        res = (res*b) % n
        
    return res

def decrypt(C, p, q, e):
    n = p*q
    totient = (p-1)*(q-1)

    # finding E^-1
    e_inv = find_e_inv(e, totient)
    
    # decrypted message
    D = [fast_exp(c, e_inv, n) for c in C]
    return D

# takes decrypted int and converts it to a string
def decode_int(n):
    alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dec_list = []
    while n > 0:
        dec_list.append(alphabet[n%27])
        n //= 27
    dec_list.reverse()

    res = ""
    for i in dec_list:
        res += i
    return res

# takes list of decrypted ints and converts it to a string
def decode_list(L):
    s = ""
    for n in L:
        s += decode_int(n)
    return s

    
C = [392482833376092259, 37946894654998926, 206997481124158797, 309293822156382938, 124367975733148998, 576469767275817590]
p = 961748941
q = 674506111
e = 7

print("message: ", C)
print("decrypted message:", decrypt(C, p, q, e))
print("decoded message:", decode_list(decrypt(C, p, q, e)))
