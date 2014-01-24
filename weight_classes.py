# Mid-term (refer to grader.py pg. 135-137
# Amanda L. Moen
# amandalmoen@yahoo.com
# Programming Exercises
# 1) You are to write a program that reads in a boxer's weight and
# report back to which weight class they belong based upon the following
# table (e.g., 141-160 is the Welterweight class):
# Weight Limits:        # Class Name:
# 201+ lb               Heavyweight
# 181-200 lb            Cruiserweight
# 161-180 lb            Middleweight
# 141-160 lb            Welterweight
# 121-140 lb            Lightweight
# 111-120 lb            Featherweight
# 0-110 lb              Bantamweight

# This program gets a weight from the boxer and reports
# back to which weight class they belong.

def main():
    # Get a weight from the user.
    weight = input('Enter your weight: ')

    # Determine the weight class.
    if weight < 111:
        print 'Your weight class is Bantamweight.'
    elif weight < 121:
        print 'Your weight class is Featherweight.'
    elif weight < 141:
        print 'Your weight class is Lightweight.'
    elif weight < 161:
        print 'Your weight class is Welterweight.'
    elif weight < 181:
        print 'Your weight class is Middleweight.'
    elif weight < 201:
        print 'Your weight class is Cruiserweight.'
    else:
        print 'Your weight class is Heavyweight.'

# Call the main function.
main()
