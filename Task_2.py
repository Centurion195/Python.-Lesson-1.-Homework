# Найдите сумму цифр трехзначного числа.

a = int(input("Введите число: "))
sum = 0

while a>=1:
    sum += a%10;
    a=a//10

print(sum)