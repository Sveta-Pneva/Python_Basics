def thesaurus(args):
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
    return result

def thesaurus_adv(*args):
    first_letters = []
    result = {}
    j = 0
    for i in args:
        surname = i.split()
        surname = surname[1]
        if not surname[0] in first_letters:
            first_letters.append(surname[0])
            result[first_letters[j]] = [i]
            j += 1
        else:
            for g in first_letters:
                if g == surname[0]:
                    result[g] = result.get(g) + [i]
    for i in first_letters:
        result[i] = thesaurus(tuple(result[i]))
    result = dict(sorted(result.items(), key=lambda x: x[0]))
    return result


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))