lst = [10,20, 30, 30, 10, 30, 20, 20,10,20,30,40,50,60,70,80,90]
d_list = [None]

for ele1 in range(len(lst)):
    flag = True
    for ele2 in range(len(d_list)):
        if lst[ele1] == d_list[ele2]:
            flag = True
            break
        else:
            flag = False
    if flag == False:
        # d_list.append(lst[ele1])
        d_list = d_list + [lst[ele1]]
    if d_list[0] == None:
        d_list.remove(None)

# print(d_list)


set_1 = {1, 'dileep', 'dasari', 2, 5, 'mahesh', 4, 5, 6, 7}

print(set_1)




