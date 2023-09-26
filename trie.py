'''
Trie (Prefix Tree) Implementation in Python
'''

class TrieNode:

    def __init__(self, char = None):

        # self.char: Str or None
        # stores the char
        self.char = char
        
        # self.is_end: Dict
        # indicates if this is a word ending with this char.
        self.children = {} 

        # self.children: Boolean
        # a dictionary of all child nodes. 
        # where key = char and value = node
        self.is_end = False

        # self.count: Int
        # the number of times the word is fetched.
        self.count = 0 

class Trie:

    # Trie() 
    # initializes the trie object with a root node
    def __init__(self):
        self.root = TrieNode()
    
    # trie.insert() 
    # inserts the string word into the trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(char)
            node = node.children[char]
        node.is_end = True
        node.count += 1

    # trie.search_word() 
    # returns True is the string word exists
    # Otherwise return False
    def search_word(self, word):
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False
        return node.is_end
    
    # trie.search_prefix() 
    # returns all words in the Trie starting with the prefix
    # returns an empty list if no words exist with this prefix.
    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return []
        self.words = []
        self.dfs(node, prefix)
        return self.words

    # The helper function of search_prefix()
    def dfs(self, node, prefix):
        if node.is_end:
            self.words.append(prefix)
        for child in node.children.values():
            self.dfs(child, prefix + child.char)