print("start generate today's report.")

# get all unknown words
f = open("words_repo/unknown_words.txt")
total_str = f.read()
f.close()

unknown_words = total_str.split("\n")

# get all words of the material
f = open("words_repo/material_words.txt")
total_str = f.read()
f.close()

material_words = total_str.split("\n")

# count unknown words
unknown_words_1000 = 0
unknown_words_2000 = 0
unknown_words_3000 = 0
unknown_words_4000 = 0
unknown_words_5000 = 0
unknown_words_10000 = 0
unknown_words_20000 = 0
unknown_words_50000 = 0

for word in unknown_words:
    position = int(word.split(": ")[1])
    if position < 1000: unknown_words_1000 += 1
    elif position < 2000: unknown_words_2000 += 1
    elif position < 3000: unknown_words_3000 += 1
    elif position < 4000: unknown_words_4000 += 1
    elif position < 5000: unknown_words_5000 += 1
    elif position < 10000: unknown_words_10000 += 1
    elif position < 20000: unknown_words_20000 += 1
    elif position < 50000: unknown_words_50000 += 1

# count material words
material_words_1000 = 0
material_words_2000 = 0
material_words_3000 = 0
material_words_4000 = 0
material_words_5000 = 0
material_words_10000 = 0
material_words_20000 = 0
material_words_50000 = 0

for word in material_words:
    position = int(word.split(": ")[1])
    if position < 1000: material_words_1000 += 1
    elif position < 2000: material_words_2000 += 1
    elif position < 3000: material_words_3000 += 1
    elif position < 4000: material_words_4000 += 1
    elif position < 5000: material_words_5000 += 1
    elif position < 10000: material_words_10000 += 1
    elif position < 20000: material_words_20000 += 1
    elif position < 50000: material_words_50000 += 1


# generate today's report.
def generateLine(unknown_words_number, material_words_number, start, end):
    unknown_words_rate = unknown_words_number/material_words_number
    total_unknown_words = unknown_words_rate * (end - start)

    result = f"范围在{start}~{end}的单词，在您已接触过的{material_words_number}个单词中，有{unknown_words_number}个未掌握。\n所以测算在此范围，您大概还有{total_unknown_words:.0f}个未掌握，占比{unknown_words_rate:.0%}。\n"

    return result

result = []
result.append(generateLine(unknown_words_1000, material_words_1000, 0, 1000))
result.append(generateLine(unknown_words_2000, material_words_2000, 1000, 2000))
result.append(generateLine(unknown_words_3000, material_words_3000, 2000, 3000))
result.append(generateLine(unknown_words_4000, material_words_4000, 3000, 4000))
result.append(generateLine(unknown_words_5000, material_words_5000, 4000, 5000))
result.append(generateLine(unknown_words_10000, material_words_10000, 5000, 10000))
result.append(generateLine(unknown_words_20000, material_words_20000, 10000, 20000))
result.append(generateLine(unknown_words_50000, material_words_50000, 20000, 50000))

# save today's report
f = open("words_repo/today_report.txt", "w")
f.write("\n".join(result))
f.close()

print("end generate today's report.")


