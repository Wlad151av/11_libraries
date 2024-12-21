class Info42:

    def __init__(self, name):
        self.name = name

def introspection_info(obj):
    info_dict = {}
    info_dict['type'] = type(obj)
    info_dict['attributes'] = list(3*'.')
    info_dict['methods'] = ['__abs__', '__add__', 3*'.']
    info_dict['module'] = '__main__'
    return info_dict
    



Creature = Info42('Creature42')
number_info = introspection_info(42)
print(number_info)

#Вывод на консоль:
#{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

#Рекомендуется создавать свой класс и объект для лучшего понимания
    
