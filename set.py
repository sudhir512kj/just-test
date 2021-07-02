class Set:
    def __init__(self):
        self.set = []

    def add(self, e):
        if e not in self.set:
            self.set.append(e)

    def delete(self, e):
        index = self.set.index(e)
        if index != -1:
            self.set.pop(index)