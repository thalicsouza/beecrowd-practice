# 1009 - Salary with Bonus
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1009

func_name = str(input())
m_salary = float(input())
total_sales = float(input())
total_salary = (total_sales * 0.15) + m_salary
print("TOTAL = R$ {:.2f}".format(total_salary))