from threading import Thread
from multiprocessing.dummy import Pool
from datetime import datetime
# import logging
# import sys
# logging.basicConfig(stream=sys.stdout,
#                     level=logging.INFO,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s')


bigNum = 60000000

a = [0]*bigNum
b = [0]*bigNum
c = [0]*bigNum
workers = 2


def worker(array, task_index, task_n, total):
  start_i = task_index*task_n
  end_i = task_index*task_n+task_n
  if end_i > total:
    end_i = total
  for i in range(start_i, end_i):
    array[i] = 2

def check(array, num):
  for i in array:
    if i != num:
      return False
  return True


def f(x):
  return 1

def log_time(f):
  def wrapper(*args, **kwargs):
    start_time = datetime.today()
    f(*args, **kwargs)
    end_time = datetime.today()
    print(end_time-start_time)
  return wrapper

@log_time
def test1(a):
  a = list(map(f, a))

@log_time
def test2(a):
  for i in range(len(a)):
    a[i] = 2

if __name__ == '__main__':

  test1(a)
  test2(c)

  pool = Pool(workers)

  t1 = datetime.today()
  pool.map(f, b)
  print(datetime.today()-t1)







  # threads=[]
  # for i in range(workers):
  #   t = Thread(target=worker, args=(b, i, bigNum//workers+1, bigNum))
  #   threads.append(t)
  #   t.start()
  #
  # for t in threads:
  #   t.join()
  #
  #
  # end_2 = datetime.today()
  #
  # print('t1: {}'.format(end_1-start))
  # print('t2: {}'.format(end_2-end_1))
  #
  # s2 = datetime.today()
  # print(check(a, 1))
  # print(check(b, 2))
  # e2 = datetime.today()
  # print(e2-s2)
