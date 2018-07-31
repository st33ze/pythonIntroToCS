# average.py
#   A simple program to calculate average of the exam scores
#   Illustrates use of multiple input
#
# by: st33ze

def main():
    # Introduction
    print("This program calculates average of three exam scores.")

    score1, score2, score3 = eval(input("Enter three scores, separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    # Output
    print("The average of the score is: {}".format(average))

main()    
