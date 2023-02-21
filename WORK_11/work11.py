# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# Input: 5
# Output: 6 

n = int(input())

prev_num = 0
current_num = 1
temp = None
count = 0
while current_num <= n:
    temp = prev_num
    prev_num = current_num + prev_num
    current_num = temp
    count += 1
    if n == current_num:
        print(count)
        break
else:
    print ("Число не является числом Фибонначи")
