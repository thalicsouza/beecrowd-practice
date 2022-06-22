# 1019 - Time Conversion
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1019

value = int(input())
seg = value % 60
min = (value - seg) / 60 % 60
hour = (value - seg) / 60 / 60 
print(f'{int(hour)}:{int(min)}:{seg}')