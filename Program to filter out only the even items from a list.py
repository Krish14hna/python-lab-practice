my_list = list(map(int,input().split()))

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)