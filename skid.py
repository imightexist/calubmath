from signal import signal, SIGINT, SIG_IGN
from json import load
from random import choice
import subprocess

signal(SIGINT, SIG_IGN)

eng = None
math = None
with open("maths_practice_test1.json", "rb") as f:
    eng = load(f)
with open("maths_practice_test2.json", "rb") as f:
    math = load(f)

done = []
correct = 0
answered = 0
def getQuestion(array):
    q = None
    while (q is None) or ("svg" in q["question_text"]):
        q = choice(array)
    return q

def doQuestion(array):
    global done
    global correct
    global answered
    q = getQuestion(array)
    # qd = q["question"]
    print("Q:",q["question_text"])
    for answer in q["options"].keys():
        text = q["options"][answer]
        print(f"\t{answer} -> {text}")
    inp = None
    while inp is None:
        try:
            inp = input("A: ").strip().lower()[0]
        except:
            print()
    answered += 1
    if inp == q["correct_answer"]:
        correct += 1
        print("Correct answer! "+str(correct)+"/8")
        # done.append(q["id"])
    else:
        # correct = 0
        print("WRONG! "+str(correct)+"/8")
        print("Correct answer: " + q["correct_answer"])
        # done = []
    print()
print("calubmath")
print("You've been a bad boy. Answer 6/8 questions correctly to access Windows.")
print()
shit = True
while correct < 6:
    if answered>=8:
        answered = 0
        correct = 0
        print("You failed the test. Please try again.")
        print()
    if shit:
        doQuestion(eng)
    else:
        doQuestion(math)
    shit = not shit

print("Very well. Come back soon!")
