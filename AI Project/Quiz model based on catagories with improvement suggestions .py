# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:00:39 2020

@author: Asusa
"""
#dont forget to read ReadME file.

import json
import time

TOPICS_LIST = ['science', 'history', 'commerce', 'technology', 'worldgk']
# this list has to in sync with the JSON filename and the Menu prompt inside test() method

def ask_one_question(question):
    print("\n" + question)
    choice = input("Enter Your Choice [a/b/c/d]: ")
    while(True):
        if choice.lower() in ['a', 'b', 'c', 'd']:
            return choice
        else:
            print("Invalid choice. Enter again")
            choice = input("Enter Choice [a/b/c/d]: ")

def score_one_result(key, meta):
    actual = meta["answer"]
    if meta["user_response"].lower() == actual.lower():
        print("Q.{0} Absolutely Correct!\n".format(key))
        return 2
    else:
        print("Q.{0} Incorrect!".format(key))
        print("Right Answer is ({0})".format(actual))
        print ("Learn more : " + meta["more_info"] + "\n")
        return -1


def test(questions):
    score = 0
    
    print("General Instructions:\n1. Please enter only the choice letter corresponding to the correct answer.\n2. Each question carries 2 points\n3. Wrong answer leads to -1 marks per question\nQuiz will start momentarily. Good Luck!\n")
    time.sleep(4)
    for key, meta in questions.items():
        questions[key]["user_response"] = ask_one_question(meta["question"])
    print("\n***************** RESULT ********************\n")
    for key, meta in questions.items():
        score += score_one_result(key, meta)
    print("Your Score:", score, "/", (2 * len(questions)))
    total=2*len(questions)
    persentage=(score/total)*100
    if score<0:
        persentage=0
        print("You scored zero persentage and negtive marks please refer above remark given for each question and try to improve yourself \nThere are no shortcuts to any place worth going. \n ","Persentage=",persentage,"%")
    elif persentage<=40:
        print("You scored less then passing persentage and try to avoid negtive marks please refer above remark given for each question and try to improve yourself \n It always seems impossible until it’s done.\n ","Persentage=",persentage,"%")
    elif persentage>=40 and persentage<=50:
        print("You scored passing percentage ,try reduse negtive marks\n please refer above remark given for each question and try to improve yourself \n The difference between ordinary and extraordinary is that little “extra.”\n ","Persentage=",persentage,"%")
    elif persentage>50 and persentage<=60:
        print("You scored average percentage ,try reduse negtive marks\n please refer above remark given for each question and try to improve yourself \n . It always seems impossible until it’s done.\n ","Persentage=",persentage,"%")
    elif persentage>60 and persentage<=80:
        print("You scored Good percentage ,try reduse negtive marks\n please refer above remark given for each question and try to improve yourself \nIf it’s important to you, you’ll find a way. If not, you’ll find an excuse.\n ","Persentage=",persentage,"%")
    elif persentage>80 and persentage<90:
        print("You scored very Good percentage ,try reduse negtive marks \n please refer above remark given for each question and try to improve yourself \n It always seems impossible until it’s done\n","Persentage=",persentage,"%")
    elif persentage>=90:
        print("You scored excelent percentage ,try reduse negtive marks\n please refer above remark given for each question and try to improve yourself \nChallenges are what make life interesting. Overcoming them is what makes life meaningful. \n ","Persentage=",persentage,"%")
    else:
        print("It always seems impossible until it’s done.")
 
  
 
def load_question(filename):
    """
    loads the questions from the JSON file into a Python dictionary and returns it
    """
    questions = None
    with open(filename, "r") as read_file:
        questions = json.load(read_file)
    return (questions)


def play_quiz():
    flag = False
    try:
        choice = int(input("Welcome to Today's Quiz!\nChoose your domain of interest:\n(1). Science\n(2). History of India\n(3). Commerce\n(4). Technology\n(5). World Gk\nEnter Your Choice [1/2/3/4/5]: "))
        if choice > len(TOPICS_LIST) or choice < 1:
            print("Invalid Choice. Enter Again")
            flag = True # raising flag
    except ValueError as e:
        print("Invalid Choice. Enter Again")
        flag = True # raising a flag

    if not flag:
        questions = load_question('topics/'+TOPICS_LIST[choice-1]+'.json')
        test(questions)
    else:
        play_quiz() # replay if flag was raised

def user_begin_prompt():
    print("Wanna test your GK?\nA. Yes\nB. No")
    play = input()
    if play.lower() == 'a' or play.lower() ==  'y':
        play_quiz()
    elif play.lower() == 'b':
        print("Hope you come back soon!")
    else:
        print("Hmm. I didn't quite understand that.\nPress A to play, or B to quit.")
        user_begin_prompt()

def execute():
    user_begin_prompt()

if __name__ == '__main__':
    execute()
