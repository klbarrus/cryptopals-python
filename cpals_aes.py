#!/usr/bin/env python3
# cryptopals AES encryption/decryption

import binascii


# parameters for AES 128: key length in words, block size, number of rounds (Figure 4)
Nk = 4
Nb = 4
Nr = 10

# AES blocksize in bytes (standard says 182 bits)
AES_BLOCK = 128 // 8

# S-box (Figure 7)
S = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
     0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
     0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
     0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
     0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
     0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
     0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
     0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
     0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
     0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
     0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
     0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
     0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
     0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
     0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
     0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

# Inverse S-box (Figure 14)
Si = [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
      0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
      0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
      0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
      0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
      0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
      0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
      0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
      0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
      0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
      0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
      0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
      0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
      0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
      0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
      0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]

# section 5.2
Rcon = [0x00, 0x01000000, 0x02000000, 0x04000000, 0x08000000, 0x10000000, 0x20000000, 0x40000000,
        0x80000000, 0x1b000000, 0x36000000]


def word_to_bytes(word_in):
    a0 = (word_in >> 24) & 0xff
    a1 = (word_in >> 16) & 0xff
    a2 = (word_in >>  8) & 0xff
    a3 = (word_in      ) & 0xff
    return a0, a1, a2, a3


def SubWord(word_in):
    a0, a1, a2, a3 = word_to_bytes(word_in)
    rv = S[a0] << 24 | S[a1] << 16 | S[a2] << 8 | S[a3]
#    print('  after subword {}'.format(hex(rv)))
    return rv


def InvSubWord(word_in):
    a0, a1, a2, a3 = word_to_bytes(word_in)
    rv = Si[a0] << 24 | Si[a1] << 16 | Si[a2] << 8 | Si[a3]
#    print('  after invsubword {}'.format(hex(rv)))
    return rv


def RotWord(word_in):
    a0, a1, a2, a3 = word_to_bytes(word_in)
    rv = a1 << 24 | a2 << 16 | a3 << 8 | a0
#    print('  after rotword {}'.format(hex(rv)))
    return rv


def SubBytes(state_in):
    for i in range(0, Nb):
        state_in[i] = SubWord(state_in[i])


def InvSubBytes(state_in):
    for i in range(0, Nb):
        state_in[i] = InvSubWord(state_in[i])


def ShiftRows(state_in):
    s00, s10, s20, s30 = word_to_bytes(state_in[0])
    s01, s11, s21, s31 = word_to_bytes(state_in[1])
    s02, s12, s22, s32 = word_to_bytes(state_in[2])
    s03, s13, s23, s33 = word_to_bytes(state_in[3])
    state_in[0] = s00 << 24 | s11 << 16 | s22 << 8 | s33
    state_in[1] = s01 << 24 | s12 << 16 | s23 << 8 | s30
    state_in[2] = s02 << 24 | s13 << 16 | s20 << 8 | s31
    state_in[3] = s03 << 24 | s10 << 16 | s21 << 8 | s32


def InvShiftRows(state_in):
    s00, s10, s20, s30 = word_to_bytes(state_in[0])
    s01, s11, s21, s31 = word_to_bytes(state_in[1])
    s02, s12, s22, s32 = word_to_bytes(state_in[2])
    s03, s13, s23, s33 = word_to_bytes(state_in[3])
    state_in[0] = s00 << 24 | s13 << 16 | s22 << 8 | s31
    state_in[1] = s01 << 24 | s10 << 16 | s23 << 8 | s32
    state_in[2] = s02 << 24 | s11 << 16 | s20 << 8 | s33
    state_in[3] = s03 << 24 | s12 << 16 | s21 << 8 | s30


def GMul(a, b):
    rv = 0
    while b > 0:
        if (b & 0x01) != 0:
            rv = rv ^ a
        hibit = (a & 0x80) != 0
        a = a << 1
        if hibit != 0:
            a = a ^ 0x1B
        b = b >> 1
    return rv & 0xFF


