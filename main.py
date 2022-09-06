import json
class Trie:
    def __init__(self, is_end=False):
        self.children = {}
        self.is_end = is_end

    def insert(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

    def search(self, s):
        node = self
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node if node.is_end else None

    def get_strings(self):
        def rec(node, string, strings):
            if node.is_end:
                strings.append("".join(string))
            for ch in node.children:
                string.append(ch)
                rec(node.children[ch], string, strings)
                string.pop()
        strings = []
        rec(self, [], strings)
        return strings

    def autocomplete(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]
        return [prefix + word for word in node.get_strings()]

    def trie_build(self):
        with open("words.txt", "r") as words:
            for word in words:
                trie.insert(word)

if __name__ == "__main__":
    trie = Trie()
    print("Just a second for building trie...")
    trie.trie_build()
    prefix = input("Enter prefix of word : ")
    suggestions = trie.autocomplete(prefix)
    for word in suggestions:
        print(word)

