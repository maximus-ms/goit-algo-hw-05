class HashTable:
    """
    A class to store (key, value) data.
    Supported methods: insert(), get(), delete(), get_hash().
    """

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def __find(self, key):
        key_hash = self.get_hash(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return key_hash, pair
        return key_hash, (None, None)

    def get_hash(self, key):
        """
        Return a hash value of a "key"
        """
        return hash(key) % self.size

    def insert(self, key, value):
        """
        Add a new item or update if exist.
        Return True
        """
        key_hash, pair = self.__find(key)

        if pair[0] is None:
            self.table[key_hash].append([key, value])
        else:
            pair[1] = value
        return True

    def get(self, key):
        """
        Get value for a *key* or None if doesn't exist.
        """
        _, pair = self.__find(key)
        return pair[1]

    def delete(self, key):
        """
        Delete (key, value) and return True.
        Return False if 'key' doesn't exist.
        """
        key_hash, pair = self.__find(key)
        if pair[0] is None:
            return False
        self.table[key_hash].remove(pair)
        return True


def main():
    H = HashTable(5)
    print("Insert 'apple':", H.insert("apple", 10))
    print("Insert 'orange':", H.insert("orange", 20))
    print("Insert 'banana':", H.insert("banana", 30))

    print("Hash 'apple':", H.get_hash("apple"))
    print("Hash 'orange':", H.get_hash("orange"))
    print("Hash 'banana':", H.get_hash("banana"))
    print("Hash 'papaya':", H.get_hash("papaya"))

    print("Get 'apple':", H.get("apple"))
    print("Get 'orange':", H.get("orange"))
    print("Get 'banana':", H.get("banana"))

    print("Delete 'orange'", H.delete("orange"))
    print("Delete 'orange'", H.delete("orange"))
    print("Delete 'papaya'", H.delete("papaya"))

    print("Get 'apple':", H.get("apple"))
    print("Get 'orange':", H.get("orange"))
    print("Get 'banana':", H.get("banana"))


if __name__ == "__main__":
    main()
