from random import choice, randint
def get_jokes(n, repeats=0):
    jokes = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for i in range(n):
        if repeats == 1:
            noun = randint(0, 4 - i)
            adv = randint(0, 4 - i)
            adj = randint(0, 4 - i)
            joke = nouns[noun] + " " + adverbs[adv] + " " + adjectives[adj]
            jokes.append(joke)
            nouns = nouns[:noun] + nouns[noun + 1:]
            adverbs = adverbs[:adv] + adverbs[adv + 1:]
            adjectives = adjectives[:adj] + adjectives[adj + 1:]
        else:
            jokes.append(choice(nouns) + " " +
                         choice(adverbs) + " " +
                         choice(adjectives))
    return jokes
"""get_jokes(n, repeats) generates jokes * n and return list of jokes
n - number of jokes
repeats - if repeats == 1: words in jokes aren't repeated and 0 < n < 6
          else: words in jokes can be repeated and 0 < n
"""
print(get_jokes(5, 1))
