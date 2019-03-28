# TODO better way of storing data inside nodes.
from numpy import array,concatenate
from copy import deepcopy
from pydot import Dot,Edge,Node,Subgraph
from math import ceil

# Algorithm credits:
# http://www.cburch.com/cs/340/reading/btree/index.html


def main():
  ''' Do something! '''
  test_remove()

### Testing and example suite ################################

def test_insert(size=4,ninsert=100):
  ''' Test insertions by adding a bunch of things and checking that they are there.
  Args:
    size (int): max size of the nodes.
    ninsert (int): number of insertions to attempt.
  '''
  from random import randint,random,seed
  from time import sleep
  seed(10)
  tree = BplusTree(size)
  ans = {}
  for i in range(ninsert):
    key = randint(0,size*30)
    val = round(random(),3)
    ans[key] = val
    print()
    print("({}) About to insert {},{}".format(i,key,val))
    #input("Press enter to continue")
    tree.insert(key,val)
    tree.make_pydot_graph()
    shakedown(tree,ans)

def test_scan(size=3,ninsert=25):
  ''' Test insertions by adding a bunch of things and checking that they are there.
  Args:
    size (int): max size of the nodes.
    ninsert (int): number of insertions to attempt.
  '''
  tree = BplusTree(size)
  for key in range(ninsert):
    val = str(chr(key+97))
    tree.insert(key,val)
  tree.make_pydot_graph()
  print(tree.serialize())

def test_remove(size=4,ninsert=40):
  ''' Test insertions by adding a bunch of things and checking that they are there.
  Args:
    size (int): max size of the nodes.
    ninsert (int): number of insertions to attempt.
  '''
  from random import randint,random,seed,shuffle
  seed(1023)
  tree = BplusTree(size)
  ans = {}
  for i in range(ninsert):
    key = randint(0,size*30)
    val = round(random(),3)
    ans[key] = val
    tree.insert(key,val)

  shakedown(tree,ans)

  tree.make_pydot_graph()

  keys = list(ans.keys())
  shuffle(keys)

  for key in keys:
    print("About to remove {}".format(key))
    input("Press enter to continue.")
    ans.pop(key)
    tree.remove(key)
    tree.make_pydot_graph()
    shakedown(tree,ans)

def shakedown(tree,solutions):
  for key in solutions:
    print(key)
    guess = tree.query(key)
    assert guess == solutions[key],'{} yields {} instead of {}'.format(key,guess,solutions[key])
  print("Shakedown!")

### Implementation suite #####################################

class BplusTree:
  ''' Contains all nodes and facilitates storing, querying, and deletion.'''
  def __init__(self,maxsize):
    ''' 
    Args:
      maxsize (int): largest node size for all nodes.
    '''
    self.maxsize = maxsize
    self.root = LeafNode(maxsize)

  def make_pydot_graph(self,figname='tree'):
    ''' Use Graphviz to generate a graphical representation of the tree.
    Args:
      figname (str): where to store the figure.
    '''
    graph = Dot(graph_type='graph')
    #graph.add_node(Node(self.root.display(),shape='diamond'))
    edgelist = self.root.append_edgelist()
    for edge in edgelist:
      graph.add_node(edge[0])
      graph.add_node(edge[1])
      graph.add_edge(Edge(*edge))
    graph.write_png(figname+'.png')

  def insert(self,key,value):
    ''' Insert new data into tree.
    Args:
      key (orderable): label for data. Must interact with < sign (i.e. be orderable).
      value: Data to store.
    '''
    self.root.insert(key,value)
    if self.root.parent is not None:
      #print("Root update.")
      self.root = self.root.parent

  def query(self,key):
    ''' Recall data stored under key.
    Args:
      key (orderable): key where data was stored previously.
    Returns:
      data or None: the data that was stored, or None if data is missing.
    '''
    return self.root.query(key)
  
  def serialize(self):
    ''' Return all the leaves data as an array.'''
    focus = self.root
    while isinstance(focus,InternalNode):
      focus = focus.children[0]
    leaves = [focus.data]
    while focus.rsibling is not None:
      leaves.append(focus.rsibling.data)
      focus = focus.rsibling
    return concatenate(leaves)

  def remove(self,key):
    ''' Remove data stored under key from the tree. If key doesn't exist, does nothing.
    Args:
      key (orderable): key where data was stored previously.
    '''
    self.root.remove(key)
    if isinstance(self.root,LeafNode) and self.root.keys.shape[0]==0:
      raise AssertionError("Database is empty. I ain't coding for this edge (corner!) case, so fuck off...")
    elif len(self.root.children) == 1:
      print("Root update.")
      self.root = self.root.children[0]
      self.root.parent = None

