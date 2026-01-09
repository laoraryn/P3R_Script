# Recreation/slight cleanup of the code I used as a first pass to clean up the script files from Persona 3 Reload.

# My Python skills are 100% self taught, so sorry if the code isn't formatted or ordered properly! I did my best.

import os, re

allfiles = []

# These first for loops put all files into one directory, but label them with the appropriate game so they're still organized

for file in os.listdir("./journey"):
    if file.endswith('.txt'): # getting rid of crud files
        allfiles.append((os.path.join('./journey',file),'Journey'))

for file in os.listdir("./answer"):
    if file.endswith('.txt'):
        allfiles.append((os.path.join('./answer',file),'Answer'))

# get text from file, cleanup file name
def FileGet(file,game):

    with open(file) as x:
        Text = x.read()

    if file.startswith(r'./journey/BMD_') == True:
        file = file[14:]
    elif file.startswith(r'./answer/BMD_') == True:
        file = file[13:]
    if file.endswith(r'_unwrapped.bmd.msg') == True:
        file = file[:-18]

    if game != 'n/a':
        CleanName = f'{game}_{file}'
    else:
        CleanName = file

    return [Text, CleanName]

# do basic find-replace from 'Readable Tags'    
def FTags(Text):
    
    ReadableTags = (('\\[f 4 2\\]','Minato'),
                ('\\[f 4 1\\]','Arisato'),
                ('\\[f 4 3\\]','Minato Arisato'),
                ('\\[nl\\]','Arisato'),
                ('\\[nf\\]','Minato'),
                ('\\[n\\]\\[w\\]\\[e\\]',''), # unimportant
                ('\\[f 2 1\\]',''), # unimportant
                ('\\[f 5 21 1 [0-9 ]+\\]',''), # remove tag for no lip flaps
                ('\\[vp [0-9 ]+\\]',''), # remove voice line tags
                ('\\[f 4 23 [0-9 ]+\\]',''), # remove face animation tags
                ('\\[f 5 13 [0-9 ]+\\]',''), # remove social link point tags
                ('\\[n\\]',r'\n'), # newline
                ('\\[e\\]',''), # unimportant
                ('\\[[^\\[]+\\[',''), # intro tag

                # emojis
                ('\\[f 1 3 132\\]',r'<3'),
                ('\\[f 1 3 136\\]',r'*thumbs up*'),
                ('\\[f 1 3 137\\]',r':)'),
                ('\\[f 1 3 138\\]',r'*sweatdrop*'),
                ('\\[f 1 3 139\\]',r':o'),
                ('\\[f 1 3 158\\]',r'*kitty*'),

                # flag for romance route and possibly reversal
                ('\\[f 2 9\\]','\\[Bitflag toggle\\]'),

                # text color change - just made it all bold
                ('\\[clr [0-9]+\\]',r'**'),
                ('未使用','Not Used'),
                (' DEV: Internal MES - ',''),
                ('\\[f [0-9 ]+\\]','') # unimportant
                )
    
    for Repl in range(len(ReadableTags)):
        Text = re.sub(ReadableTags[Repl][0],ReadableTags[Repl][1],Text)

    return Text

def SplitLine(self,game):
    Splits = re.split(r'\n',self.Text)
    for Line in range(len(Splits)):
        if Splits[Line] == '':       # empty line
            continue
        elif Splits[Line].startswith('[msg') == True or Splits[Line].startswith('[sel') == True: # label line
            Splits[Line] = LabelTags(Splits[Line],game) 
        elif Splits[Line].startswith('[bup ') == True:
            Splits[Line] = BustUps(Splits[Line])

    ReSplit = '\n'.join(Splits)

    return ReSplit

# fixing the speaker label lines
def LabelTags(STR,game):
    x = (re.split(' ',STR)) #split by space

    if len(x[-1]) == 1: #if the last split is len 1, it's just a ']'
        x.pop(-1)
    elif x[-1][-2] == ']':  #elif, if the second to last char is ']', the last 2 are ']'
        x[-1] = x[-1][:-2]
    else:                   # otherwise, the last char is a ']' and that's the only bad one
        x[-1] = x[-1][:-1]

    if len(x) > 2:      # if there's more than 2 splits, there's a name in the tag. the first one is trash
        
        Len = len(x)
        Name = ''
        if x[2][0] == '[':
            x[2] = x[2][1:]
        elif x[2][1] == '[':   # soemtimes there's a double bracket
            x[2] = x[2][2:]
        
        for y in range(Len - 2):       # loop to get all name parts into a new string - most have 1 or 2, may have more
            Name = f'{Name} {x[y+2]}'
        if Name[0] == ' ':
            Name = Name[1:]
        NewLabel = f'{Name} - {x[1]}'  # new string to be the label

    else:               # if there are only 2 splits, there's no name attached
        NewLabel = x[1]

    # cover selection lines
    # these didn't take on all the files for some reason ? 
    if game == 'Answer':
        if NewLabel.startswith(' top - SEL_') == True:
            NewLabel = 'Aigis - Selection'
        elif NewLabel.startswith('MND_') == True:
            NewLabel = 'Aigis - Thoughts'
    else:
        if NewLabel.startswith(' top - SEL_') == True or NewLabel.startswith('top - SEL_') == True:
            NewLabel = 'Minato Arisato - Selection'
        elif NewLabel.startswith('MND_') == True:
            NewLabel = 'Minato Arisato - Thoughts'

    return NewLabel

def BustUps(self,STR):
    
    Expressions =  {"0": "Neutral",
                    "1": "Happy",
                    "2": "Angry",
                    "3": "Sad",
                    "4": "Surprised",
                    "5": "Hurt",
                    "6": "Exasperated",
                    "7": "Horrified", 
                    "8": "Very angry", 
                    "9": "Scheming", 
                    "10": "Looking away", 
                    "11": "Very happy",
                    "30": "Determined", 
                    "31": "Closed eyes, concentrating", 
                    "32": "Faceplate down",
                    "33": "Upset", 
                    "60": "Tearing up", 
                    "61": "Happy tears",
                    "63": "Embarrassed crying", 
                    "64": "Crying",
                    "90": "Phone Call"}
        
    x = re.split('\\]',STR)
    xx = x[0][5:]
    xxx = re.split(' ',xx)

    try:
        Expression = Expressions[xxx[1]]
    except:
        print(f'{xxx[1]} - exp')
        Expression = "Unknown"

    if xxx[4] == 1:
        Expression = f'{Expression} - blushing'
    if xxx[5] == 1:
        Expression = f'{Expression} - sweatdrop'

    #Detail = Expression + Outfit
    if Expression != "Neutral":
        All = f'{Expression} - {x[1]}'
    else:
        All = x[1]

    return All

def NewFile(CleanName,FinalFile):

    # writes into new text file within the top level folder
    with open(f'{CleanName}.txt', "w") as ff:
        ff.write(FinalFile)

for xx in allfiles:
    
    file = xx[0]
    game = xx[1]

    thing = FileGet(file,game)
    Text = thing[0]
    CleanName = thing[1]

    CleanText = FTags(Text)

    ReSplit = SplitLine(CleanText)

    NewFile(CleanName,ReSplit)
