class Table:
    def __init__(self,sizemax):
        self.key = [None] * (sizemax + 1)
        self.valor = [None] * (sizemax + 1)
        self.li = 1
        self.ls = sizemax
        self.ini = self.li - 1
        self.end = self.ls + 1

    def __repr__(self):
        string = ""
        if not self.is_empty():
            for i in range(self.ini,self.end + 1):
                string = string + str(self.key[i]) + ":" + str(self.valor[i]) + "\n"

        return string + "\n"

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

    def consult(self,key):
        if not self.is_empty():
            for i in range(self.ini,self.end + 1):
                if self.key[i] != key:
                    continue
                else:
                    return self.valor[i]
        else:
            return 0

    def insert(self):
        pass



    def remove(self):
        pass

    def search(self, key):
        pass