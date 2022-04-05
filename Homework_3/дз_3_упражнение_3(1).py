def thesaurus(*args):
    first_letters = []
    result = {}
    j = 0
    for i in args:
        if not i[0] in first_letters:
            first_letters.append(i[0])
            result[first_letters[j]] = [i]
            j += 1
        else:
            for g in first_letters:
                if g == i[0]:
                    result[g] = result.get(g) + [i]
    return  result

print(thesaurus("Иван", "Мария", "Петр", "Илья"))
