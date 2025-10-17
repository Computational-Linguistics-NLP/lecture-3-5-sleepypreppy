text = input()
if len(text) < 2:
    print("чудовищно мало")
elif len(text) < 5:
    print("очень мало")
elif len(text) < 10:
    print("мало")
elif len(text) < 30:
    print("ок")
elif len(text) < 100:
    print("много")
else:
    print("чудовищно много")
