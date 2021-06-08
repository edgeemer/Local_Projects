"""
Кол-во команд из 5 человек из выборки в 8 мальчиков и 3 девочки (1 девочка обязательно)
"""

from itertools import combinations

print("All possible variants: ", end="")
variants = [i for i in combinations(["M1", "M2", "M3", "M4", "M5", "M6", "M7", "M8", "M9", "G1", "G2", "G3"], 5)]
print(len(variants))

print("Variants with all requirements [girls in range (1,4)]: ", end="")
girls_check_list = []
for index_variant in range(0, len(variants)):
    counter = 0
    for element in variants[index_variant]:
        if element in ["G1", "G2", "G3"]:
            counter += 1
    if 0 < counter <= 3:
        girls_check_list.append(variants[index_variant])
print(len(girls_check_list))
