# TODO Напишите функцию для поиска индекса товара


def fnd_frst_inx(list_of_prod, product):
    if product not in list_of_prod:
        return None
    else:
        return list_of_prod.index(product)


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = fnd_frst_inx(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

