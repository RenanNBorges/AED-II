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
                string = string + str(self.key[i]) + " : " + str(self.valor[i]) + "\n"

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

    def linear_search(self, key):
        if not self.is_empty():
            for i in range(self.ini,self.end + 1):
                if self.key[i] == key:
                    return i
        return 0

    def insert(self, key, valor):
        index = self.linear_search(key)
        if index < 0:
            self.valor[index] = valor
        elif not self.is_full():
            if self.is_empty():
                self.ini = self.li
                self.end = self.ini
            else:
                self.end = self.end + 1
            self.key[self.end] = key
            self.valor[self.end] = valor

    def consult(self,key):
        index = self.linear_search(key)
        if index < 0:
            return self.valor[index]
    def remove(self, key):
        pass

    def search(self, key):
        pass


test_table = Table(10)
test_table.insert("ABYG45", "CARRO 1")
test_table.insert("ABYG31", "CARRO 2")
print(test_table)
test_table.remove("ABYG45")
