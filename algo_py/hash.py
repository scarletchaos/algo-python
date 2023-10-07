from algo_py.linkedlist import LinkedList
from algo_py.decorators import timeit


class HashTable:
    def __init__(self):
        self.table = [None for _ in range(128)]
        self.count = 0

    def hash(self, s: str) -> int:
        k = 2**15
        m = 2**20
        power = 0
        result = 0

        for letter in s:
            result += ord(letter) * k**power % m
            power += 1

        return result

    def calculate_index(self, key, m):
        return self.hash(key) % m if m else 1

    def set(self, key, value, _table=None):
        self.rebuild()
        table = _table if _table else self.table
        index = self.calculate_index(key, len(table))
        if not table[index]:
            table[index] = LinkedList()
        table[index].append({"key": key, "value": value})
        self.count += 1

    @timeit
    def get(self, key):
        index = self.calculate_index(key, len(self.table))
        if self.table[index]:
            for pair in self.table[index].fore():
                if pair["key"] == key:
                    return pair["value"]
        return None

    def rebuild(self):
        if len(self.table) == 0:
            self.table = [None for _ in range(128)]
        else:
            load_factor = self.count / len(self.table)
            if load_factor > 0.8:
                new_table = [None for _ in range(len(self.table) * 2)]
                for _list in self.table:
                    if _list:
                        for pair in _list.fore():
                            self.count = 0
                            self.set(pair["key"], pair["value"], new_table)
                self.table = new_table


if __name__ == "__main__":
    ht = HashTable()
    ht.set("ya", "ebu sobak")
    for i in range(1023):
        print(i)
        ht.set(str(i), "poshel")
    print(ht.get("ya"))
