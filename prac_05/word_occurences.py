words = {}

text_raw = input("Text: ")
text_array = text_raw.split(" ")
for word in text_array:
    try:
        words[word] += 1
    except KeyError:
        words[word] = 1
if '' in words:
    words.pop('')

for word in sorted(words.keys()):
    max_length = max([len(word) for word in words])
    print(f"{word:{max_length}} : {words[word]}")