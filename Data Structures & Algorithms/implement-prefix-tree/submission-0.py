class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = {}
    
    def addNeighbour(self, neighbour) -> None:
        self.next[neighbour.data] = neighbour

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        current_node = self.root
        for letter in word:
            current_node_neighbor = current_node.next
            if letter in current_node_neighbor:
                current_node = current_node_neighbor[letter]
            else:
                new_neighbour = Node(letter)
                current_node.addNeighbour(new_neighbour)
                current_node = new_neighbour
        new_neighbour = Node(None)
        current_node.addNeighbour(new_neighbour)


    def search(self, word: str) -> bool:
        current_node = self.root
        for letter in word:
            current_node_neighbor = current_node.next
            if letter not in current_node_neighbor:
                return False
            else:
                current_node = current_node_neighbor[letter]

        if None not in current_node.next:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for letter in prefix:
            current_node_neighbor = current_node.next
            if letter not in current_node_neighbor:
                return False
            else:
                current_node = current_node_neighbor[letter]
        
        return True
        
        