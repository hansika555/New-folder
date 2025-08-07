word = input()
while word.lower() != "stop":
    if word.lower().endswith("ing") or word.lower().endswith("ed"):
        print(word)
    word = input()

    