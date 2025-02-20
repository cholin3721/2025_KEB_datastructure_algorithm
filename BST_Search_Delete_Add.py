class TreeNode :
    def __init__(self, data):
        self.left_child = None
        self.right_child = None
        self.data = data


    def __str__(self):
        return self.data


# def set_tree(current, data_list) :
#     data_list_copy = data_list[:]
#     if data_list_copy :
#         data_list_copy.sort()
#         num = data_list_copy[len(data_list_copy)//2]
#         current = TreeNode(num)
#         data_list_copy.remove(num)
#
#         if num < current.data :
#             current.left_child = TreeNode(num)
#             set_tree(current.left_child, data_list_copy)
#         else :
#             current.right_child = TreeNode(num)
#             set_tree(current.right_child, data_list_copy)
#     return
#  내 코드


def set_tree(current, data_list):
    if not data_list:
        return

    data_list.sort()  # 데이터 정렬
    mid = len(data_list) // 2
    num = data_list[mid]

    current.data = num  # 현재 노드에 값 설정
    left_list = data_list[:mid]  # 왼쪽 서브트리 데이터
    right_list = data_list[mid + 1:]  # 오른쪽 서브트리 데이터

    # 왼쪽 자식 노드 생성 및 재귀 호출
    if left_list:
        current.left_child = TreeNode(None)  # 빈 노드 생성
        set_tree(current.left_child, left_list)

    # 오른쪽 자식 노드 생성 및 재귀 호출
    if right_list:
        current.right_child = TreeNode(None)  # 빈 노드 생성
        set_tree(current.right_child, right_list)

    #gpt 코드

def pre_set_tree(data_list) :
    return list(set(data_list))


def print_tree(select, root):
    if select == 1 :
        # plr
        if root is None :
            return
        print(root.data)
        print_tree(1,root.left_child)
        print_tree(1, root.right_child)
    elif select == 2:
        # lpr
        if root is None :
            return
        print_tree(2,root.left_child)
        print(root.data)
        print_tree(2,root.right_child)
    elif select == 3:
        # lrp
        if root is None :
            return
        print_tree(3,root.left_child)
        print_tree(3,root.right_child)
        print(root.data)
    else :
        print("잘못 입력하셨습니다!")

def search_tree(root) :
    find_num = int(input())
    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group}을(를) 찾았습니다")
            break
        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_group}이(가) 존재하지 않습니다")
                break
            current = current.right



if __name__ == "__main__" :
    a = [35, 64, 23, 72, 24]
    b = a[:]