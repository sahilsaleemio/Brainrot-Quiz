print("WELCOME TO BRAINROT QUIZ!")

playing = input("Do you want to play? ").lower()
score = 0
if playing != "yes" :
    quit()

print( "YAY!!!, Lets play ")

answer_1 = input("what is the 15% tax on food called? ").lower()

if answer_1 == "fanum tax":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

answer_2 = input("who rizzed up livvy donne? ").lower()

if answer_2 == "baby gronk":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

answer_3 = input("what is that one shake called? ").lower()

if answer_3 == "grimace shake":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")


answer_4 = input("what do you say when someone says something that you dont fully understand? ").lower()

if answer_4 == "what the sigma":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

answer_1 = input("what song was played at brainrot party? ").lower()

if answer_1 == "carnival":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

answer_1 = input("what is the highest level of gyat one can achieve? ").lower()

if answer_1 == "level 10":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

answer_1 = input("whos that streamer who looks like a monkey? ").lower()

if answer_1 == "ishowspeed":
    print("correct, +5000 aura")
    score += 1
else:
    print("incorrect, -5000 aura")

print("you got " + str(score) + " questions right!")
print("you got " + str((score/7) * 100) + "%!")

if score <= 4:
    print("you are a disgrace to the brainrot community")
else:
    print("congrats, you are the real skibidi sigma")