import os
from pprint import pprint

#ЗАДАЧА 1

cook_book = {}
keys = []
sustain_list = ['ingredients_name', 'count', 'measure']
print()


with open('recipes.txt', 'r', encoding = 'utf-8') as file:
  for line in file:
    keys += [line.strip()]
    num = int(file.readline().strip())
    variables = []
    cook_book[line.strip()] = variables
    for i in range(num):
      elem = file.readline().strip().split(' | ')
      variables.append(dict(zip(sustain_list, elem)))
    file.readline()

#pprint(cook_book, sort_dicts=False)


#ЗАДАЧА 2

dish = ['Запеченный картофель', 'Омлет', 'Фахитос']
persons = 2

def get_shop_list_by_dishes(dishes, person_count):
  sustain_list = ['ingredients_name', 'count', 'measure']
  if set(dishes) & set(keys) == set(dishes):
    list_dishes = []
    list_measure = []
    list_quantity = []
    measure_dict = []
    quantity_dict = []
  # Разбиваем данные в первые 3 списка
    for i in dishes:
      for raw in cook_book[i]:
        if raw['ingredients_name'] in list_dishes:
          item = list_dishes.index(raw['ingredients_name'])
          list_quantity[item] += int(raw['count']) * person_count
        else:
          list_dishes.append(raw['ingredients_name'])
          list_measure.append(raw['measure'])
          list_quantity.append(int(raw['count']) * person_count)

  # Добавляем данные в доп списки по форме вывода
    for ii in list_measure:
      measure_dict.append(dict.fromkeys(['measure'], ii))
    for iii in list_quantity:
      quantity_dict.append(dict.fromkeys(['quantity'], iii))

    dictgo_list = {}
  # Добавляем финальный словарь
    for fig in range(len(list_dishes)):
      measure_dict[fig]['quantity'] = quantity_dict[fig]['quantity']
    for fig in range(len(list_dishes)):
      dictgo_list[list_dishes[fig]] = measure_dict[fig]
    pprint(dictgo_list)

  else:
    print('Проверьте вводные данные')

#get_shop_list_by_dishes(dish, persons)


# Задача 3
mylist = ['1.txt', '2.txt', '3.txt']

def get_result_file(list_import):

  file_export = 'result.txt'
  file_export_path = os.path.join(os.getcwd(), 'sorted', file_export)

  list_full_path = []
  dict_all = {}

  for i in list_import:
    list_full_path.append(os.path.join(os.getcwd(), 'sorted', i))

  for i in list_full_path:
    count_file = 0
    with open(i, 'r', encoding = 'utf-8') as first:
      for line in first:
        count_file += 1
    with open(i, 'r', encoding = 'utf-8') as first:
      list_text = str(count_file) + '\n' + first.read()
      count_file = 0
    dict_all[list_text] = i

  with open(file_export_path, 'w', encoding='utf-8') as exp:
    exp.write(f'')
    for text, path in sorted(dict_all.items()):
      exp.write(f'{os.path.basename(path)}\n')
      exp.write(f'{text}\n')
      exp.write(f'\n')

#get_result_file(mylist)