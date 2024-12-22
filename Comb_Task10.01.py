from itertools import permutations
from itertools import combinations
from collections import Counter

# Функция генерирует слова длины n,
# где ровно 2 буквы повторяются два раза
# и одна буква повторяется k раз,
# остальные буквы не повторяются.
# Полученные слова записываются в файл
def generate_words(alphabet, n, k):
    # alphabet: строка, которая содержит буквы алфавита
    # n: длина слов
    # k: число повторений одной буквы

    count = 0
    with open("output1.txt", "w") as file:

        # создаем множество, для слов, которые
        # будут повторятся
        processed = set()

        # используем 3 вложенных цикла для перебора индексов
        # символов для повторения
        for index1 in range(len(alphabet)):
            for index2 in range(index1, len(alphabet)):
                for index3 in range(len(alphabet)):
                    if index3 == index1 or index3 == index2:
                        continue

                    # определяем повторяющиеся символы
                    repeat1 = alphabet[index1]
                    repeat2 = alphabet[index2]
                    repeat3 = alphabet[index3]

                    # длина слова, которую должны заполнить остальные буквы
                    length = n - 2 - 2 - k
                    if length < 0:
                        continue

                    # генерируем комбинации из уникальных символов
                    others = [i for i in alphabet if i != repeat1 and i != repeat2 and i != repeat3]

                    # для каждой из комбинаций формируем список из символов,
                    # учитывая повторения
                    for others_tuple in combinations(others, length):
                        chars = [repeat1, repeat1, repeat2, repeat2, *([repeat3] * k), *others_tuple]

                        # формируем всевозможные перестановки
                        for word_tuple in permutations(chars):
                            word = "".join(word_tuple)

                            # проверка на то, что в полученном слове
                            # ровно 3 уникальные буквы
                            if len(Counter(word).keys()) == length + 3:
                                if word not in processed:
                                    count += 1
                                    file.write(word + "\n")
                                    processed.add(word)
        print(len(processed))


# Пример 1
alphabet = "abcdefghjk"
n = 9
k = 3
generate_words(alphabet, n, k)

# # Пример 2
# alphabet = "abcdefghjk"
# n = 7
# k = 2
# generate_words(alphabet, n, k)

# # Пример 3
# alphabet = "abcdefghjk"
# n = 6
# k = 1
# generate_words(alphabet, n, k)