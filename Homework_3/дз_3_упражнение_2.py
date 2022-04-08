def num_translate_adv(n):
    translation_dict = {"zero": "ноль", "one": "один", "two": "два", "tree": "три", "four": "четыре", "five": "пять",
         "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}
    if n.istitle():
        return translation_dict.get(n.lower()).capitalize()
    else:
        return translation_dict.get(n)

num_to_translate = input()
print(num_translate_adv(num_to_translate))