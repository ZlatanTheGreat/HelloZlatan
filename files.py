def file():
    file = open("testfile.txt", "w+")

    for item in range(5):
        file.write("Lorem ipsum")

    file.close()

file()
