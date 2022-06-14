# 1006 - Average 2
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1006

peso_a = float(2)
peso_b = float(3)
peso_c = float(5)
nota_a = float(input())
nota_b = float(input())
nota_c = float(input())
media_ponderada = ((nota_a * peso_a) + (nota_b * peso_b) + (nota_c * peso_c)) / (peso_a + peso_b + peso_c)
print("MEDIA = {:.1f}".format(media_ponderada))
