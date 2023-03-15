import difflib              # to finding similar matches
import json                 # for uploading the data-set
import pyttsx3 as ptx       # to reading the output (text to speach module)

# uploading the data set
df = json.load(open('data.json'))
# print(df)


def defination():
    print('\n\t\t\t\t\t\t\tWELCOME TO THE DICTIONARY\t\t\t\t\t\t\t\n')
    # taking input from user
    word = input('What you are searching for :')
    print(f"\nWORD : {word}")
    word = word.lower()
    # searching for similar words to user input
    match = difflib.get_close_matches(word, df.keys())
    # print(match)
    # we add these three steps because what if word is in other styles (upper, lower, title case)
    if word in df:
        print("\nDEFINATION :")
        return df[word]


    elif word.title() in df:
        print("\nDEFINATION :")
        return df[word.title()]


    elif word.upper() in df:
        print("\nDEFINATION :")
        return df[word.upper()]


    # when we found a similar match
    elif len(match) == 1:
        print(f'\nYOU ARE LOOKING FOR {match} THIS WORD instade {word}')
        print("IF YES THEN ENTER Y IF NOT THEN ENTER N")
        ans = input('\nEnter your Answer here :')
        if ans == "Y":
            print("\nDEFINATION :")
            return df[match]
        else:
            print('\nSORRY!!!!! WE CANT HELP YOU')

    # when we found more similar matches
    elif len(match) > 1:
        print('\nPLEASE CHOOSE THE WORD YOU ARE LOOKING FOR :')
        # print matches that we have found in data-set
        for i in range(len(match)):
            print(match[i])
        ser = input('\nenter your answer :')
        if ser in df.keys():
            print('\nDEFINATION :')
            return df[ser]
        else:
            print('\nSORRY!!!! WE CANT HELP ')
    else:
        print("\nSORRY WE CANT HELP YOU")



output = defination()
if type(output) == list:
    for i in output:
        print(str(i).replace(',','\n'))
    print('\nGLAD TO HELP YOU')

# for reading the output
eng = ptx.init()
"""SPEED"""
rate = eng.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice rate
eng.setProperty('rate', 120)

"""VOICE"""
voices = eng.getProperty('voices')  # getting details of current voice
# eng.setProperty('voice', voices[0].id)             # changing index, changes voices. o for male
eng.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

"""VOLUME"""
volume = eng.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
eng.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

eng.say(output)
eng.runAndWait()
eng.stop()








'''
word : This is the string for which we need the close matches.
possibilities : This is usually a list of string values in which we search for the match.
'''

# match = difflib.get_close_matches('hel',df.keys())
# print(match)
# for i in range(len(match)):
#     print(match[i])

# word = "learning"
# possibilities = ["love", "learn", "lean", "moving", "hearing"]
# match = difflib.get_close_matches('le',possibilities)
# print(match)
# for i in range(len(match)):
#     print(i+1,match[i])
# print(str(match).replace(',','\n'))

# word = {'a':["asdf,zxcv"],'b':["qwer,pouy"],'c':["lkjh,mnbv"]}
# w = word['a']
# if type(w) == list:
#     for i in word['a']:
#         print(i)
# for i in word['a']:
#         print(str(i).replace(',','\n'))

# a ='hello seraph how are you'
# print(a.lower())