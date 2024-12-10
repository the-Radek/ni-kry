with open("words.txt", "r") as f1, open("clean.txt", "w") as f2:
    for line in f1:
        word = line.strip()
        if len(word) > 4 and word.isalpha() and word.islower() and len(set(word)) > 2:
            f2.write(word + "\n")
