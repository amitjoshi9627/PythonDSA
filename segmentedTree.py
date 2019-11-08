from __future__ import division
import math
import itertools
class LPSTree:
	def __init__(self, n, value=None, reducef=None, modulo=None):
		if n <= 0:
			raise ValueError("n most be greater than 0")
		self.n = n
		size = 1;
		while(size < n):
			size *= 2
		size *= 2
		self.size = size
		self.tree = [None] * size
		self.boolset = [False] * size
		self.booladd = [False] * size
		self.lazyset = [None] * size
		self.lazyadd = [None] * size
		self.modulo = modulo
		if not reducef:
			reducef = sum
		if reducef == sum:
			self.nodef = (lambda val, n: val*n)
		elif reducef == max or reducef == min:
			self.nodef = (lambda val, n: val)
		else:
			raise ValueError("reducef can only be sum, max or min")
		if self.modulo:
			self.reducef = lambda x: reducef(x) % self.modulo
		else:
			self.reducef = reducef

		if value != None:
			array = [value] * n
		else:
			array = [0] * n
		def construct(tree, array, sleft, sright, v):
			if sleft+1 == sright:
				tree[v] = array[sleft]
				return tree[v]
			smid = (sleft + sright) // 2
			tree[v] = self.reducef((construct(tree, array, sleft, smid, 2*v+1),
					construct(tree, array, smid, sright, 2*v+2)))
			return tree[v]
		construct(self.tree, array, 0, n, 0)

	def __len__(self):
		return self.n

	def _lazypropagate(self, v, vleft, vright):
		tree = self.tree
		boolset = self.boolset
		booladd = self.booladd
		lazyset = self.lazyset
		lazyadd = self.lazyadd
		vmid = (vleft + vright) // 2
		# print(tree), v, tree[2*v+1], boolset[v], booladd[v]
		if boolset[v]:
			tree[2*v+1] = self.nodef(lazyset[v], vmid-vleft)
			tree[2*v+2] = self.nodef(lazyset[v], vright-vmid)
			if self.modulo:
				tree[2*v+1] %= self.modulo
				tree[2*v+2] %= self.modulo
			boolset[2*v+1] = boolset[2*v+2] = True
			booladd[2*v+1] = booladd[2*v+2] = False
			lazyset[2*v+1] = lazyset[2*v+2] = lazyset[v]
			boolset[v] = False
		if booladd[v]:
			tree[2*v+1] += self.nodef(lazyadd[v], vmid-vleft)
			tree[2*v+2] += self.nodef(lazyadd[v], vright-vmid)
			if self.modulo:
				tree[2*v+1] %= self.modulo
				tree[2*v+2] %= self.modulo
			if booladd[2*v+1]:
				lazyadd[2*v+1] += lazyadd[v]
			else:
				booladd[2*v+1] = True
				lazyadd[2*v+1] = lazyadd[v]
			if booladd[2*v+2]:
				lazyadd[2*v+2] += lazyadd[v]
			else:
				booladd[2*v+2] = True
				lazyadd[2*v+2] = lazyadd[v]
			booladd[v] = False

	def get(self, start, stop):
		n = self.n
		if not(start < stop and start >=0 and stop <= n):
			raise IndexError(start, stop)
		tree = self.tree
		boolset = self.boolset
		booladd = self.booladd
		lazyset = self.lazyset
		lazyadd = self.lazyadd
		def _get(sleft, sright, v, vleft, vright):
			# print v, start, stop, vleft, vright, tree
			if sleft>=vright or sright <= vleft:
				return
			if sleft<=vleft and sright >= vright:
				# if self.modulo:
				# 	tree[v] %= self.modulo
				return tree[v]
			vmid = (vleft + vright) // 2
			self._lazypropagate(v, vleft, vright)
			# print v, start, stop, vleft, vright, tree
			return self.reducef([x for x in
								(_get(sleft, sright, 2*v+1, vleft, vmid),
								_get(sleft, sright, 2*v+2, vmid, vright))
								if x != None])
		return _get(start, stop, 0, 0, n)

	def set(self, start, stop, value):
		n = self.n
		if not(start < stop and start >=0 and stop <= n):
			raise IndexError(start, stop)
		tree = self.tree
		boolset = self.boolset
		booladd = self.booladd
		lazyset = self.lazyset
		lazyadd = self.lazyadd
		def _set(sleft, sright, v, vleft, vright, value):
			# print v, start, stop, vleft, vright, value, tree
			if sleft >= vright or sright <= vleft:
				return
			if sleft <= vleft and sright >= vright:
				tree[v] = self.nodef(value, vright-vleft)
				if self.modulo:
					tree[v] %= self.modulo
				boolset[v] = True
				booladd[v] = False
				lazyset[v] = value

				return
			vmid = (vleft + vright) // 2
			self._lazypropagate(v, vleft, vright)
			_set(sleft, sright, 2*v+1, vleft, vmid, value)
			_set(sleft, sright, 2*v+2, vmid, vright, value)
			tree[v] = self.reducef((tree[2*v+1], tree[2*v+2]))
		_set(start, stop, 0, 0, n, value)

	def add(self, start, stop, diff):
		n = self.n
		if not(start < stop and start >=0 and stop <= n):
			raise IndexError(start, stop)
		tree = self.tree
		boolset = self.boolset
		booladd = self.booladd
		lazyset = self.lazyset
		lazyadd = self.lazyadd
		def _add(sleft, sright, v, vleft, vright, diff):
			if sleft >= vright or sright <= vleft:
				return
			if sleft <= vleft and sright >= vright:
				tree[v] += self.nodef(diff, vright-vleft)
				if self.modulo:
					tree[v] %= self.modulo
				if booladd[v]:
					lazyadd[v] += diff
				else:
					booladd[v] = True
					lazyadd[v] = diff
				return
			vmid = (vleft + vright) // 2
			self._lazypropagate(v, vleft, vright)
			_add(sleft, sright, 2*v+1, vleft, vmid, diff)
			_add(sleft, sright, 2*v+2, vmid, vright, diff)
			tree[v] = self.reducef((tree[2*v+1], tree[2*v+2]))
			# if self.modulo:
			# 	tree[v] %= self.modulo
		_add(start, stop, 0, 0, n, diff)

	def __getitem__(self, index):
		return self.get(index, index+1)

	def __setitem__(self, index, value):
		self.set(index, index+1, value)

	def __repr__(self):
		return repr([self[x] for x in range(self.n)])

	def tolist(self):
		return [self[x] for x in range(self.n)]

