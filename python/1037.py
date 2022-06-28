# 1037 -  Interval
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1037

value = float(input())
int1,int2,int3,int4 = [0,25], [25,50], [50,75], [75,100]

if value < 0 or value > 100:
    print("Fora de intervalo")
elif value <= max(int1):
    print("Intervalo [0,25]")
elif value <= max(int2):
    print("Intervalo (25,50]")
elif value <= max(int3):
    print("Intervalo (50,75]")
elif value <= max(int4):
    print("Intervalo (75,100]")