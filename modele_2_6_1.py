def single_root_words(root_word, *other_words):
    same_words=[]
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)

#второй вариант с вводом от пользователя

def single_root_words_2(root_word, *other_words):
    same_words=[]
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words

root_word = input("Введите корневое слово: ")

while True:
    other_words = input("Введите несколько слов через пробел (минимум два слова): ").split()
    if len(other_words)>= 2:
        break
    else:
        print("Слов должно быть от двух и больше.")

result = single_root_words_2(root_word, *other_words)
print(result)

