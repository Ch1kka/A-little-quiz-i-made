import sys
import random
from time import sleep


score = 0
selected_answer=0

print 'Hello! Whats your name?\n'
user_name = raw_input()
print 'Hello ' + user_name + ', your about to get tested for which bending element is the best for you. would you like to proceed?\n'
print '1 = Yes 2 = No : '
raw_input()
sleep(2)
print 'I dont really care what you selected :-), your going to get tested anyways'
sleep(2)
print 'Get ready for the first question good luck!'
sleep(2)
## Question 1
print 'Question 1#: Whats your favorite season?'
sleep(1)
print '1: Autumn'
sleep(0.1)
print '2: Spring'
sleep(0.1)
print '3: Summer'
sleep(0.1)
print '4: Monsoon'
sleep(0.1)
print '5: Winter'
selected_answer = int(raw_input())
score_add = [0,40,20,10,30,50]
score += score_add[selected_answer]

## Question 2
print 'Question 2#: What is your battle tactic'
sleep(1)
print '1: Evasive and defensive'
sleep(0.1)
print '2: Using others strength against them'
sleep(0.1)
print '3: Attack! i dont need to defend'
sleep(0.1)
print '4: Balance both defence and attack'
sleep(0.1)
print '5: tricks'
selected_answer = int(raw_input())
score_add=[0,40,30,10,20,50]
score += score_add[selected_answer]

## Question 3
print 'Question 3#: Whats your animal counterpart?'
sleep(1)
print '1: Dragon'
sleep(0.1)
print '2: Dolphin'
sleep(0.1)
print '3: Lion'
sleep(0.1)
print '4: Bear'
sleep(0.1)
print '5: Turtle'
selected_answer = int(raw_input())
score_add=[0,10,30,40,20,50]
score += score_add[selected_answer]

## Question 4
print 'Question 4#: Which of the following philosophies is most like your own?'
sleep(1)
print '1: if first you dont succed, try again'
sleep(0.1)
print '2: Might is right'
sleep(0.1)
print '3: Just go with the flow'
sleep(0.1)
print '4: Forgive and forget'
sleep(0.1)
print '5: Where theres a will, theres a way'
selected_answer = int(raw_input())
score_add = [0,20,10,30,40,50]
score += score_add[selected_answer]

## Question 5
print 'Question 5#: What is the best way to resolve a situation?'
sleep(1)
print '1: Love and peace'
sleep(0.1)
print '2: Fight'
sleep(0.1)
print '3: Walking away from the problem'
sleep(0.1)
print '4: Waiting for it to settle itself'
sleep(0.1)
print '5: Communication and understanding'
selected_answer = int(raw_input())
score_add = [0,40,10,50,20,30]
score += score_add[selected_answer]

##Question 6
print 'Question 6#: How would you describe yourself?'
sleep(1)
print '1: Free-spritied'
sleep(0.1)
print '2: dependable'
sleep(0.1)
print '3: Focused'
sleep(0.1)
print '4: passionate'
sleep(0.1)
print '5: Dynamic'
selected_answer = int(raw_input())
score_add = [0,40,20,50,10,30]
score += score_add[selected_answer]

## Question 7
print 'Question 7#: Pick a color...'
sleep(1)
print '1: Yellow'
sleep(0.1)
print '2: White'
sleep(0.1)
print '3: Red'
sleep(0.1)
print '4: Blue'
sleep(0.1)
print '5: Grey'
selected_answer = int(raw_input())
score_add = [0,50,40,10,30,20]
score += score_add[selected_answer]

##Question 8
print 'Question 8#: What do you value most?'
sleep(1)
print '1: Willpower'
sleep(0.1)
print '2: Stability'
sleep(0.1)
print '3: Freedom'
sleep(0.1)
print '4: Power'
sleep(0.1)
print '5: Harmony'
selected_answer = int(raw_input())
score_add = [0,50,20,40,10,30]
score += score_add[selected_answer]
sleep(0.5)
print 'Your close to the end of the quiz :D'

##Question 9
print 'Question 9#: In a group your...'
sleep(1)
print '1: A peacemaker'
sleep(0.1)
print '2: A leader'
sleep(0.1)
print '3: The smart problem-solver'
sleep(0.1)
print '4: A clown'
sleep(0.1)
print '5: The goodfy and moody one'
selected_answer = int(raw_input())
score_add = [0,40,50,30,20,10]
score += score_add[selected_answer]
sleep(0.5)
print 'So close!'

##Question 10
print 'Question 10#: Which of the following is most important in a fight?'
sleep(1)
print '1: Speed'
sleep(0.1)
print '2: Strength'
sleep(0.1)
print '3: Balance'
sleep(0.1)
print '4: Flexibility'
sleep(0.1)
print '5: Accuracy'
selected_answer = int(raw_input())
score_add = [0,40,10,20,30,50]
score += score_add[selected_answer]
sleep(1.5)

print 'Ok, the quiz is over! we found out which bender are you!'
sleep(0.5)
print 'You are'
sleep(1.5)

if score>=100 and score<=160:
    print ' a Firebender!!\n\n'
    sleep(0.5)
    print 'Fire is the element of power\n' \
          'and the most aggresive bending art.\n' \
          'Firebenders are genrally strong willed,' \
          'short tempered and driven by emotion'

if score>=161 and score<=250:
    print ' an Earthbender!!\n\n'
    sleep(0.5)

    print 'Earth is the element of\n' \
          'substance, stability and strength.\n' \
          'Earthbenders have unmovable will and nerves of steel. no one gets in their way\n'

if score>= 251 and score<=330:
    print ' a Waterbender!!\n\n'
    print 'Water is the element of change and growth.\n' \
          'Waterbenders are generally gentle, resourceful and sensitive.\n' \
          'Powerful waterbenders are even capable of bending blood!\n'

if score>=331 and score<920:
    print ' an Airbender!!\n\n'
    sleep(0.5)
    print 'Air is the element of freedom.\n' \
          'Airbenders are pacifists, spirtiual and carefree.\n' \
          'powerful airbenders are capable of harnessing\n' \
          'the immense and intangible power of the wind.\n' \
          'they can even fly if the need arises'

sleep(1)