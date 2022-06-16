# 1015 - Distance
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1015

x = input().split()
y = input().split()
x_1 = (float(y[0]) - float(x[0])) **2
y_1 = (float(y[1]) - float(x[1])) **2
distance = (x_1 + y_1) ** (0.5)
print("{:.4f}".format(distance))