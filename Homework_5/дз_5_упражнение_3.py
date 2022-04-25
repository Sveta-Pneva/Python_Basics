tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей',
          'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
def gen_lists():
    i = 0
    while i != len(tutors):
        if len(tutors) > len(klasses):
            klasses.append(None)
            yield tutors[i], klasses[i]
        else:
            yield tutors[i], klasses[i]
        i += 1
a = gen_lists()
while True:
    try:
        print(next(a))
    except:
        break