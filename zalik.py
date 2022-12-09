print("Введіть довільне трьох значне число ***")
a = open("file.txt", "r")
list = a.read().split("\n")

b = int(input())
if (b < 99 or b > 1000):
    print("Не коректне число, прочитайте умову ще раз ")
else:
    for line in list:
        parts = line.split(" ")
        if (int(parts[1]) > b):
            print(line)