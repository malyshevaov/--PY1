def get_count_char(str_):
    str_ = str_.lower()
    list_symbol = []
    slovar = {}
    DEFAULT_COUNT = 0
    for symbol in str_:
        if symbol.isalpha():
            list_symbol.append(symbol)
            slovar[symbol] = slovar.get(symbol, DEFAULT_COUNT) + 1
    return slovar
def get_count_char_percent(str_):
    str_ = str_.lower()
    list_symbol = []
    slovar_percent = {}
    DEFAULT_COUNT = 0
    for symbol in str_:
        if symbol.isalpha():
            list_symbol.append(symbol)
            slovar_percent[symbol] = round(((slovar_percent.get(symbol, DEFAULT_COUNT) + 1) * 100 / len(str_)),2)
    return slovar_percent
main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(get_count_char_percent(main_str))
