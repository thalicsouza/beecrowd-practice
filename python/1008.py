# 1008 - Salary
# original link: https://www.beecrowd.com.br/judge/en/problems/view/1008

func_number = int(input())
w_hours = int(input())
hourly_salary = float(input())
total_salary = w_hours * hourly_salary
print(f"NUMBER = {func_number}")
print("SALARY = U$ {:.2f}".format(total_salary))