# 5.6
def MixColumns(state_in):
    a = [0, 0, 0, 0]
    for i in range(0, Nb):
        a[0], a[1], a[2], a[3] = word_to_bytes(state_in[i])
        r0 = GMul(0x02, a[0]) ^ GMul(0x03, a[1]) ^ GMul(0x01, a[2]) ^ GMul(0x01, a[3])
        r1 = GMul(0x01, a[0]) ^ GMul(0x02, a[1]) ^ GMul(0x03, a[2]) ^ GMul(0x01, a[3])
        r2 = GMul(0x01, a[0]) ^ GMul(0x01, a[1]) ^ GMul(0x02, a[2]) ^ GMul(0x03, a[3])
        r3 = GMul(0x03, a[0]) ^ GMul(0x01, a[1]) ^ GMul(0x01, a[2]) ^ GMul(0x02, a[3])
        state_in[i] = r0 << 24 | r1 << 16 | r2 << 8 | r3
    # print('  after MixColumns')
    # PrintState(state_in)


# 5.10
def InvMixColumns(state_in):
    a = [0, 0, 0, 0]
    for i in range(0, Nb):
        a[0], a[1], a[2], a[3] = word_to_bytes(state_in[i])
        r0 = GMul(0x0e, a[0]) ^ GMul(0x0b, a[1]) ^ GMul(0x0d, a[2]) ^ GMul(0x09, a[3])
        r1 = GMul(0x09, a[0]) ^ GMul(0x0e, a[1]) ^ GMul(0x0b, a[2]) ^ GMul(0x0d, a[3])
        r2 = GMul(0x0d, a[0]) ^ GMul(0x09, a[1]) ^ GMul(0x0e, a[2]) ^ GMul(0x0b, a[3])
        r3 = GMul(0x0b, a[0]) ^ GMul(0x0d, a[1]) ^ GMul(0x09, a[2]) ^ GMul(0x0e, a[3])
        state_in[i] = r0 << 24 | r1 << 16 | r2 << 8 | r3
    # print('  after MixColumns')
    # PrintState(state_in)


def PrintState(state_in):
    rv = b''
    for i in range(0, Nb):
        # print('{}'.format(hex(state_in[i])[2:].zfill(8)))
        rv += (state_in[i]).to_bytes(Nb, 'big')
    print('  {}'.format(binascii.b2a_hex(rv)))
    print('  {}'.format(rv))


