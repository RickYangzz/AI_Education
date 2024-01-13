f = open("words_repo/material.txt")
total_str = f.read()
f.close()

total_str = total_str.replace("\n"," ")
total_str = total_str.replace("——"," ")
total_str = total_str.replace("-"," ")
total_str = total_str.replace("\"","")
total_str = total_str.replace("!","")
total_str = total_str.replace("?","")
total_str = total_str.replace(",","")
total_str = total_str.replace(".","")
total_str = total_str.replace(":","")
total_str = total_str.replace(";","")
total_str = total_str.replace("\'s","")
total_str = total_str.replace("\'re","")
total_str = total_str.replace("\'m","")
total_str = total_str.replace("\'ll","")
total_str = total_str.replace("\'d","")
total_str = total_str.replace("\'ve","")
total_str = total_str.replace("\'","")
total_str = total_str.lower()
total_array = total_str.split(" ")

material_words_times = {}
for _word in total_array:
    if _word in material_words_times.keys():
        material_words_times[_word] += 1
    else:
        material_words_times[_word] = 1


f = open("words_repo/unknown_words.txt")
unknown_words = f.read()
f.close()

result = []
unknown_words_array = unknown_words.split("\n")
for _word in unknown_words_array:
    word = _word.split(": ")[0]
    if word in material_words_times.keys():
        result.append(f"{word}: {material_words_times[word]}")
    else:
        result.append(f"{word}: no-times")

f = open("words_repo/unknown_words_times.txt", "w")
f.write("\n".join(result))
f.close()