class InternalNode:
  ''' Internal direction-finding class. Never exists at the bottom of the tree.'''
  def __init__(self,maxsize,parent):
    '''
    Args:
      maxsize (int): Maximum leaf size.
      parent (InternalNode): node which directs queries to this node.
    '''

    self.parent = parent
    self.maxsize = maxsize
    if self.parent is None:
      self.minsize = 1
    else:
      self.minsize = maxsize//2

    self.keys = array([])
    self.children = array([])

  def display(self):
    ''' Return string of contents '''
    return '[ ' + ' v '.join(self.keys.astype(int).astype(str)) + ' ]'

  def append_edgelist(self):
    ''' Internal function for generating Graphviz tree.'''
    edgelist = []
    for child in self.children:
      edgelist.append((
            Node(self.display(),shape='invhouse',fontname='monospace'),
            Node(child.display(),shape='rectangle',fontname='monospace')
          ))
      edgelist += child.append_edgelist()
    return edgelist

  # There is such beauty in this world!
  def birth(self,key,child):
    ''' Insert a key to this node.
    Args:
      key (orderable): smallest value larger than keys in child.
      child (LeafNode or InternalNode): node to keep track of.
    '''

    place = (self.keys < key).sum()

    # Case: normal insertion. TODO should insert after split for small speedup.
    self.keys = concatenate((self.keys[:place],array([key]),self.keys[place:]))
    self.children = concatenate((self.children[:place],array([child]),self.children[place:]))

    # Case: split required.
    if self.keys.shape[0] > self.maxsize:
      median = self.keys.shape[0]//2
      if self.parent is None:
        #print("Root split.")
        self.parent = InternalNode(self.maxsize,parent=None)
        self.parent.children = array([self])

      newleft = InternalNode(self.maxsize,parent=self.parent)

      newkey = self.keys[median]
      newleft.keys = self.keys[:median]
      newleft.children = self.children[:median+1]
      for child in newleft.children:
        child.parent = newleft # How sad that they are seperated!
      self.keys = self.keys[median+1:]
      self.children = self.children[median+1:]

      self.parent.birth(newkey,newleft)

  def insert(self,key,value):
    ''' Insert a value the correct descendent node.
    Args:
      key (orderable): label for the data.
      value: Data to be stored.
    '''
    place = (self.keys <= key).sum()
    self.children[place].insert(key,value)

  def query(self,key):
    ''' Direct query for key to the next step. '''
    place = (self.keys <= key).sum()
    #print(key)
    #print(self.keys,self.children)
    return self.children[place].query(key)

  def remove(self,key):
    ''' Direct the appropriate descendent to remove a data entry and its key from the tree.
    Args:
      key (orderable): label for the data.
    '''
    place = (self.keys <= key).sum()
    self.children[place].remove(key)

  # What is create can will is destroy.
  def filicide(self,place):
    ''' Remove a child.'''

    kplace = max(0,place-1)
    key = self.keys[kplace]

    self.keys = concatenate((self.keys[:kplace],self.keys[kplace+1:]))
    self.children = concatenate((self.children[:place],self.children[place+1:]))

    # If size is below minimum and not parent.
    if self.parent is not None and self.keys.shape[0] < self.minsize:
      parplace = (self.parent.keys <= key).sum()
      if parplace+1 < self.parent.children.shape and \
          self.parent.children[parplace+1].keys.shape[0] > self.parent.children[parplace+1].minsize:
        print("Internal rotating from right.")
        self.rotate_right(parplace)
      elif parplace != 0 and \
          self.parent.children[parplace-1].keys.shape[0] > self.parent.children[parplace-1].minsize:
        print("Internal rotating from left.")
        self.rotate_left(parplace)
      elif parplace+1 < self.parent.children.shape:
        print("Internal merging right.")
        self.merge_right(parplace)
      elif parplace != self.parent.children.shape:
        print("Internal merging left.")
        self.merge_left(parplace)
      else:
        raise AssertionError("Must either have siblings or be root. Fuck off!")

  def rotate_right(self,parplace):
    ''' Take a key from a right neighbor by rotating through parent.
    Args:
      parplace (int): index of self in parent.
    '''
    right = self.parent.children[parplace+1]

    # Move parent key here.
    self.keys = concatenate((self.keys,array([self.parent.keys[parplace]])))
    self.children = concatenate((self.children,array([right.children[0]])))
    self.children[-1].parent = self

    # Move right key to parent.
    self.parent.keys[parplace] = right.keys[0]

    # Remove data from right.
    right.keys = right.keys[1:]
    right.children = right.children[1:]

  def rotate_left(self,parplace):
    ''' Take a key from a left neighbor by rotating through parent.
    Args:
      parplace (int): index of self in parent.
    '''
    left = self.parent.children[parplace-1]

    # Move parent key here.
    self.keys = concatenate((array([self.parent.keys[parplace-1]]),self.keys))
    self.children = concatenate((array([left.children[-1]]),self.children))
    self.children[0].parent = self

    # Move left key to parent.
    self.parent.keys[parplace-1] = left.keys[-1]

    # Remove data from left.
    left.keys = left.keys[:-1]
    left.children = left.children[:-1]

  def merge_right(self,parplace):
    ''' Merge with right sibling.'''
    right = self.parent.children[parplace+1]

    self.keys = concatenate((self.keys,array([self.parent.keys[parplace]]),right.keys))
    self.children = concatenate((self.children,right.children))
    for child in right.children:
      child.parent = self

    self.parent.filicide(parplace+1)

  def merge_left(self,parplace):
    ''' Merge with left sibling.'''
    left = self.parent.children[parplace-1]

    self.keys = concatenate((left.keys,array([self.parent.keys[parplace-1]]),self.keys))
    self.children = concatenate((left.children,self.children))
    for child in left.children:
      child.parent = self

    self.parent.filicide(parplace-1)

