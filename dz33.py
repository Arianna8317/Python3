#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в
#  рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные 
# варианты комплектации рюкзака. 

equipment = {"палатка": 3.5,"спальник": 1.8,"пенка": 0.45, "вода": 1.5, "фонарь": 0.5,  "нож": 0.3,"продукты": 5,"одежда": 4, \
            "средства гигиены": 0.5, "котелок": 0.2, "посуда": 0.8, "топор": 1.2, "веревка": 0.5, "тент": 0.8, "обувь": 2}
backpack_size = int(input("Введите вместимость рюкзака: "))
combinations = []

def backpack(equipment: dict[str:int], size: int) -> list[list[str]]:
    items, weight = zip(*sorted(equipment.items(), key=lambda x: x[1], reverse=True))
    collection, weight_counter = [], 0
   
    for item_index, item_weight in enumerate(weight, 0):
        weight_counter += item_weight
        if weight_counter < size:
            collection.append((items[item_index]))
    return collection

def backpack_unsorted(equipment: dict[str:int], size: int) -> list[list[str]]:
    weight = list(equipment.values())
    items = list(equipment.keys())
    collection, weight_counter = [], 0
   
    for item_index, item_weight in enumerate(weight, 0):
        if item_weight < size:
            weight_counter += item_weight
            if weight_counter < size:
                collection.append((items[item_index]))
    return collection


print(f"В рюкзак можно положить : {backpack(equipment, backpack_size)} ")
print(f"В рюкзак можно положить : {backpack_unsorted(equipment, backpack_size)}")