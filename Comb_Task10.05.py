from itertools import permutations


# генерирует перестановки букв слова и выводит в файл
def generate(word):
    # word: исходное слово

    with open("output5.txt", "w", encoding="utf-8") as file:

        # создаем множество, для слов, которые
        # будут повторятся
        processed = set()

        # генерация всех перестановок
        for words in permutations(word):
           word_unq = "".join(words)
           if word_unq not in processed:
               file.write(word_unq + "\n")
               processed.add(word_unq)
        print(f"Количество слов: {len(processed)}")


word = "ПРЕДОПРЕДЕЛЕННОСТЬ"
generate(word)