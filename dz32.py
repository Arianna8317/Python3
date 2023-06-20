""" В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
 Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из 
 документации к языку. """
import re


def text_processor(text, max_number):
    text = text.lower()
    text = re.sub(r'[.,"\'-?:!;]', '', text)
    words = text.split()  # текст на слова
    word_counts = {}  # словарь для хранения количества вхождений каждого слова
    word_counter = 0
    for word in words:
        if word not in word_counts:
            word_counts[word] = 1     # Считаем количество вхождений каждого слова
        else:
            word_counts[word] += 1
        word_counter += 1    
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse = True) 
    # return_dict = {}
    # Сортируем словарь по значению в порядке убывания
    
    return (sorted_word_counts[0:max_number:1] , word_counter)    

my_text = '''Во́лга  — река в европейской части России \ 
Одна из крупнейших рек на Земле и самая большая по водности, площади бассейна и длине в Европе, \
а также крупнейшая в мире река, впадающая в бессточный (внутренний) водоём . В нижнем течении после впадения Камы Волга получает \
доволно мало речного стока . \
Она протекает здесь вдоль Приволжской возвышенности.  Около Тольятти выше Самарской Луки  \
которую образует Волга, огибая Жигулёвские горы, сооружена плотина Жигулёвской ГЭС;  \
выше плотины простирается Куйбышевское водохранилище.  \
На Волге в районе города Балаково возведена плотина Саратовской ГЭС. \
Выше плотины находится Саратовское водохранилище. Нижняя Волга принимает сравнительно небольшие притоки \
Сок, Самару, Большой Иргиз, Еруслан. В Волгограде, в районе Волжской ГЭС от Волги отделяется левый рукав \
— Ахтуба (длина 537 км), которая течёт параллельно основному руслу. \
Обширное пространство между Волгой и Ахтубой, пересечённое многочисленными протоками и староречьями, \
называется Волго-Ахтубинской поймой; ширина разливов в пределах этой поймы достигала прежде 20—30 км. \
На Волге между началом Ахтубы и Волгоградом построена Волжская ГЭС;  \
выше плотины простирается Волгоградское водохранилище. В сорока километрах ниже плотины к Волге \
gримыкает Волго-Донской канал, связывающий её с Цимлянским водохранилищем Дона. '''

print(text_processor(my_text, 10))