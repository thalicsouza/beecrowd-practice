# 1038 -  Snack
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1038

code,qty = map(int,input().split())
items_dict = {1:4,2:4.5,3:5,4:2,5:1.5}
value = ()

for k,v in items_dict.items():
    if code == k:
        value = v * qty
print("Total: R$ {:.2f}".format(float(value)))     