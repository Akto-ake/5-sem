import timeit

# создаём объект Timer
t = timeit.Timer("sum(range(100))")
num, total_time = t.autorange()

print(f"Количество повторов: {num}")
print(f"Общее время: {total_time} секунд")
print(f"Среднее время одного запуска: {total_time / num} секунд")