class LeafNode:
  ''' Data container class. Always exists at the bottom of the tree.'''
  def __init__(self,maxsize,left_sibling=None,right_sibling=None,parent=None):
    '''
    Args:
      maxsize (int): Maximum leaf size.
      left_sibling (LeafNode): leaf node with keys just less then these keys.
      right_sibling (LeafNode): leaf node with keys just larger then these keys.
      parent (InternalNode): node which directs queries to this node.
    '''
    self.maxsize = maxsize
    self.minsize = maxsize//2

    self.lsibling = left_sibling
    self.rsibling = right_sibling
    self.parent = parent

    self.keys = array([])
    self.data = array([])

  def display(self):
    ''' Return string of contents '''
    return ' _ '.join(self.keys.astype(int).astype(str))

  def append_edgelist(self):
    ''' Internal function for generating Graphviz tree.'''
    return [(
        Node(self.display(),shape='house',fontname='monospace'),
        Node(' _ '.join(self.data.astype(str)),shape='rectangle',fontname='monospace')
      )]

  def insert(self,key,value):
    ''' Insert a value to this node.
    Args:
      key (orderable): label for the data.
      value: Data to be stored.
    '''
    place = (self.keys < key).sum()

    # Normal insertion. TODO should insert after split for small speedup.
    if place < self.keys.shape[0] and key == self.keys[place]:
      self.data[place] = value
    else:
      self.keys = concatenate((self.keys[:place],array([key]),self.keys[place:]))
      self.data = concatenate((self.data[:place],array([value]),self.data[place:]))

    # Case: split required.
    if self.keys.shape[0] > self.maxsize:
      median = self.keys.shape[0]//2
      if self.parent is None:
        #print("Root leaf split.")
        self.parent = InternalNode(self.maxsize,parent=None)
        self.parent.children = array([self])

      # Make new leaf and divide data correctly.
      newleft = LeafNode(
          self.maxsize,
          left_sibling=self.lsibling,
          right_sibling=self,
          parent=self.parent
        )
      if self.lsibling is not None:
        self.lsibling.rsibling = newleft
      self.lsibling = newleft

      newleft.keys = self.keys[:median]
      newleft.data = self.data[:median]
      self.keys = self.keys[median:]
      self.data = self.data[median:]

      # Update above tree.
      self.parent.birth(self.keys[0],newleft)

  def query(self,key):
    ''' Find the data associated with key in the structure. '''
    place = (self.keys < key).sum()
    if place < self.keys.shape[0] and self.keys[place] == key:
      return self.data[place]
    else:
      return None

  def remove(self,key):
    ''' Find the data associated with key, delete it and the key from the tree.
    Args:
      key (orderable): label for the data.
    Returns:
      data associated with key.
    '''
    place = (self.keys < key).sum()

    if place > self.keys.shape[0] or self.keys[place] != key:
      return 

    self.keys = concatenate((self.keys[:place],self.keys[place+1:]))
    self.data = concatenate((self.data[:place],self.data[place+1:]))

    if self.parent is None:
      return 

    parplace = (self.parent.keys <= key).sum()

    # If size is below minimum and not root.
    if self.keys.shape[0] < self.minsize:
      if parplace+1 < self.parent.children.shape and \
          self.parent.children[parplace+1].keys.shape[0] > self.parent.children[parplace+1].minsize:
        print("Rotating from right.")
        self.rotate_right(parplace)
      elif parplace != 0 and \
          self.parent.children[parplace-1].keys.shape[0] > self.parent.children[parplace-1].minsize:
        print("Rotating from left.")
        self.rotate_left(parplace)
      elif parplace+1 < self.parent.children.shape:
        print("Merging right.")
        self.merge_right(parplace)
      elif parplace != self.parent.children.shape:
        print("Merging left.")
        self.merge_left(parplace)
      else:
        raise AssertionError("Must either have siblings or be root. Fuck off!")
    elif parplace > 0 and place == 0:
      # Update parent key.
      self.parent.keys[parplace-1] = self.keys[0]

  def rotate_right(self,parplace):
    ''' Take a key from a right neighbor.
    Args:
      parplace (int): index of self in parent.
    '''
    right = self.parent.children[parplace+1]

    # Copy data over.
    self.keys = concatenate((self.keys,array([right.keys[0]])))
    self.data = concatenate((self.data,array([right.data[0]])))

    # Update parent key for right.
    self.parent.keys[parplace] = right.keys[1]

    # Remove data from right.
    right.keys = right.keys[1:]
    right.data = right.data[1:]

  def rotate_left(self,parplace):
    ''' Take a key from a left sibling.
    Args:
      parplace (int): index of self in parent.
    '''
    # Copy data over.
    left = self.parent.children[parplace-1]
    self.keys = concatenate((array([left.keys[-1]]),self.keys))
    self.data = concatenate((array([left.data[-1]]),self.data))

    # Update parent key for self.
    self.parent.keys[parplace-1] = self.keys[0]

    # Remove data from left.
    left.keys = left.keys[:-1]
    left.data = left.data[:-1]

  def merge_right(self,parplace):
    ''' Merge with right sibling.'''
    right = self.parent.children[parplace+1]

    self.keys = concatenate((self.keys,right.keys))
    self.data = concatenate((self.data,right.data))
    self.rsibling = right.rsibling

    self.parent.filicide(parplace+1)

  def merge_left(self,parplace):
    ''' Merge with left sibling.'''
    left = self.parent.children[parplace-1]

    left.keys = concatenate((left.keys,self.keys))
    left.data = concatenate((left.data,self.data))
    left.rsibling = self.rsibling

    self.parent.filicide(parplace)

if __name__=='__main__':
  main()
