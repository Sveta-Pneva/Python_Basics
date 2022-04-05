def num_translate(n):
    translation_dict = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
         "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    return translation_dict.get(n)

num_to_translate = input()
print(num_translate(num_to_translate))