#
# key expansion (Figure 11)
#
def KeyExpansion(aes_key):
    w = []
    i = 0
    while i < Nk:
        bytes_w = aes_key[(i*Nk):(i+1)*Nk]
        w.append(int.from_bytes(bytes_w, 'big'))
    #    print('{} - {}'.format(i, hex(w[i])))
        i = i + 1
    i = Nk
    while i < (Nb * (Nr + 1)):
        temp = w[i-1]
        if i % Nk == 0:
            temp = SubWord(RotWord(temp)) ^ (Rcon[i//Nk])
    #        print('  after rcon {}'.format(hex(temp)))
        elif Nk > 6 and (i % Nk) == 4:
            temp = SubWord(temp)
        w.append(w[i-Nk] ^ temp)
    #    print('{} - {}'.format(i, hex(w[i])))
        i = i + 1
    return w


#
# encrypt (Figure 5)
#
def Cipher(state, w):
    key_counter = 0

    # AddRoundKey
    for i in range(0, Nb):
        state[i] = state[i] ^ w[key_counter]
        key_counter += 1

    # print('end of round 1')
    # PrintState(state)
    # print('')

    for aes_round in range(1, Nr):
        SubBytes(state)
        ShiftRows(state)
        MixColumns(state)
        for i in range(0, Nb):
            state[i] = state[i] ^ w[key_counter]
            key_counter += 1
        # print('end of round {}'.format(aes_round + 1))
        # PrintState(state)
        # print('')

    SubBytes(state)
    ShiftRows(state)
    for i in range(0, Nb):
        state[i] = state[i] ^ w[key_counter]
        key_counter += 1

    # print('end of round {}'.format(Nr))
    # PrintState(state)
    # print('')

    return state


def encrypt(cipher_in, cipher_key):
    w = KeyExpansion(cipher_key)

    state = [0, 0, 0, 0]
    # state = in
    for i in range(0, Nb):
        state[i] = int.from_bytes(cipher_in[(i * Nb):(i + 1) * Nb], 'big')

    state = Cipher(state, w)

    rv = b''
    for i in range(0, Nb):
        rv += (state[i]).to_bytes(Nb, 'big')

    return rv


def encrypt_ecb(cipher_in, cipher_key):
    block = 0
    rv = b''
    state = [0, 0, 0, 0]
    w = KeyExpansion(cipher_key)

    for j in range(0, len(cipher_in)//AES_BLOCK):
        # state = in
        for i in range(0, Nb):
            state[i] = int.from_bytes(cipher_in[(block * Nb):(block + 1) * Nb], 'big')
            block += 1

        state = Cipher(state, w)

        for i in range(0, Nb):
            rv += (state[i]).to_bytes(Nb, 'big')

    return rv


def encrypt_cbc(cipher_in, cipher_key):
    block = 0
    rv = b''
    state = [0, 0, 0, 0]
    iv = [0, 0, 0, 0]
    w = KeyExpansion(cipher_key)

    for j in range(0, len(cipher_in)//AES_BLOCK):
        # state = in
        for i in range(0, Nb):
            state[i] = int.from_bytes(cipher_in[(block * Nb):(block + 1) * Nb], 'big')
            state[i] ^= iv[i]
            block += 1

        state = Cipher(state, w)

        for i in range(0, Nb):
            iv[i] = state[i]
            rv += (state[i]).to_bytes(Nb, 'big')

    return rv


#
# decrypt (Figure 12)
#
def InvCipher(state, w):
    key_counter = ((Nr + 1) * Nb) - 1

    # AddRoundKey
    for i in range(Nb - 1, -1, -1):
        state[i] = state[i] ^ w[key_counter]
        key_counter -= 1

    # print('end of round {}'.format(Nr))
    # PrintState(state)
    # print('')

    for aes_round in range(Nr - 1, 0, -1):
        InvShiftRows(state)
        InvSubBytes(state)
        for i in range(Nb - 1, -1, -1):
            state[i] = state[i] ^ w[key_counter]
            key_counter -= 1
        InvMixColumns(state)
        # print('end of round {}'.format(aes_round))
        # PrintState(state)
        # print('')

    InvSubBytes(state)
    InvShiftRows(state)
    for i in range(Nb - 1, -1, -1):
        state[i] = state[i] ^ w[key_counter]
        key_counter -= 1

    # print('end of round 1')
    # PrintState(state)
    # print('')

    return state


def decrypt(cipher_in, cipher_key):
    w = KeyExpansion(cipher_key)

    # state = in
    state = [0, 0, 0, 0]
    for i in range(0, Nb):
        state[i] = int.from_bytes(cipher_in[(i * Nb):(i + 1) * Nb], 'big')

    state = InvCipher(state, w)

    rv = b''
    for i in range(0, Nb):
        rv += (state[i]).to_bytes(Nb, 'big')

    return rv


def decrypt_ecb(cipher_in, cipher_key):
    block = 0
    rv = b''
    state = [0, 0, 0, 0]
    w = KeyExpansion(cipher_key)

    for j in range(0, len(cipher_in)//AES_BLOCK):
        # state = in
        for i in range(0, Nb):
            state[i] = int.from_bytes(cipher_in[(block * Nb):(block + 1) * Nb], 'big')
            block += 1

        state = InvCipher(state, w)

        for i in range(0, Nb):
            rv += (state[i]).to_bytes(Nb, 'big')

    return rv


def decrypt_cbc(cipher_in, cipher_key):
    block = 0
    rv = b''
    iv = [0, 0, 0, 0]
    state = [0, 0, 0, 0]
    state_copy = [0, 0, 0, 0]
    w = KeyExpansion(cipher_key)

    for j in range(0, len(cipher_in)//AES_BLOCK):
        # state = in
        for i in range(0, Nb):
            state[i] = int.from_bytes(cipher_in[(block * Nb):(block + 1) * Nb], 'big')
            state_copy[i] = state[i]
            block += 1

        state = InvCipher(state, w)

        for i in range(0, Nb):
            state[i] ^= iv[i]
            iv[i] = state_copy[i]
            rv += (state[i]).to_bytes(Nb, 'big')

    return rv
