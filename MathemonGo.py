import random
import time
import sys
import math


def output(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    input()


level = 1
mathemons = ["Addy", "Minusy", "Multiman", "Divi", "Expo", "Sqrt", "Witz", "Hades", "Combato", "Arceus",  "Mathmew"]
available = mathemons[0:4]
description = {
    "Addy": "The god of addition, combines substances.",
    "Minusy": "The god of subtraction, decomposes substances.",
    "Multiman": "The god of multiplication, multiplies substances.",
    "Divi": "The god of division, splits substances.",
    "Expo": "The god of exponential functions, has the power to repeatedly multiply substances.",
    "Sqrt": "The god of square roots, has the power to perform the inverse operation of Expo.",
    "Combato": "The mightiest of all gods.",
    "Witz": "The king of the gods.",
    "Hades": "The king of the devil.",
    "Arceus": "The absolute god of the gods.",
    "Mathmew": "The artificial Mathemon, the second strongest (besides Arceus and hades)."
}
mine = []
coins = 0
xp = 0
questions = ["math.sqrt(100)", "math.sqrt(100) + 200", "100 + 300", "123 + 877", "120 + 523", "10 * 100", "120 * 5",
             "9*5", "math.sqrt(9)", "math.sqrt(121)", "1 / 100", "1 / 1", "500 / 1", "200 / 100", "10000 / 1000",
             "1000 + 200 / 2"]
print('''In this wild and mysterious world...
Everyone wants to be the very best.
You are 14, which is finally legal in stepping on your first adventure...
(PRESS ENTER TO CONTINUE IN EACH PROMPT)''')
output("You walk into a laboratory which your mother told you to.")
output("Oak: Hello there!")
output('Oak: Welcome to the world of Mathemon!')
output('Oak: My name is Oak!')
output('Oak: People call me the Mathemon professor!')
output('Oak: This world is inhabited by creatures called Mathemon!')
output('Oak: For some people, Mathemon are pets.')
output('Oak: Others use them for fights.')
output('Oak: Myself...')
output('Oak: I study Mathemon as a profession.')
output('Oak: First, what is your name? Say it.')
username = input()
output(f'Oak: Oh. Your name is {username}. Interesting.')
output('Oak: The first Mathemon you could get is in my laboratory.')
output("Oak: Let me go into the laboratory and look.")
output(f"Oak: Hmm... Seems like I have {len(available)} options: ")
for i in range(len(available)):
    output(f"{i + 1}. {available[i]}")
output("Oak: Which one would you like? Enter the index.")
idx = int(input())
mine.append(mathemons[idx - 1])
output(f"Oak: Great.")
output(f"You retrieved your first Mathemon: {mine[0]}.")
coins += 10
xp += 100
level = len(mine) // 5 + 1
output(f"You are now at level {level}.")
output("Oak: However, that is just part of the adventure.")
output("Oak: Next, you should get your Mathedex.")
output("Oak: COME OUT DEX!")
output("A weird creature appears from the sky.")
time.sleep(1)
output("Dex: SYSTEM INITIALIZATION FINISHED.")
output("Dex: USER CONFIRMATION EXECUTING...")
output(f"Dex: SUCCESS! DETECTED {username}.")
output("Dex: HELLO, I AM YOUR ROBOTIC ASSISTANT.")
output("Dex: LATER, YOU CAN RELY ON ME FOR PROVIDING USEFUL INFORMATION ON THE MATHEMON.")
output("Dex: LET'S BEGIN ON THE ADVENTURE!")
output("Oak: Bye-bye! Be careful!")
output("You left the laboratory.")
output("Dex: MAY US GOOD LUCK!")
output("Dex: RATHER THAN FIGHTING, WE WILL BE ASKED MATH QUESTIONS.")
output("DEX: EXPLORATION MODE!")
cmd = input("Enter command (Type \"documentation\" for further details): ")
state = 0
while True:
    if cmd == 'exit':
        output("Dex: Are you sure you want to exit (Y/N)? This can't be undone and all your progress might be lost.")
        if input() == 'Y':
            output("Dex: OK. Bye!")
            break
        else:
            output("Dex: I know you won't.")
    elif cmd == 'profile':
        output(f"User {username}: currently at level {level}, has buddy {mine[0]}, has {xp}xp experience, and has "
               f"Mathemons {', '.join(mine)}.")
    elif cmd == 'current mathemons':
        output(f"You have {', '.join(mine)}.")
    elif cmd == 'documentation':
        output("Available commands: exchange, exit, play, profile, current mathemons, travel, examine, xp, coins, "
               "shop, level")
        output('exit: terminates this game.')
        output('profile: displays current profile.')
        output('current mathemons: displays current Mathemon.')
        output('travel: travels to a new location.')
        output('examine: checks the mathemons in this area.')
        output('play: plays with your buddy.')
        output('exchange: changes your buddy.')
        output('Other commands are for fetching particular fields in this game.')
    elif cmd == 'exchange':
        output('Do you really desire to exchange your buddy (Y/N)?')
        state = input()
        if state == 'Y':
            output('OK. Then which the following Mathemons do you want to exchange your buddy with?')
            for i in range(1, len(mine)):
                output(f'{i + 1}. {mine[i]}')
            output('Enter the index below.')
            idx = int(input())
            if idx == 1:
                output('Cannot swap buddy with buddy.')
                continue
            else:
                idx -= 1
                tmp = mine[0]
                mine[0] = mine[idx]
                mine[idx] = tmp
                output(f'You must carefully preserve this mathemon: {mine[0]}!')
                output(f'{mine[0]} is now your buddy!')
    elif cmd == 'play':
        buddy = mine[0]
        output(f'Go {buddy}!')
        output('Let us have some great playing!')
        output('[Playing]')
        time.sleep(10)
        output(f'{buddy}: (giggle)')
        output('You gained 20 coins!')
        output('Also earned 100xp experience!')
        coins += 20
        xp += 100
    elif cmd == "level":
        output(f"You are at level {level}.")
    elif cmd == "shop":
        output("You walked into a shop.")
        output("Boss: Welcome! Do you want to retrieve mathemons by paying me?")
        output("Boss: All right!")
        output("Boss: Look up.")
        output("You see...")
        print('''
        SHOP ITEM SHOWN BELOW:
        * Regional mathemons (i.e. random mathemons except hades and witz and Mathmew): POKE$10
        ''')
        output("Boss: Do you desire to pay (Y/N)? Enter it below.")
        choice = input()
        if choice == "Y":
            output("Boss: Great!")
            new = random.choice(mathemons[0:6])
            output("Boss: Let me check your credit card.")
            if coins < 10:
                output("Boss: You don't even have enough dollars! Get out from here!")
            else:
                output(f"Boss: Great. Here is {new}.")
                output(f'You retrieved {new}.')
                coins -= 10
                mine.append(new)
                level = len(mine) // 5 + 1
                output(f"You are now at level {level}.")
                output("Boss: Bye!")
        else:
            output("Boss: OK. Bye!")
    elif cmd == "coins":
        output(f"You have POKE${coins} dollars.")
    elif cmd == "xp":
        output(f"You have {xp}xp experience.")
    elif cmd == 'travel':
        state = random.randint(0, 1)
        output("Travelled!")
    elif cmd == 'examine':
        if state == 0:
            output("You see no Mathemons...")
        else:
            output("You see a lot of Mathemons, including:")
            regional = random.sample(mathemons, 3)
            for i in range(len(regional)):
                output(f'{i + 1}. {regional[i]}: {description[regional[i]]}')
            output("Which do you desire to catch? Enter the index.")
            idx = int(input())
            current = regional[idx - 1]
            output(f"{current} requests a Mathemon battle!")
            output(f"Go {mine[0]}!")
            question = random.choice(questions)
            output(f"{current} asks, {question} = ___")
            answer = eval(question)
            output("Enter your answer below.")
            ans = float(input("Answer: "))
            if answer == ans:
                output("It is super effective!")
                output(f"... {current} fainted.")
                mine.append(current)
                output("Mathemon added to your mathemon collection.")
                coins += 10
                xp += 100
                level = len(mine) // 5 + 1
                output(f"You are now at level {level}.")
                output("You received POKE$10 dollars as reward.")
                output("You also earned 100xp.")
            else:
                output("There is no effect!")
                output(f"Oh no! {current} escaped!")
    else:
        output("Invalid command.")
    cmd = input("Enter command (Type \"documentation\" for further details): ")
