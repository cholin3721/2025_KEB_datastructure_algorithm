class TreeNode:
    def __init__(self):
        self.left = None
        self.data =None
        self.right =None

if __name__ == "__main__" :
    # memory = []
    groups=["블랙핑크", "레드벨벳", "마마무", "에이핑크", "걸스데이", "트와이스"]
    # groups = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = groups[0]
    root = node

    for group in groups[1:]:
        node = TreeNode()
        node.data = group
        current = root

        while True :
            if group < current.data:
                if current.left is None :
                    current.left = node
                    break
                else :
                    current = current.left  # move

            else:
                if current.right is None :
                    current.right = node
                    break
                else :
                    current = current.right  #move

    print("BST 구성완료")


# 사실 이 모든 과정을 함수화해서 설계해야함

    find_group = input("그룹을 입력하시오 : ")

    current = root
    while True:
        if find_group == current.data:
            print(f"{find_group} 을/를 찾았습니다")
            break

        elif find_group < current.data:
            if current.left is None:
                print(f"{find_group} 이/가 존재하지 않습니다")
                break
            else :
                current = current.left

        else :
            if current.right is None:
                print(f"{find_group} 이/가 존재하지 않습니다")
                break
            else :
                current = current.right

    deleteName = input("그룹을 입력하시오 : ")

    current = root
    parent = None
    while True :
        if deleteName == current.data :
            if current.left == None and current.right == None:
                if parent.left == current :
                    parent.left = None
                else :
                    parent.right = None
                del current


            elif current.left != None and current.right == None:
                if parent.left == current:
                    parent.left = current.left
                else :
                    parent.right = current.left
                del current


            elif current.left == None and current.right != None:
                if parent.left == current:
                    parent.left = current.right
                else:
                    parent.right = current.right
            else :
                pass
            # 여기는 과제
            print(f"{deleteName}을 삭제하였습니다.")
            break



        elif deleteName < current.data :
            if current.left is None :
                print(deleteName, " 이/가 없습니다.")
                break
            parent = current
            current = current.left

        else :
            if current.right is None :
                print(deleteName, " 이/가 없습니다.")
                break
            parent = current
            current = current.right

