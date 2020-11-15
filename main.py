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


# Функция проверяет корректность ввода пользователя
def check_input():
    while True:
        letter = input().lower()
        if len(letter) != 1:
            print('Ошибка! Длина введённой строки не равна 1.')
        elif letter not in letters:
            print(f"Ошибка! Введите букву из предложенного списка: {' '.join(letters)}")
        else:
            break
    return letter


letters = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
word = get_random_word()
lifes = 7
print('Компьютер загадал слово, попробуйте отгадать его')
while '_' in get_guessed_word(word, letters) and lifes != 0:
    print(f"Введите букву из предложенного списка: {' '.join(letters)}")
    letter = check_input()
    if letter in word:
        print(f'Вы угадали букву {letter}')
    else:
        print(f'Введённая буква была неверной. Количество ваших жизней: {lifes}')
        lifes -= 1
    letters.remove(letter)
    print(f'Отгаданные вами буквы: {get_guessed_word(word, letters)}')

if lifes == 0:
    print(f'Вы проиграли! Загаданным словом было {word}')
else:
    print('Поздравляем, вы выиграли!')
