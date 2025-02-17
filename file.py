students = []
try:
    file = input("file name : ")
    fp = open(file, 'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split("_")
    print(readme_list)

except FileNotFoundError as err :
    print(f"{err}")


fp.close()