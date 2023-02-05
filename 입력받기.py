#잘못된 예시
# items = input().split();

# item_a = items[0];
# item_b = items[1];
# item_c = items[2];
# item_d = items[3];
# item_e = items[4];

#올바른 예시
a,b = map(int,input().split(" "))
print(a / b)