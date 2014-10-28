class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path_list = path.split('/')
        simp_path = []
        for dir in path_list:
            if dir == '.' or not dir: continue
            elif dir == '..':
                if simp_path:
                    simp_path.pop()
            else:
                simp_path.append(dir)

        return '/' + '/'.join(simp_path)
