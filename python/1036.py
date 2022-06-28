# 1036 -  Bhaskara's Formula
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1036

a,b,c = map(float,input().split())
delta = pow(b,2) - (4 * a * c)
raiz_delta = delta ** 0.5

if delta < 0 or a == 0:
    print("Impossivel calcular")
else:
    r1 = (-b + raiz_delta) / (2 * a)
    r2 = (-b - raiz_delta) / (2 * a)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))

