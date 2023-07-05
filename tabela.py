class Table:
    def __init__(self,sizemax):
        self.key = [None] * (sizemax + 1)
        self.valor = [None] * (sizemax + 1)
        self.li = 1
        self.ls = sizemax
        self.ini = self.li - 1
        self.end = self.ls + 1

    def is_empty(self):
        if self.ini != self.li - 1 and self.end != self.ls + 1:
            return False
        else:
            return True

    def is_full(self):
        if self.ini == self.li and self.end == self.ls:
            return True
        else:
            return False

    def size(self):
        if not self.is_empty():
            return self.end - (self.ini + 1)
        else:
            return 0

    def insert(self):
        pass

    def consult(self):
        pass

    def remove(self):
        pass

    def search(self, key):
        pass