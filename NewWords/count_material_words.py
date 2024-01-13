from pprint import pprint

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
total_set = set(total_array)

print(len(total_array))
print(len(total_set))

#----------------------------------#
f = open("words_repo/word_times.txt")
word_times = f.read()
f.close()

result = []

vocabulary_array = word_times.split("\n")
for i in range(len(vocabulary_array)):
    word = vocabulary_array[i].split(",")[0]
    if word in total_set: 
        result.append(word + ": " + str(i+1))
        total_set.remove(word)

f = open("words_repo/material_words.txt", "w")
f.write("\n".join(result))
f.close()

pprint(result)
pprint(len(result))
pprint(total_set)
