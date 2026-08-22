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
    while (q is None) or (q["id"] in done):
        q = choice(array)
    return q

def doQuestion(array):
    global done
    global correct
    q = getQuestion(array)
    qd = q["question"]
    if qd["paragraph"] != "null":
        print(f"\"{qd["paragraph"]}\"")
        print()
    print(f"Q: {qd["question"]}")
    for answer in qd["choices"].keys():
        text = qd["choices"][answer]
        print(f"\t{answer} -> {text}")
    inp = None
    while inp is None:
        try:
            inp = input("A: ").strip().upper()[0]
        except:
            print()
    answered += 1
    if inp == qd["correct_answer"]:
        correct += 1
        print("Correct answer! "+str(correct)+"/6")
        done.append(q["id"])
    else:
        # correct = 0
        print("WRONG! "+str(correct)+"/6")
        print("Correct answer: " + qd["correct_answer"])
        done = []
    print()
    print()
    print()
print("calubmath")
print("You've been a bad boy. Answer 6/8 questions correctly to access Windows.")
print()

while correct < 6:
    if answered>=8:
        answered = 0
        correct = 0
    doQuestion(eng)
    doQuestion(math)

print("Very well. Come back soon!")