def allSubArrays(xs):
    n = len(xs)
    indices = list(range(n+1))
    for i,j in itertools.combinations(indices,2):
        if len(xs[i:j])<32:
        	yield xs[i:j]
def buildTree(arr,tree,st,end,treeNode):
	mid = (st+end)//2
	if st == end:
		tree[treeNode] = 0
		return
	buildTree(arr,tree,st,mid,2*treeNode+1)
	buildTree(arr,tree,mid+1,end,2* treeNode+2)
	tree[treeNode] = tree[2*treeNode+1] & tree[2*treeNode+2]
def updaterange(cn,lazy,tree,ss,se,us,ue,diff):
	if lazy[cn]!=0:
		tree[cn] = (se-ss+1)*lazy[cn]
		if ss is not se:
			lazy[2*cn+1] += lazy[cn]
			lazy[2*cn+2] += lazy[cn]
		lazy[cn] = 0
	if (ss>se  or ss>ue or se<us):
		return 
	if ss>=us and se<=ue:
		tree[si]+=1

def query(tree,l,r,ts,te,cn):
	if l<=ts and r>=te:
		#print('Yeah',tree[cn],ts,te)
		return tree[cn]
	if l>te or r<ts:
		#print('yeah')
		return 2047
	mid = (ts+te)//2
	return query(tree,l,r,ts,mid,2*cn+1) & query(tree,l,r,mid+1,te,2*cn+2)

t = int(input())
for i in range(t):
	n,q = input().split()
	n = int(n)
	q = int(q)
	arr = [int(i) for i in input().split()]
	x = int((math.ceil(math.log2(n))))	
	max_size = 2 * int(2**x )- 1
	tree3=[127 for i in range(0,max_size+1)]
	tree2=[0 for i in range(0,max_size+1)]		
	lazy = [0 for i in range(0,max_size+1)]
	tree = LPSTree(max_size)
	d={}
	count=0
	#print(tree)
	buildTree(arr,tree3,0,n-1,0)
	for c in allSubArrays(arr[:]):
			l1 =arr.index(c[0])+1
			r1 = arr.index(c[-1])+1
			if len(c)>=32:
				d[(l1,r1)]=1
				count+=1
				continue
			if 0 in c:
				d[(l1,r1)] =1
				count+=1
				continue
			if len(c) == 1:
				x= c[0]
				sr = math.sqrt(x) 
				if((sr - math.floor(sr)) == 0):
					count+=1
					d[(l1,r1)]=1
					continue
				else:
					d[(l1,r1)] = 0
			else:
				ans = query(tree3,arr.index(c[0]),arr.index(c[-1]),0,n-1,0)
				if ans == 0 or ans ==1 or ans == 4 or ans == 9 or ans == 16 or ans == 25 or ans == 36 or ans == 49 or ans == 64 or ans is 81 or ans is 100 or ans is 121:
					d[(l1,r1)]=1
					count+=1
					continue
				else:
					sr = math.sqrt(ans) 
					if((sr - math.floor(sr)) == 0):
						count+=1
						d[(l1,r1)]=1
						#continueto Your Side
					else:
						d[(l1,r1)] = 0
	
	for i in range(q):
		l,r = input().split()
		l = int(l)
		r = int(r)
		count = 0
		print(d[(l,r)])
			
		#print(count)
