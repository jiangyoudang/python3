

def rm_cmnts(i_file):
    #open file
    with open(i_file) as text:
        #match /* and the first */, ignore any /* between
        # left indicates if there is */ ongoing
        left = False
        for line in text:
            # repeatedly check
            while True:
                # no comment so far
                if not left:
                    if '/*' not in line:
                        print(line, end='')
                        break
                    else:
                        left = True
                        index = line.find('/*')
                        print(line[:index], end='')
                # To find end of comment
                if left:
                    if '*/' in line:
                        index = line.find('*/')
                        line = line[index+2:]
                        left = False
                        same_line = True
                    else:
                        break
         #change line
            print()


rm_cmnts('./rm_comment.c')

