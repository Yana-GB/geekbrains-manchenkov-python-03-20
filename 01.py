# Задание 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные,
# выведите на экран.

my_name = "Яна"
my_hobby = "рисование"
print(f"Привет! Меня зовут {my_name} и я хочу немного узнать о тебе")

name = input("Как тебя зовут?...")
age = int(input("Сколько тебе лет?..."))
hobby = input("Какое у тебя хобби?...")

print(f"Приятно познакомиться, {name}! "
      f"Теперь я знаю, что тебе {age} лет "
      f"и твое увлечение - {hobby}, а я люблю {my_hobby}!")
