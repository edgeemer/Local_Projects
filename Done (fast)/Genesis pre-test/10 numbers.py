"""
Минимальное значение из всех максимальных сумм 3х случайных чисел выборки из 10 чисел
"""

import itertools

print("All variants: ", end="")
all_variants_raw = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(f"{len(all_variants_raw)}")
print("Variants sum calculating and sorting: ", end="")


def variants_max_sum(variants):
    all_variants_sums = []
    for variant in variants:
        sum_list = []
        for index in range(0, len(variant)):
            if index + 2 >= len(variant):
                sum_list.append(variant[index] + variant[index + 1 - len(variant)]
                                + variant[index + 2 - len(variant)])
            else:
                sum_list.append(variant[index] + variant[index + 1] + variant[index + 2])
        sum_list.sort(reverse=True)
        all_variants_sums.append(sum_list[0])
    return all_variants_sums


all_var_best_sums = variants_max_sum(all_variants_raw)
print(f"done\n")

final = sorted(zip(all_var_best_sums, all_variants_raw), key=lambda x: x[0], reverse=False)
best_result = final[0][0]
counter = 0
for pair in final:
    if pair[0] == best_result:
        print(f"Score: {pair[0]} and sequence: {pair[1]}")
        counter += 1
    else:
        print(f"Score: {pair[0]} and sequence: {pair[1]}\n")
        print(f"Total variants with top score: {counter}")
        break
