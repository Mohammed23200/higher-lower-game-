import art
import gamedata
import random

score = 0
isEnd = True



def high_low(first, second, state):
    print(art.logo)
    global score
    if state.upper() == 'A':
        if first >= second:
            score += 1
            return True
        else:
            print(f"\nYou are Wrong ❌\nYour final score is: {score}")
            return False
    elif state.upper() == 'B':
        if second >= first:
            score += 1
            return True
        else:
            print(f"\nYou are Wrong ❌\nYour final score is: {score}")
            return False
    else:
        print("Invalid input. Please type 'A' or 'B'.")
        return True 

randomone1 = random.randint(0, len(gamedata.data) - 1)
randomone2 = random.randint(0, len(gamedata.data) - 1)
while randomone2 == randomone1:
    randomone2 = random.randint(0, len(gamedata.data) - 1)

current = randomone1

while isEnd:
    next_one = randomone2

    person1 = gamedata.data[current]
    person2 = gamedata.data[next_one]

    print(f"\nCompare A: {person1['name']}, {person1['description']}, from {person1['country']}")
    print(art.vs)
    print(f"Compare B: {person2['name']}, {person2['description']}, from {person2['country']}")

    answer = input("Who has more followers? Type 'A' or 'B': ")

    isEnd = high_low(person1['follower_count'], person2['follower_count'], answer)

    if isEnd:
        print(f"✅ Correct! Current score: {score}")
        if (answer.upper() == 'A' and person1['follower_count'] >= person2['follower_count']) or \
           (answer.upper() == 'B' and person2['follower_count'] >= person1['follower_count']):
            current = current if answer.upper() == 'A' else next_one

        randomone2 = random.randint(0, len(gamedata.data) - 1)
        while randomone2 == current:
            randomone2 = random.randint(0, len(gamedata.data) - 1)
