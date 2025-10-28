text = input("Введите текст: ")
length = len(text)
if length < 2:
    print("Чудовищно мало")
elif length >= 2 and length < 5:
    print("Очень мало")
elif length >= 5 and length < 10:
    print("Мало")
elif (length >= 10 and length < 30) or length == 10:
    print("Ок")
elif (length >= 30 and length < 100) or length == 30:
    print("Много")
elif length >= 100 or length > 99:
    print("Чудовищно много")
