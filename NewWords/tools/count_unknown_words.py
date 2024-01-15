from datetime import date

print("start count unknown words.")


# get file name. I need to learn new words at today.
today = date.today()

# new_file_name = today.strftime("%Y_%m_%d_new_words.txt")
new_file_name = today.strftime("user/%Y_%m_%d_new_words.txt")

# read new words during today
f = open(new_file_name)
total_str = f.read()
f.close()

new_words_today = total_str.lower().split("\n")

# get all unknown words
f = open("words_repo/unknown_words.txt")
total_str = f.read()
f.close()

all_unknown_words = total_str.split("\n")

# combine new words and old words
for word in all_unknown_words:
    _word = word.split(": ")[0]
    new_words_today.append(_word)

# get the order of words.
f = open("words_repo/word_times.txt")
word_order = f.read()
f.close()

# order all of the unknown words
result = []

vocabulary_array = word_order.split("\n")
for i in range(len(vocabulary_array)):
    word = vocabulary_array[i].split(",")[0]
    if word in new_words_today: 
        result.append(word + ": " + str(i+1))

# save unknown words
f = open("words_repo/unknown_words.txt", "w")
f.write("\n".join(result))
f.close()

print("end count material words.")
