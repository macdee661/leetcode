class MyHashMap:

    def __init__(self):
        self.hashmap = []
        

    def put(self, key: int, value: int) -> None:
        for index in range(len(self.hashmap)):
            if self.hashmap[index][0] == key:
                self.hashmap[index] = [key, value]
                return
        self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for index in range(len(self.hashmap)):
            if self.hashmap[index][0] == key:
                return self.hashmap[index][1]
        return -1
         
    def remove(self, key: int) -> None:
        new_map = []
        for index in range(len(self.hashmap)):
            if self.hashmap[index][0] != key:
                new_map.append(self.hashmap[index])
        self.hashmap = new_map

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)