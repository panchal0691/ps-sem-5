def checkMagazine(magazine, note):
    for word in note:
        try:
            magazine.remove(word)
        except:
            print("No")
            return
    print("Yes")
