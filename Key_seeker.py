import random


x=0
y=0

attemps = 0

player_position = (x,y)

key_x = random.randint(0,10)  
key_y = random.randint(0,10)  

key_position = (key_x, key_y)

while key_position == (0,0):
    key_x = random.randint(0,10)  
    key_y = random.randint(0,10)  
    key_position = (key_x, key_y)



print("In this game you will try to find a key in a dark room. Use the WSAD keys to move around, good luck!")
any_key = str(input("press any key to start \n"))


while player_position != key_position:
    buttom = str(input(">>"))
    buttom = buttom.upper()
    if buttom == "W":
        x += 1
        attemps += 1
    if buttom == "S":
        x -= 1
        attemps += 1
    if buttom == "D":
        y += 1
        attemps += 1
    if buttom == "A":
        y -= 1
        attemps += 1
    if buttom != "W" and buttom != "S" and buttom != "A" and buttom != "D":
        print("Bad command!")
    if x < 0 or x > 10 or y < 0 or y > 10:
        print("wrong move, you got off the map")
        if x > 10:
            x-=1
        if x < 0:
            x+=1
        if y > 10:
            y-=1
        if y < 0:
            y+=1
    if buttom == "W" or buttom == "S" or buttom == "A" or buttom == "D":
        player_position = (x,y)
        print("your position is: " ,player_position)

print("Great you got the key!")
print("You needed " , attemps , " moves for that")
