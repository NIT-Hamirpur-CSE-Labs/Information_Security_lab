from struct import pack, unpack

def sha1(data):
    """ Returns the SHA1 sum as a 40-character hex string """
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    def rol(n, b):
        return ((n << b) | (n >> (32 - b))) & 0xffffffff

    # After the data, append a '1' bit, then pad data to a multiple of 64 bytes
    # (512 bits).  The last 64 bits must contain the length of the original
    # string in bits, so leave room for that (adding a whole padding block if
    # necessary).
    padding = chr(128) + chr(0) * (55 - len(data) % 64)
    if len(data) % 64 > 55:
        padding += chr(0) * (64 + 55 - len(data) % 64)
    padded_data = data + padding + pack('>Q', 8 * len(data))

    thunks = [padded_data[i:i+64] for i in range(0, len(padded_data), 64)]
    for thunk in thunks:
        w = list(unpack('>16L', thunk)) + [0] * 64
        for i in range(16, 80):
            w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)

        a, b, c, d, e = h0, h1, h2, h3, h4

        # Main loop
        for i in range(0, 80):
            if 0 <= i < 20:
                f = (b & c) | ((~b) & d)
                k = 0x5A827999
            elif 20 <= i < 40:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i < 60:
                f = (b & c) | (b & d) | (c & d) 
                k = 0x8F1BBCDC
            elif 60 <= i < 80:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            a, b, c, d, e = rol(a, 5) + f + e + k + w[i] & 0xffffffff, \
                            a, rol(b, 30), c, d

        h0 = h0 + a & 0xffffffff
        h1 = h1 + b & 0xffffffff
        h2 = h2 + c & 0xffffffff
        h3 = h3 + d & 0xffffffff
        h4 = h4 + e & 0xffffffff

    return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

s = raw_input("Input String : ")
print "Hash generated : ", sha1(s)
