import numpy as np
import random


def find_alphabet_number(x):
    return ord(x)-97


def find_alphabet(num):
    return chr(97+num)

def matrix_multiply(A,B):
    return np.dot(A,B)


def generate_matrix(block_size):
    l=[x for x in range(0,26)]
    matrix=[]
    for x in range(block_size):
        temp=[]
        for y in range(block_size):
            temp.append(random.choice(l))
        matrix.append(temp)
    return np.array(matrix)

def encrypt(string,block_size):
    n=len(string)
    block_size=min(n,block_size)
    print(block_size)
    string=list(string)
    string=[find_alphabet_number(x) for x in string]
    matrix=generate_matrix(block_size)
    s=[]
    for x in range(0,n,block_size):
        s.append(string[x:x+block_size])
    if len(s[-1])!=block_size:
        while len(s[-1])!=block_size:
            s[-1].append(25)
    print(s)
    encrypted=""
    for block in s:
        print(block)
        block=np.array(block).reshape(block_size,1)
        temp=matrix_multiply(matrix,block)%26
        for i in range(len(temp)):
            encrypted+=find_alphabet(temp[i])
    return encrypted,matrix


def decrypt(string,matrix):
    block_size=matrix.shape[0]
    n=len(string)
    string=list(string)
    string=[find_alphabet_number(x) for x in string]
    s=[]
    for x in range(0,n,block_size):
        s.append(string[x:x+block_size])
    if len(s[-1])!=block_size:
        while len(s[-1])!=block_size:
            s[-1].append(25)
    print("Initial Matrix=",matrix)
    det=np.round(np.linalg.det(matrix))
    print("Determinant= ",det)
    key=-1
    for x in range(0,26):
        if (x*det)%26==1:
            key=x
    print(matrix)
    print("Key= ",key)
    #matrix=np.round(np.linalg.inv(matrix)*det)
    adjugate=np.matrix.getH(matrix)
    print("Adjugate= ",adjugate)
    matrix=(adjugate*key)%26
    matrix=matrix%26
    print("Inverted matrix= ",matrix)
    decrypted=""
    for block in s:
        block=np.array(block).reshape(block_size,1)
        temp=matrix_multiply(matrix,block)%26
        for i in range(len(temp)):
            decrypted+=find_alphabet(temp[i])
    return decrypted

i=input("Enter any string: ")
block_size=int(input("Enter the Blocksize "))
encrypted,matrix=encrypt(i,block_size)
decrypted=decrypt(encrypted,matrix)
print(encrypted)
print(matrix)
print(decrypted)
