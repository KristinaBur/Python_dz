# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 


number = input("Введите трехзначное число: ")
number = int(number)
 
a = number % 10
b = number % 100 // 10
c = number // 100
 
print("Сумма цифр числа:", a + b + c)
