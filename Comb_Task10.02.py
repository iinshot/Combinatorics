from itertools import permutations
from itertools import combinations
from collections import Counter


# функция для проверки уникальности
# некоторого количества символов
def is_valid(word, count_char):
    # word: слово для проверки
    # count_char: количество символов

    if len(Counter(word).keys()) == count_char:
        return len(Counter(word).keys())


# функция генерирует комбинации символов с повторениями
def generate_comb(alphabet, k):
    # alphabet: строка, которая содержит буквы алфавита
    # k: число повторений одной буквы

    # используем 3 вложенных цикла для перебора индексов
    # символов для повторения
    for index1 in range(len(alphabet)):
        for index2 in range(len(alphabet)):
            if index1 == index2:
                continue
            for index3 in range(len(alphabet)):
                if index1 == index3 or index2 == index3:
                    continue

                # определяем повторяющиеся символы
                repeat1 = alphabet[index1]
                repeat2 = alphabet[index2]
                repeat3 = alphabet[index3]

                # генерация комбинаций
                for count1 in range(k + 1):
                    yield repeat1, count1, repeat2, k + 1, repeat3


# Функиция генерирует все слова из
# комбинаций слов и записывает в файл
def generate_words(alphabet, n, k, comb):
    # alphabet: строка, которая содержит буквы алфавита
    # n: длина слов
    # k: число повторений одной буквы
    # comb: комбинации символов с повторениями

    count = 0
    with open("output2.txt", "w") as file:

        # создаем множество, для слов, которые
        # будут повторятся
        processed = set()

        for repeat1, count1, repeat2, count2, repeat3 in comb:

            # перебор количества повторений 3-го символа
            for count3 in [k + 2, k + 3]:
                length = n - count1 - count2 - count3
                if length < 0:
                    continue

                # генерируем комбинации из уникальных символов
                others = [i for i in alphabet if i != repeat1 and i != repeat2 and i != repeat3]

                # для каждой из комбинаций формируем список из символов,
                # учитывая повторения
                for others_tuple in combinations(others, length):
                    chars = [*([repeat1] * count1), *([repeat2] * (k + 1)),  *([repeat3] * count3), *others_tuple]

                    # формируем всевозможные перестановки
                    for word_tuple in permutations(chars):
                        word = "".join(word_tuple)

                        # проверка на уникальность
                        if word not in processed:
                            if is_valid(word, length + 3):
                                count += 1
                                file.write(word + "\n")
                                processed.add(word)
    print(count)


def generate(alphabet, n, k):
    # alphabet: строка, которая содержит буквы алфавита
    # n: длина слов
    # k: число повторений одной буквы

    combs = generate_comb(alphabet, k)
    generate_words(alphabet, n, k, combs)


# # Пример 1
# alphabet = "abcdefghjk"
# n = 7
# k = 3
# generate(alphabet, n, k)

# # Пример 2
# alphabet = "abcdefghjk"
# n = 8
# k = 2
# generate(alphabet, n, k)

# Пример 3
alphabet = "abcdefghjk"
n = 6
k = 1
generate(alphabet, n, k)