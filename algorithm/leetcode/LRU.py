class Node(object):
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.pre = None
    self.next = None

class LRUCache(object):
  def __init__(self, capacity):
    """
    :type capacity: int
    """
    self.capacity= capacity
    self.size = 0
    self.cache = {}
    self.head = None
    self.rear = None

  def _update(self, node):
    """Move node to the end of double linked list."""
    _next = node.next
    if _next is None:
      # rear node
      return
    _pre = node.pre
    if _pre is None:
      # head
      _next.pre = None
      self.head = _next
    else:
      _pre.next = _next
      _next.pre = _pre
    self.rear.next = node
    node.pre = self.rear
    self.rear = node

  def get(self, key):
    """
    :rtype: int
    """
    if key in self.cache:
      self._update(self.cache[key])
      return self.cache[key].val
    return -1

  def set(self, key, value):
    """
    :type key: int
    :type value: int
    :rtype: nothing
    """
    if key in self.cache:
      self.cache[key].val = value
      self._update(self.cache[key])
    else:
      new_node = Node(key, value)
      self.cache[key] = new_node
      if self.head is None:
        self.head = new_node
        self.rear = new_node
      else:
        new_node.pre = self.rear
        self.rear.next = new_node
        self.rear = new_node
      if self.capacity == self.size:
        _next = self.head.next
        _next.pre = None
        self.head.next = None
        del self.cache[self.head.key]
        self.head = _next
      else:
        self.size += 1



lru = LRUCache(2)
print(lru.set(1, 2))
print(lru.get(1))
print(lru.set(2, 1))
print(lru.get(2))
print(lru.get(1))
print(lru.rear.valu)
