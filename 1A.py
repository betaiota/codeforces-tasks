initials = [int(i) for i in input().split()]

horizontal=0
vertical=0
sqsd=0

while(sqsd < initials[0]):
    horizontal+=1
    sqsd+=4
while(initials[2] < initials[1]):
    vertical+=1
    sqsd+=4

print(horizontal, vertical)
final = horizontal + vertical
print(final)