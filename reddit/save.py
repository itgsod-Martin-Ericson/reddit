class Save(object):
    def __init__(self, data):
        self.data = data

    def save_image(self):
        file = open("images.txt", "r+")

        for s in file.readlines():
            if s == self.data + "\n" or self.data == "This is not an imgur image.":
                file.close()
                return "Image already saved."

        file.write(self.data + "\n")

        file.close()