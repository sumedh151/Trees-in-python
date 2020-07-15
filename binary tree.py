class Node():
	def __init__(self , value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self,root):
		self.root = Node(root)

	def inorder(self):
		if self.root.left is not None:
			self.root.left.inorder()
		print(self.root.value, end =" ")
		if self.root.right is not None:
			self.root.right.inorder()

	def preorder(self):
		print(self.root.value, end =" ")
		if self.root.left is not None:
			self.root.left.preorder()
		if self.root.right is not None:
			self.root.right.preorder()

	def postorder(self):
		if self.root.left is not None:
			self.root.left.postorder()
		if self.root.right is not None:
			self.root.right.postorder()
		print(self.root.value, end =" ")

	def iterative_preorder(self):
		stack = list()
		print(self.root)
		while self.root or len(stack)!=0:
			if self.root:
				print(self.root.value)
				stack.append(self.root)
				if self.root.left is not None:
					self.root = self.root.left.root
				else:
					self.root = None
			else:
				self.root = stack.pop()
				if self.root.right is not None:
					self.root = self.root.right.root
				else:
					self.root = None

	def iterative_inorder(self):
		stack = list()
		while self.root or len(stack)!=0:
			if self.root:
				stack.append(self.root)
				if self.root.left is not None:
					self.root = self.root.left.root
				else:
					self.root = None
			else:
				self.root = stack.pop()
				print(self.root.value)
				if self.root.right is not None:
					self.root = self.root.right.root
				else:
					self.root = None

	def count_nodes(self):
		if self.root != None:
			if self.root.left is not None:
				x = self.root.left.count_nodes()
			else:
				x=0
			if self.root.right is not None:
				y = self.root.right.count_nodes()
			else:
				y=0
			return x+y+1
		else:
			return 0

	def count_height(self):
		if self.root==None:
			return 0
		if self.root.left is not None:
			x = self.root.left.count_height()
		else:
			x=0
		if self.root.right is not None:
			y = self.root.right.count_height()
		else:
			y=0
		if x > y:
			return x+1
		else:
			return y+1

q = list()
x = int(input('Enter root value:'))
root = BinaryTree(x)
q.append(root)

while (len(q) != 0):
	temp = q.pop(0)
	
	x = int(input('Enter left child value of {} : '.format(temp.root.value)))
	if x != -1:
		tree = BinaryTree(x)
		temp.root.left = tree
		q.append(tree)

	x = int(input('Enter right child value of {} : '.format(temp.root.value)))
	if x != -1:
		tree = BinaryTree(x)
		temp.root.right = tree
		q.append(tree)

print('\n')
print('Preorder traversal:', end=" ")
root.preorder()
print('\n')
print('Inorder traversal:', end=" ")
root.inorder()
print('\n')
print('Postorder traversal:', end=" ")
root.postorder()
print('\n')
print('Total nodes in tree:', root.count_nodes())
print('\n')
print('Total height of tree:', root.count_height())