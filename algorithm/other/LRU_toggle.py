class User:
  def __init__(self, name):
    self.name = name
    self.prev = None
    self.next = None


head = User('$')
rear = head
cache = {}


def toggle(user):
  global rear
  global head
  global cache

  if user in cache:
    curr = cache[user]

    prev = curr.prev
    next = curr.next

    if curr == rear:
      rear = prev
    else:
      next.prev = prev
    prev.next = next

    del cache[user]

  else:
    curr = User(user)
    cache[user] = curr
    curr.prev = rear
    rear.next = curr
    rear = curr



def contains(user):
  global cache
  return user in cache


def printList():
  global head
  mover = head.next
  users = []
  while mover:
    users.append(mover.name)
    mover = mover.next

  return users


if __name__ == '__main__':
  toggle('user1')
  toggle('user2')
  toggle('user1')
  print(contains('user1') == False)
  toggle('user1')
  print(printList())
  toggle('user1')
  toggle('user2')
  print(printList())