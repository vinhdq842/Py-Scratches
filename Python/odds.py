def wordCount(s):
    tokens = s.split()
    words = list(dict.fromkeys(tokens))
    print(words)
    counts = [tokens.count(words[i]) for i in range(0, len(words))]
    return words, counts


text = "lúa nếp là lúa nếp làng lúa lên lớp lớp lòng nàng lâng lâng"
words, counts = wordCount(text)
for i in range(0, len(words)):
    print(words[i], ':', counts[i])



