seconds = int(input("Введіть кількість секунд: "))

days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

if days % 10 == 1 and days % 100 != 11:
    day_word = "день"
elif 2 <= days % 10 <= 4 and (days % 100 < 10 or days % 100 >= 20):
    day_word = "дні"
else:
    day_word = "днів"

time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
result = f"{days} {day_word}, {time_str}"

print(result)