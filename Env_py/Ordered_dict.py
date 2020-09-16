"""
Módulo Colletions: Ordered Dict

Em um dicionário comum a ordem pouco importa, o que importa é o que há
dentro do dicionário.
"""
# Veja que pro Python não importa a ordem dos itens alocados

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
if dict1 == dict2:
    print(f'Para o Python, não importa a ordem,'
          f' importa é que existem ali os mesmo itens.\n'
          f'Dic1={dict1}\nDic2={dict2}\n'
          f'Pro Python Dic1 == Dic2? {dict1 == dict1}\n')

from collections import OrderedDict
odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

if odict1 != odict2:
    print(f'No "OrderedDict" será levado em consideração'
          f' tanto os itens quanto a ordem\n'
          f'ODic1= {odict1}\nODic2= {odict2}\n'
          f'Pro Python ODic1 == ODic2? {odict1 == odict2}\n')