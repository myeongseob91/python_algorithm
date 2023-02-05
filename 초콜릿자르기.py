N,M = map(int, input().split(" "));
S = 0;

if M>=N:
    S = S+(N-1)

for i in range(0, M):
    S = S+(N-1)

print(S)

#답은 잘나오는데 채점은 틀림.

# if N>=N :
#     S = S+(N-1)

# for i in range(0, M):
#     S = S+(N-1)
 
# print(S)

