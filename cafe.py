menu=['coffee','tea','muffin','sandwich'];
stock={'coffee':7,
       'tea':7,
       'muffin':7,
       'sandwich':7};
price={'coffee':7,
       'tea':7,
       'muffin':7,
       'sandwich':7};
total_stock=0;
for i in range(len(menu)):
    total_stock+=price[menu[i]]*stock[menu[i]];
print(f'Total worth of stock: {total_stock}');