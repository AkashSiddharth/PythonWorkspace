'''
Problem: For this challenge, you are given two complex numbers, and you have to print the result of their addition, subtraction, 
        multiplication, division and modulus operations. The real and imaginary precision part should be correct up to two decimal places.

    Input Format: One line of input: The real and imaginary part of a number separated by a space.

    Output Format: For two complex numbers C and D, the output should be in the following sequence on separate lines:
        -> C + D
        -> C - D
        -> C * D
        -> C / D
        ->  mod(C)
        ->  mod(D)
    For complex numbers with non-zero real(A) and complex part(B), the output should be in the following format: A + Bi. Replace the plus 
    symbol with a minus symbol when B < 0. 
    For complex numbers with a zero complex part i.e. real numbers, the output should be: A + 0.00i
    For complex numbers where the real part is zero and the complex part is non-zero, the output should be: 0.00 + Bi
'''
''' Complex object approach
a = list(map(float, input().split()))
b = list(map(float, input().split()))

print (a, b)
comA, comB = complex(*a), complex(*b)

print(*map(str, [comA + comB, comA - comB, comA * comB, comA/comB, abs(comA), abs(comB)]), sep='\n')
'''

class Complex(complex):
    '''def __init__(self, real, imaginary):
        self.comp = complex(real, imaginary)
        print(self.comp.real, self.comp.imag)'''

    def __add__(self, no):
        #return self.comp + no.comp
        return ('{0.real:04.2f}{0.imag:+04.2f}i'.format(complex.__add__(self, no)))

    def __sub__(self, no):
        return ('{0.real:04.2f}{0.imag:+04.2f}i'.format(complex.__sub__(self, no)))

    def __mul__(self, no):
        return ('{0.real:04.2f}{0.imag:+04.2f}i'.format(complex.__mul__(self, no)))

    def __truediv__(self, no):
        return ('{0.real:04.2f}{0.imag:+04.2f}i'.format(complex.__truediv__(self, no)+0))

    def mod(self):
        return ('{0.real:04.2f}{0.imag:+04.2f}i'.format(complex(complex.__abs__(self), 0)))

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(complex(*c))
    y = Complex(complex(*d))
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')