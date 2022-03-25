# Design a HashMap without using any built-in hash table libraries. 
# 
#  Implement the MyHashMap class: 
# 
#  
#  MyHashMap() initializes the object with an empty map. 
#  void put(int key, int value) inserts a (key, value) pair into the HashMap. 
# If the key already exists in the map, update the corresponding value. 
#  int get(int key) returns the value to which the specified key is mapped, or -
# 1 if this map contains no mapping for the key. 
#  void remove(key) removes the key and its corresponding value if the map 
# contains the mapping for the key. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2
# ,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the 
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= key, value <= 10⁶ 
#  At most 10⁴ calls will be made to put, get, and remove. 
#  
#  Related Topics Array Hash Table Linked List Design Hash Function 👍 2500 👎 2
# 68


# leetcode submit region begin(Prohibit modification and deletion)
class MyHashMap:

    def __init__(self):
        self.prime_number = 1069
        self.hash_list = [None]*self.prime_number

    def put(self, key: int, value: int) -> None:
        index = key % self.prime_number

        if self.hash_list[index] is None:
            self.hash_list[index] = []

        append = True
        for i, (key_, value_) in enumerate(self.hash_list[index]):
            if key == key_:
                self.hash_list[index][i] = (key, value)
                append = False
                break

        if append:
            self.hash_list[index].append((key, value))

    def get(self, key: int) -> int:
        index = key % self.prime_number
        if self.hash_list[index] is not None:
            for key_, value_ in self.hash_list[index]:
                if key == key_:
                    return value_
        return -1

    def remove(self, key: int) -> None:
        index = key % self.prime_number
        if self.hash_list[index] is not None:
            for i, (key_, value) in enumerate(self.hash_list[index]):
                if key == key_:
                    self.hash_list[index].pop(i)
                    break

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# leetcode submit region end(Prohibit modification and deletion)
