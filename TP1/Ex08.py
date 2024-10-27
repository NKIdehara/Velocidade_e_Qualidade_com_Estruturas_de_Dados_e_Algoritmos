def bubbleSort(self):
        for last in range(self.__nItems-1, 0, -1):
            for inner in range(last):
                if self.__a[inner] > self.__a[inner+1]:
                    self.swap(inner, inner+1)

        ultimo = self.__nItems
        for primeiro in range(ultimo):
            for externo in range(ultimo, primeiro, -1):
                if self.__a[externo] < self.__a[externo-1]:
                    self.swap(externo, externo-1)
