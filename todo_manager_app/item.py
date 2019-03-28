#Item class

class Item(object):
    def __init__(self, record):
        self.id = record[0]
        self.completed = record[1]
        self.time = record[2]
        self.text = record[3]
