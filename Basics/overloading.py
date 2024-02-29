#operator overloading

print(100 + 200)  #Add numbers

print('Jess' + 'Roy') #concatenate strings

print([10, 20, 30] + ['jessa', 'emma', 'kelly'])  #merge two lists


#method overloading

def addition(a, b):
    c = a + b
    print(c)


def addition(a, b, c):
    d = a + b + c
    print(d)

# addition(4, 5)
addition(3, 7, 5)