# 1012 - Area
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1012

x = input().split()
a = float(x[0])
b = float(x[1])
c = float(x[2])
pi = 3.14159 
print("TRIANGULO: {:.3f}".format(a*c/2))
print("CIRCULO: {:.3f}".format(pi*c**2))
print("TRAPEZIO: {:.3f}".format((a+b)*c/2))
print("QUADRADO: {:.3f}".format(b**2))
print("RETANGULO: {:.3f}".format(a*b))