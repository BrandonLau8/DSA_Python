class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word:str) -> None:
        print(f"\nInserting word: {word}")
        node = self.root
        for char in word:
            print(f" Checking '{char}'...")
            if char not in node.children:
                print(f"'{char}' not found, creating new node")
                node.children[char] = TrieNode()
            else:
                print(f"'{char}' exists, moving to next node.")
            node = node.children[char]
        node.isEndOfWord = True
        print(f"Marked end of word: {word}")
        
    def search(self, word: str) -> bool:
        print(f"\nSearching for word: {word}")
        node = self.root
        for char in word:
            print(f"  Looking for '{char}'...")
            if char not in node.children:
                print(f"    '{char}' not found. Word does not exist.")
                return False
            node = node.children[char]
        if node.isEndOfWord:
            print(f"  Found word: {word}")
            return True
        else:
            print(f"  Prefix exists but not a complete word: {word}")
            return False
    
    def startsWith(self, prefix:str) -> bool:
        print(f"\nChecking prefix: {prefix}")
        node = self.root
        for char in prefix:
            print(f"  Looking for '{char}'...")
            if char not in node.children:
                print(f"    '{char}' not found. Prefix does not exist.")
                return False
            node = node.children[char]
        print(f"  Prefix exists: {prefix}")
        return True
    
trie = Trie()

# Insert words
trie.insert("cat")
trie.insert("car")
trie.insert("dog")

# Search
trie.search("cat")      
trie.search("cap")      

# Prefix search
trie.startsWith("ca")   
trie.startsWith("do")   
trie.startsWith("da") 

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word:str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            else:
                node = node.children[char]
        node.isEndOfWord = True
    
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.isEndOfWord:
            return True
        else:
            return False
    
    def startsWith(self, prefix:str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node =  node.children[char]
        return True
   