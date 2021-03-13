def read_given():
    with open("temp.txt", "r") as file:
        return file.read()


def set_given(num):
    file = open("temp.txt", "w")
    file.write(num)
    file.close()
