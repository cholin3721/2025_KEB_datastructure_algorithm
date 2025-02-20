class TreeNode :
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data


    def __str__(self):
        return self.data


def set_root(data_list) :
    if data_list :
        data_list = list(set(data_list))
        data_list.sort()
        data_list = [TreeNode(data) for data in data_list]
        i = len(data_list) // 2
        root = data_list[i]
        left_list = data_list[:i]
        right_list = data_list[i+1:]
        data_list.remove(root)
        return root, left_list, right_list
    else :
        print("데이터 셋이 비어있습니다.")


def set_Tree(root, left_list, right_list) :
    if left_list :
        for data in left_list :
            if root.data > data.data :
                root.left_child = data
                left_list.remove(data)
                set_Tree(root.left_child, left_list, right_list)
            else :
                root.right_child = data
                right_list.remove(data)
                set_Tree(root.right_child, left_list, right_list)

    if right_list :
        for data in right_list :
            if root.data > data.data :
                root.left_child = data
                left_list.remove(data)
                set_Tree(root.left_child, left_list, right_list)
            else :
                root.right_child = data
                right_list.remove(data)
                set_Tree(root.right_child, left_list, right_list)





if __name__ == "__main__" :
    num_list = [10, 15, 8, 7, 12]
    root, left, right = set_root(num_list)
    set_Tree(root, left, right)