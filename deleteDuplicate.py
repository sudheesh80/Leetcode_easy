# More informations about linked list in https://realpython.com/linked-lists-python/
class LinkList():
    def __init__(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for x in nodes:
                node.next = Node(data=x)
                node = node.next
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return "->".join(nodes)
    def deleteDuplicates(self):
        current_node = self.head
        while current_node and current_node.next:
            if current_node.data == current_node.next.data:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data


headlist = LinkList(["1","1","1","2","2","3"])
headlist.deleteDuplicates()
print(headlist)
