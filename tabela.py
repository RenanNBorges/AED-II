class Table:
    def __init__(self, sizemax):
        self.key = [None] * (sizemax + 1)
        self.value = [None] * (sizemax + 1)
        self.li = 1
        self.ls = sizemax
        self.ini = self.li - 1
        self.end = self.ls + 1

    def __repr__(self):
        string = ""
        if not self.is_empty():
            for i in range(self.ini, self.end + 1):
                string = string + str(self.key[i]) + " : " + str(self.value[i]) + "\n"

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
            return self.end - (self.ini - 1)
        else:
            return 0

    def insert(self, key, value):
        index = self.binary_search(key)
        if index > 0:
            self.value[index] = value
        elif not self.is_full():
            if self.is_empty():
                self.ini = self.li
                self.end = self.ini
            else:
                self.end = self.end + 1
            self.key[self.end] = key
            self.value[self.end] = value
        self.insertion_sort()

    def consult(self, key):
        index = self.linear_search(key)
        if index < 0:
            return self.value[index]

    def remove(self, key):
        index = self.linear_search(key)
        if index > 0:
            for i in range(index, self.end):
                self.key[i] = self.key[i + 1]
                self.value[i] = self.value[i + 1]
            self.end -= 1

    def destroy(self):
        self.ini = self.li - 1
        self.end = self.ls + 1

    def insertion_sort(self):
        i = self.li + 1
        while i <= self.size():
            temp_key = self.key[i]
            temp_value = self.value[i]
            switch = False
            j = i - 1
            while j >= self.li and self.key[j] > temp_key:
                self.key[j + 1] = self.key[j]
                self.value[j + 1] = self.value[j]
                switch = True
                j -= 1

            if switch:
                self.key[j + 1] = temp_key
                self.value[j + 1] = temp_value
            i += 1

    def linear_search(self, key):
        if not self.is_empty():
            for i in range(self.ini, self.end + 1):
                if self.key[i] == key:
                    return i
        return 0

    def binary_search(self, key):
        if not self.is_empty():
            ini_var = self.ini
            end_var = self.end
            middle_var = (ini_var + end_var) // 2
            while end_var >= ini_var:
                if key == self.key[middle_var]:
                    return middle_var
                elif key < self.key[middle_var]:
                    end_var = middle_var - 1
                elif key > self.key[middle_var]:
                    ini_var = middle_var + 1
                else:
                    return 0
                middle_var = (ini_var + end_var) // 2
        return 0

