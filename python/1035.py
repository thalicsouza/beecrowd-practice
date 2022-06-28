# 1035 - Selection Test 1
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1035

abcd_list = input().split()
a = int(abcd_list[0])
b = int(abcd_list[1])
c = int(abcd_list[2])
d = int(abcd_list[3])

if b > c and d > a and c + d > a + b and c >= 0 and d >= 0 and a % 2 == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
       