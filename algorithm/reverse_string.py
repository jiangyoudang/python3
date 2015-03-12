
string_list = list('test a string')

def reverse_string(string_list, start, end):
    for i in range((end-start+1)//2):
        temp = string_list[start+i]
        string_list[start+i] = string_list[end-i]
        string_list[end-i] = temp



print(string_list)
reverse_string(string_list, 4, len(string_list)-1)
print(string_list)