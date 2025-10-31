def first_non_repeating_char(s):
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
        
    return None

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
    
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sounds(self):
        pass
    
class Dog(Animal):
    def make_sounds(self):
        print("woof")
        
class Cat(Animal):
    def make_sounds(self):
        print("meow")
        
Dog().make_sounds()