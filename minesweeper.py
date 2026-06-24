minefield=[["-","-","-","#","#"],
           ["-","#","-","-","-"],
           ["-","-","#","-","-"],
           ["-","#","#","-","-"],
           ["-","-","-","-","-"]];

def count_mines(minefield):
    for i in range(len(minefield)):
        for j in range(len(minefield[i])):
            if minefield[i][j]=="-":
                count=0;
                for k in range(-1,2):
                    for l in range(-1,2):
                        if i+k>=0 and i+k<len(minefield) and j+l>=0 and j+l<len(minefield[i]):
                            if minefield[i+k][j+l]=="#":
                                count+=1;
                minefield[i][j]=count;
    for i in minefield:
        print(*i);

count_mines(minefield);