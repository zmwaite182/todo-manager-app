#Item class

class Item(object):
    def __init__(self, record):
        import datetime
        self.completed = record[1]
        self.time = record[2]
        self.text = record[3]
