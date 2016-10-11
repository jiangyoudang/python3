# -*- coding utf-8 -*-
__author__ = 'congliu'


from random import randint

a = [randint(1,100) for i in range(50)]


def sift_down(a, start, end):
  root = start
  while True:
    child = 2*root + 1
    if child > end:
      break
    if child+1 <=end and a[child] < a[child+1]:
      child = child+1
    if a[root] < a[child]:
      a[root],a[child] = a[child], a[root]
      root = child
    else:
      break

def heapify(a):
  for start in range((len(a)-2)//2,-1,-1):
    sift_down(a,start,len(a)-1)

def heap_sort(a):
  heapify(a)
  for end in range(len(a)-1,0,-1):
    a[0],a[end] = a[end],a[0]
    sift_down(a,0,end-1)
  return a

print(heap_sort(a))



############################################################
import heapq

class HuffNode:

  def __init__(self, freq, key=None):
    self.freq = freq
    self.key = key
    self.left = self.right = None


def huffman(data):
  h = []
  for key in data:
    freq = data[key]
    heapq.heappush(h, (freq, HuffNode(freq, key)))

  while len(h) > 1:
    left = heapq.heappop(h)
    right = heapq.heappop(h)

    freq = left[0] + right[0]

    new_node = HuffNode(freq)
    new_node.left = left[1]
    new_node.right = right[1]

    heapq.heappush(h, (freq, new_node))

  result = {}
  getResult(new_node, result, '')
  return result

def getResult(root, result, path):
  if not root.left and not root.right:
    result[root.key] = path
    return
  if root.left:
    getResult(root.left, result, path+'0')
  if root.right:
    getResult(root.right, result, path+'1')



data = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
print(huffman(data))

