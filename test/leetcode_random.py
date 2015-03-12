import random

done_filename = '已做'
todo_filename = '未做'

done_list = []
todo_list = []

def write_file(dl, tl):
    with open(done_filename,'w') as df:
        if not dl:
            df.write('')

        for i in dl:
            df.write('{} '.format(i))

    with open(todo_filename, 'w') as tf:
        for i in tl:
            tf.write('{} '.format(i))


def init(dl, tl):
    with open(done_filename) as df:
        done = df.read()
    dl += done.split()
    with open(todo_filename) as tf:
        todo = tf.read()
    tl += todo.split()


def random2_gen(td_list):
    questions = random.sample(td_list,2)
    return questions



# write_file([], list(range(1,180)))
init(done_list, todo_list)
random2_gen(todo_list)

while True:
    do_now = random2_gen(todo_list)
    print('今天做 {d[0]} 和 {d[1]} '.format(d=do_now))
    c = input("y/n or q(quit)  ")
    if c=='q':
        break
    elif c=='y':
        done_list += do_now
        todo_list.remove(do_now[0])
        todo_list.remove(do_now[1])
        write_file(done_list, todo_list)
        break