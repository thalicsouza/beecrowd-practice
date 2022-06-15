# 1010 - Simple Calculate
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1010

p1 = input().split()
p2 = input().split()
result1 = (int(p1[1])) * float(p1[2])
result2 = (int(p2[1])) * float(p2[2])
print("VALOR A PAGAR: R$ {:.2f}".format(result1 + result2))