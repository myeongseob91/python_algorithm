count = 0
dx = ['a','b','c','d','e','f','g','h']
dy = ['1','2','3','4','5','6','7','8']


string = input()
ix = string[0]
iy = string[1]

sx =dx.index(ix)
sy =dy.index(iy)

if (0 <= sx-2 < 8) and (0 <= sy-1 < 8):
    count = count+1

if (0 <= sx-2 < 8) and (0 <= sy+1 < 8):
    count = count+1

if (0 <= sx+2 < 8) and (0 <= sy-1 < 8):
    count = count+1

if (0 <= sx+2 < 8) and (0 <= sy+1 < 8):
    count = count+1

#
if (0 <= sx-1 < 8) and (0 <= sy-2 < 8):
    count = count+1

if (0 <= sx+1 < 8) and (0 <= sy-2 < 8):
    count = count+1

if (0 <= sx-1 < 8) and (0 <= sy+2 < 8):
    count = count+1

if (0 <= sx+1 < 8) and (0 <= sy+2 < 8):
    count = count+1

print(count)








# 수평2 / 수직1
# 수직2 / 수평1


###   a   b   c   d   e   f   g   h
# 1 (1,a)

# 2

# 3

# 4

# 5

# 6

# 7

# 8
