#Item class

class Item(object):
    def __init__(self, text):
        import datetime
        self.completed = False
        self.time = datetime.datetime.now().strftime("%m-%d")
        self.text = text
