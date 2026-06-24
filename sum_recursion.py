def adding_up_to(int_list, index):
    if index < 0:
        return 0;
    else:
        return int_list[index] + adding_up_to(int_list, index - 1);

my_list = [1, 2, 3, 4, 5];
print(adding_up_to(my_list, len(my_list) - 1));