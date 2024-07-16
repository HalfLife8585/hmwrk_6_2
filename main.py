seconds = int(input("Введіть кількість секунд: "))

days, remainder = divmod(seconds, 86400)
hours, remainder = divmod(remainder, 3600)
minutes, seconds = divmod(remainder, 60)

if days == 1:
    day_word = "день"
elif 1 < days < 5:
    day_word = "дні"
else:
    day_word = "днів"

time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
result = f"{days} {day_word}, {time_str}"

print(result)