#4.	Считать с клавиатуры непустую произвольную последовательность целых чисел. Найти:
#i.	Сумму всех чисел последовательности (решить задачу используя циклическую конструкцию while)
#ii.	Количество всех чисел последовательности (решить задачу используя циклическую конструкцию while)
x = 0
y = 0
while True:
    n = int(input())
    if n == 0:
        break
    x += n
    y += 1
print(x, y)