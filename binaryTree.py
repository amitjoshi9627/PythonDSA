class Node:
	def __init__(self,data):
		self.left = None
		self.right = None
		self.data = data

def inorder(root):
	if root:
		inorder(root.left)
		print(root.data,end = ' ')
		inorder(root.right)
def level_order(root):
	if root is None:
		return
	q = [root]

	while len(q):
		print(q[0].data,end=' ')
		temp = q.pop(0)

		if temp.left:
			q.append(temp.left)
		if temp.right:
			q.append(temp.right)


def inorder_stack(root):
	if not root:
		return

	s = []
	current = root
	while True:
		if current is not None :
			s.append(current)
			current = current.left

		elif len(s):
			current = s.pop()
			print(current.data,end=' ')
			current = current.right
		else:
			break
def height(root):
	if root:
		return 1+ max(height(root.left),height(root.right))
	else:
		return 0

def level_order_line_by_line(root):
	q = []	
	q.append(root)
	ans = 0
	while True:
		# ans = max(ans,sum([i.data for i in q]))
		k = 0
		x = len(q)
		while x>0:
			x-=1
			i = q.pop(0)
			print(i.data,end=' ')
			if i.left:
				q.append(i.left)
			if i.right:
				q.append(i.right)
		print()
		if not len(q):
			break

if __name__ == '__main__':
	root = Node(24) 
	root.left = Node(3) 
	root.right = Node(9) 
	root.left.left = Node(1) 
	root.left.right = Node(2) 
	root.right.left = Node(4)
	root.right.right = Node(5)
	inorder_stack(root)
	print()
	inorder(root)
	print()
	level_order(root)
	print()
	print(height(root))
	print()
	level_order_line_by_line(root)
	print()