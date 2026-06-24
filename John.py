i=input("Enter your name: ");
i=i.lower();
i=i[0].upper() + i[1:];
not_john=[];
while i != "John":
    not_john.append(i);
    i=input("Enter your name: ");
    i=i.lower();
    i=i[0].upper() + i[1:];


print(f'Incorrect names: {not_john}');