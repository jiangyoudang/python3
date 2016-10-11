
lalala = '--------------------lalala--------------------'
class treeNode():

  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def __str__(self):
    return 'treeNode: {}'.format(self.val)


def test_tree():
  tree = {i:treeNode(i) for i in range(1,12)}
  tree[1].left = tree[2]
  tree[1].right = tree[3]
  tree[2].left = tree[4]
  tree[2].right = tree[6]
  tree[4].left = tree[5]
  tree[4].right= tree[11]
  tree[6].right = tree[7]
  tree[3].left = tree[8]
  tree[8].right = tree[10]
  tree[8].left = tree[9]

  return tree[1]


def dep(root):
  if not root:
    return 0
  return max(dep(root.left), dep(root.right)) + 1


# def prettyBST(root, sep = ' '):
#     if not root:
#         return ''
#     curr_level = [root]
#     next_level = []
#     h = dep(root)
#     space_length = (1 << h) - 1
#     while curr_level:
#         if not any(curr_level):
#             break
#
#         print(sep*(space_length>>1), end = '')
#         for i, node in enumerate(curr_level):
#             if i == len(curr_level)-1:
#                 space_length >>= 1
#             if not node:
#                 print(sep, end='')
#
#                 next_level.append(None)
#                 next_level.append(None)
#             else:
#                 print(node.val, end='')
#                 next_level.append(node.left)
#                 next_level.append(node.right)
#             print(sep*space_length, end = '')
#
#         print('')
#
#
#         curr_level = next_level
#         next_level = []

def prettyBST(root, sep = ' '):
  h = dep(root)
  w = (1 << h) - 1
  matrix = [[' ' for i in range(w)] for j in range(h)]
  _printdfs(root, 0, w-1, 0, matrix)
  for i in range(h):
    print(''.join(matrix[i]))

def _printdfs(root, left, right, h, matrix):
  if not root:
    return
  mid = (left + right) // 2
  matrix[h][mid] = str(root.val)
  _printdfs(root.left, left, mid-1, h+1, matrix)
  _printdfs(root.right, mid+1, right, h+1, matrix)


def levelTravese(root, lel, num, res, num_len):
  # num: [&]
  if not root:
    return
  if lel == len(res):
    res.append('')
  levelTravese(root.left, lel+1, num, res, num_len)
  str_node = str(root.val)
  res[lel] = res[lel] + ' '* (num_len * num[0] - len(res[lel])) + str_node
  num[0] += 1
  levelTravese(root.right, lel + 1, num, res, num_len)

def treePrint(root, num_len = 2):
  res = []
  levelTravese(root, 0, [0], res, num_len)
  for line in res:
    print(line)

if __name__ == '__main__':

  root = test_tree()
  treePrint(root)
  print(lalala)
  treePrint(root, 4)
  print(lalala)
  prettyBST(root)





