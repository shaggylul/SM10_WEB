from operator import itemgetter


class OS:
    """Операционная система"""
    def __init__(self, id, name, price, comp_id):
        self.id = id
        self.name = name
        self.price = price
        self.comp_id = comp_id


class Comp:
    """Компьютер"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Отделы
comps = [
    Comp(1, 'Витя'),
    Comp(2, 'Прохор'),
    Comp(3, 'Ринат'),
]


# Сотрудники
os = [
    OS(1, 'Windows95', 1, 2),
    OS(2, 'Windows10', 20, 1),
    OS(3, 'Windows11', 200, 3),
    OS(4, 'macOS', 300, 3),
    OS(5, 'Linux', 0, 3),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим 
    one_to_many = [(o.name, o.price, c.name) 
        for o in os 
        for c in comps 
        if o.comp_id==c.id]
    
    print('Задание 1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)
    
    print('\nЗадание 2')
    res_12_unsorted = []
    # Перебираем все компьютеры
    for c in comps:
        # Список операционных систем компьютера
        c_os = list(filter(lambda i: i[2]==c.name, one_to_many))
        # Если у компьтера есть ОС        
        if len(c_os) > 0:
            # Цены операционных систем
            c_prices = [price for _,price,_ in c_os]
            # Суммарная цена операционных систем на одном компьютере
            c_prices_sum = sum(c_prices)
            res_12_unsorted.append((c.name, c_prices_sum))


    # Сортировка по суммарной цене
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


if __name__ == '__main__':
    main()
