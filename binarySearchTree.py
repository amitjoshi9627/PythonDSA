	class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

def insert(root,data):
	if root is None:
		root =  Node(data)
	
	else:
		if root.data>data:
			if root.left is None:
				root.left = Node(data)
			else:
				insert(root.left,data)
		else:
			if root.right is None:
				root.right = Node(data)
			else:
				insert(root.right,data)
def minnode(root):
	while root.left:
		root = root.left
	return root

	
def delete(root,data):
	if root:
		if root.data < data:
			root.right = delete(root.right,data)
		elif root.data >data:
			root.left = delete(root.left, data)
		else:
			if root.left == None:
				temp = root.right
				return temp
			elif root.right == None:
				temp = root.left
				return temp
			else:
				minNode = minnode(root.right)
				root.data = minNode.data
				root.right = delete(root.right,minNode.data)
	return root
def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end=" ")
		inorder(root.right)

def checkBst(root,arr):
	if root:
		checkBst(root.left,arr)
		arr.append(root.data)
		checkBst(root.right,arr)


r = Node(30)
insert(r,20)
r.left = Node(100)
r.right = Node(14)
#insert(r,40)
#insert(r,70)
#insert(r,60)
#insert(r,80)
inorder(r)
print()
#r = delete(r,60)
#inorder(r)
#print()
#print(minnode(r).data)
arr=[]
checkBst(r,arr)
if sorted(arr) == arr:
	print("It's not a BST tree")
else:
	print("It's a BST tree")
