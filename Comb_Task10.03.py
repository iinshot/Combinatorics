from itertools import product
from itertools import combinations
from collections import Counter


# функция для проверки уникальности
# некоторого количества символов
def is_valid(word, count_char):
    # word: слово для проверки
    # count_char: количество символов

    return len(Counter(word).keys()) == count_char


# функция генерирует все слова длины n,
# включающее k уникальных букв
def generate_words(alphabet, n, unique):
    # alphabet: строка, которая содержит буквы алфавита
    # n: длина слов
    # unique: количество уникальных слов

    count = 0
    with open("output3.txt", "w") as file:

        # выбираем комбинации уникальных букв
        for unq in combinations(alphabet, unique):

            # создаем всевозможные комбинации длины n
            for words in product(unq, repeat=n):
                word = "".join(words)

                # проверка на уникальность
                if is_valid(word, unique):
                    file.write(word + "\n")
                    count += 1
    print(f'Количество слов: {count}')


alphabet = "abcdefghjk"
n = 10
unique_sym = 4
generate_words(alphabet, n, unique_sym)