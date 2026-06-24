start_string=input("Please enter string: ");
upper_first=list(start_string);
lower_first=list(start_string);
lower_counter=0;
for i in range(len(start_string)):
    if i%2==0:
        upper_first[i]=start_string[i].upper();
        
    else:
        upper_first[i]=start_string[i].lower();
    
    if lower_first[i]==" ":
        lower_counter+=1;
    
    if lower_counter%2==0:
        lower_first[i]=start_string[i].lower();  
      
    else:
        lower_first[i]=start_string[i].upper();
print("".join(upper_first));
print("".join(lower_first));