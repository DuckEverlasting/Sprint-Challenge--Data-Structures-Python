class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while current:
            if value < current.value:
                if not current.left:
                    current.left = BinarySearchTree(value)
                    return 1
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = BinarySearchTree(value)
                    return 1
                else:
                    current = current.right
    
    def insert_no_dupes(self, value):
        current = self
        while current:
            if value == current.value:
                return 0
            if value < current.value:
                if not current.left:
                    current.left = BinarySearchTree(value)
                    return 1
                else:
                    current = current.left
            else:
                if not current.right:
                    current.right = BinarySearchTree(value)
                    return 1
                else:
                    current = current.right
            
    def contains(self, target):
        current = self
        while current:
            if target == current.value:
                return True
            elif target < current.value:
                if not current.left:
                    return False
                else:
                    current = current.left
            elif target > current.value:
                if not current.right:
                    return False
                else:
                    current = current.right

    def get_max(self):
        current = self
        while current:
            if current.right:
                current = current.right
            else:
                return current.value

    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    def in_order_return(self, node, output=[]):
        if node.left:
            self.in_order_return(node.left, output)
        output.append(node.value)
        if node.right:
            self.in_order_return(node.right, output)
        return output