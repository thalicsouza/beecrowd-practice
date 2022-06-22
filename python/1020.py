# 1020 - Age in Days
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1020

value = int(input())

years = int(value / 365)
print(f'{years} ano(s)')

months = int(value % 365 / 30) 
print(f'{int(months)} mes(es)')

days = value - (years * 365) - (months * 30)
print(f'{int(days)} dia(s)')