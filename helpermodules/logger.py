class log:
    def __init(self, name="log"):
        self.file = open("log.txt", "w")

    def write(self, text):
        print(text)
        self.file.write(text)
        self.file.write("\n")

    def close(self):
        self.file.close()


