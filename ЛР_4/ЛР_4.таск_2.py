def get_count_char(str_):
    str_ = " ".join(main_str.split())
    str_ = str_.lower()
    list_new = sorted(str_)
    list_simbol = []
    slovar = {}
    DEFAULT_COUNT = 0
    for simbol in list_new:
        if simbol.isalpha():
            list_simbol.append(simbol)
    for letter in list_simbol:
        slovar[letter] = slovar.get(letter, DEFAULT_COUNT) + 1
    return slovar
def get_count_char_percent(str_):
    str_ = " ".join(main_str.split())
    str_ = str_.lower()
    list_new = sorted(str_)
    list_simbol = []
    slovar_percent = {}
    DEFAULT_COUNT = 0
    for simbol in list_new:
        if simbol.isalpha():
            list_simbol.append(simbol)
    for letter in list_simbol:
        slovar_percent[letter] = round(((slovar_percent.get(letter, DEFAULT_COUNT) + 1) * 100 / len(str_)),2)
    return slovar_percent
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_count_char_percent(main_str))
