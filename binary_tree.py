#!/usr/bin/python
import sys

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


    def insert_node(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert_node(data)
        else:
            self.data = data

   
    def search_node(self, data, parent=None):
        if data < self.data:
            if self.left == None:
                return None, None
            return self.left.search_node(data, self)
        elif data > self.data:
            if self.right == None:
                return None, None
            return self.right.search_node(data, self)
        else:
            print ("Node found, value : %i" %(data)) 
            return self, parent

    
    def print_tree_inorder(self):
        if self.left:
            self.left.print_tree_inorder()
        print self.data,
        if self.right:
            self.right.print_tree_inorder()

    
    def print_tree_postorder(self):
        if self.left:
            self.left.print_tree_postorder()
        if self.right:
            self.right.print_tree_postorder()
        print self.data,    

    
    def print_tree_preorder(self):
        print self.data,
        if self.left:
            self.left.print_tree_preorder()
        if self.right:
            self.right.print_tree_preorder()

    
    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


    def delete_node(self, data):
        node, parent = self.search_node(data)
        if node != None:
            children_count = node.children_count()
            if children_count == 0:  # if node has no children
                
                if parent:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    node = None
                else:
                    self.data = None

            elif children_count == 1: #If one child node is there
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left == node:
                        parent.left = n
                    else:
                        parent.right = n
                    del node
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data

            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                
                node.data = successor.data

                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right



#a=  int(raw_input("Enter a value for root node :"))
root=Node(int(raw_input("Enter a value for root node :")))
print("")
'''
node_count=(int(raw_input("Enter the no. of nodes you want to create other then root : ")))

for i in range(node_count):
    root.insert(int(raw_input("Enter a value:")))
    i+=1


root.insert(12)
root.insert(6)
root.insert(23)
root.insert(3)
root.insert(63)
root.insert(14)


print "Inorder Traversal :"
(root.print_tree_inorder())
print "\nPreorder Traversal :"
root.print_tree_preorder()
print "\nPostorder Traversal"
root.print_tree_postorder()


root.print_tree_inorder()
print "\n"
node, parent =root.search(int(raw_input("Enter the value you want to search : ")))
print node, parent

node.delete(int(raw_input("Enter the value you want to delete :")))
root.print_tree_inorder()
'''



def bin_tree():
    while(1):
        print "Please enter an key :\n1. Insert\n2. Traversal inorder\n3. Traversal Preorder\n4. Traversal Postorder\n5. Searching\n6. Deletion\n7. Exit"

        def quit():
            sys.exit(1)

        def insert():

            node_count=(int(raw_input("Enter the no. of nodes you want to create other then root : ")))

            for i in range(node_count):
                root.insert_node(int(raw_input("Enter a value(%i):"%(i+1))))
                i+=1

        def traversal_Inorder():
            print ("Inorder traversal")
            root.print_tree_inorder()

        def traversal_Preorder():
            print ("Preorder traversal")
            root.print_tree_preorder()

        def traversal_Postorder():
            print ("Postorder traversal")
            root.print_tree_postorder()

        def search():
            node, parent =root.search_node(int(raw_input("Enter the value you want to search : ")))
            if node == None:
                print ("value not found")

        def deletion():
            root.delete_node(int(raw_input("Enter the value you want to delete :")))

        options = {
                   1 : insert,
                   2 : traversal_Inorder,
                   3 : traversal_Preorder,
                   4 : traversal_Postorder,
                   5 : search,
                   6 : deletion,
                   7 : quit,   
        }   

        options[int(raw_input(""))]()
        print ("\n")


if __name__ == '__main__':
    bin_tree()