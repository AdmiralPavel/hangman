import random


# Функция читает слова из файла и возвращает список
def get_words():
    with open('corpus.txt', 'r', encoding='utf-8') as words:
        corpus = words.read().split(',')
        return corpus


# Возвращает случайное слово из списка слов
def get_random_word():
    corpus = get_words()
    return random.choice(corpus)


# word - слово, загаданное компьютером
# letters - буквы, ещё не угаданные пользователем
# Возвращает слово, которое пользователь угадал на данный момент
def get_guessed_word(word, letters):
    answer = ''
    for letter in word:
        if letter not in letters:
            answer += letter
        else:
            answer += '_'
    return answer


letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
word = get_random_word()
print('Компьютер загадал слово, попробуйте отгадать его')
while '_' in get_guessed_word(word, letters):
    print("Введите букву из предложенного списка: " + ' '.join(letters))
    letter = input().lower()
    if letter in word:
        print(f'Вы угадали букву {letter}')
    else:
        print(f'Введённая буква была неверной.')
    letters.remove(letter)
    print(f'Отгаданные вами буквы: {get_guessed_word(word, letters)}')

print('Поздравляем, вы выиграли!')
