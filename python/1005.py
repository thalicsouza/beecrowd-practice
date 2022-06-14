# 1005 - Average 1
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1005

media_a = float(3.5)
media_b = float(7.5)
a = float(input())
b = float(input())
result_a = a * media_a
result_b = b * media_b
result = (result_a + result_b) / (media_a + media_b)
print("MEDIA = {:.5f}".format(round(result, 5)))
