#################################################
# hw3.py
# name:
# andrew id:
#################################################

import cs112_f22_week3_linter
import math
from cmu_112_graphics import *

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7): #helper-fn
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d): #helper-fn
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

def rgbString(red, green, blue):
     return f'#{red:02x}{green:02x}{blue:02x}'

#################################################
# Functions for you to write
#################################################

def rotateStringLeft(s, n):
    l = len(s)
    if n < 0:
        n = abs(n)%l
        if(n != 0 ):
            s_shift = s[-n:]
            return (s_shift + s[0:l-n])
        else:
            return s
    else:
        n = abs(n)%l
        s_shift = s[0:n]
        return (s[n:l] + s_shift)

def applyCaesarCipher(message, shift):
    i = 0
    lettleCount = 26
    mesCopy = message
    if(shift < 0):
        shift = abs(shift)
        shift %= lettleCount
        shift = lettleCount - shift
    for lettle in message:
        if ord(lettle) in range(ord('a'),ord('z')+1):
            lettleValue = ord(lettle)
            lettleValue += shift
            lettleValue %= ord('z')
            if lettleValue == 0:
                lettleValue = ord('z')
            elif lettleValue < ord('a'):
                lettleValue += (ord('a')-1)
            mesCopy = mesCopy[:i] + chr(lettleValue) + mesCopy[i+1:]
        elif ord(lettle) in range(ord('A'),ord('Z')+1):
            lettleValue = ord(lettle)
            lettleValue += shift
            lettleValue %= ord('Z')
            if lettleValue == 0:
                lettleValue = ord('Z')
            elif lettleValue < ord('A'):
                lettleValue += (ord('A')-1)
            mesCopy = mesCopy[:i] + chr(lettleValue) + mesCopy[i+1:]
        i += 1  
    return mesCopy

def largestNumber(s):
    maxNumber = 0
    currentNumber = 0
    isExistNumber = False
    state = 'number'
    for symbol in s:
        if state == 'number':
            if (symbol.isdigit()):
                isExistNumber = True
                currentNumber = currentNumber*10+int(symbol)
                state ='number'
                continue
            else:
                state = 'text'
                if(maxNumber < currentNumber):
                    maxNumber = currentNumber
                currentNumber = 0
                continue
        if state == 'text':
            if (symbol.isdigit()):
                isExistNumber = True
                currentNumber = currentNumber*10+int(symbol)
                if(maxNumber < currentNumber):
                    maxNumber = currentNumber
                state ='number'
                continue
            else:
                state = 'text'
                continue
    if(isExistNumber):
        return maxNumber
    else:
        return None

def topScorer(data):
    return 42

def collapseWhitespace(s):
    return 42

def patternedMessage(message, pattern):
    return 42

def mastermindScore(target, guess):
    return 42



#################################################
# Graphics functions for you to write
#################################################

# Make sure you have cmu_112_graphics downloaded to the 
# same directory as this file!

# Note: If you don't see any text when running graphics code, 
# try changing your computer's color theme to light mode. 

def drawFlagOfTheEU(canvas, x0, y0, x1, y1):
    # You may delete starter code in this function
    canvas.create_rectangle(x0, y0, x1, y1, fill='yellow', outline='black')
    size = (x1 - x0) // 12
    canvas.create_text((x0 + x1)/2, (y0 + y1)/2, fill='black',
                       text='Draw the EU flag here!', font=f'Arial {size} bold')
    # Your code goes here!

def drawNiceRobot(canvas, width, height):
    # You may delete starter code in this function
    canvas.create_rectangle(0, 0, width, height, fill='yellow', outline='black')
    canvas.create_text(width/2, height/2, fill='black',
                       text='Draw a nice robot here!',
                       font='Arial 20 bold')
    # Your code goes here!

#################################################
# Bonus/Optional
#################################################

def bonusTopLevelFunctionNames(code):
    return 42

def bonusGetEvalSteps(expr):
    return 42

#################################################
# Test Functions
#################################################

def testRotateStringLeft():
    print("Testing RotateStringLeft()...", end="")
    assert(rotateStringLeft("abcde", 0) == "abcde")
    assert(rotateStringLeft("abcde", 1) == "bcdea")
    assert(rotateStringLeft("abcde", 2) == "cdeab")
    assert(rotateStringLeft("abcde", 3) == "deabc")
    assert(rotateStringLeft("abcde", 4) == "eabcd")
    assert(rotateStringLeft("abcde", 5) == "abcde")
    assert(rotateStringLeft("abcde", 25) == "abcde")
    assert(rotateStringLeft("abcde", 28) == "deabc")
    assert(rotateStringLeft("abcde", -1) == "eabcd")
    assert(rotateStringLeft("abcde", -2) == "deabc")
    assert(rotateStringLeft("abcde", -3) == "cdeab")
    assert(rotateStringLeft("abcde", -4) == "bcdea")
    assert(rotateStringLeft("abcde", -5) == "abcde")
    assert(rotateStringLeft("abcde", -25) == "abcde")
    assert(rotateStringLeft("abcde", -28) == "cdeab")
    print("Passed!")

def testApplyCaesarCipher():
    print("Testing applyCaesarCipher()...", end="")
    # assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 3) ==
    #                          "defghijklmnopqrstuvwxyzabc")
    # assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
    # assert(applyCaesarCipher("1234", 6) == "1234")
    # assert(applyCaesarCipher("abcdefghijklmnopqrstuvwxyz", 25) ==
    #                          "zabcdefghijklmnopqrstuvwxy")
    # assert(applyCaesarCipher("We Attack At Dawn", 2)  == "Yg Cvvcem Cv Fcyp")
    # assert(applyCaesarCipher("We Attack At Dawn", 4)  == "Ai Exxego Ex Hear")
    assert(applyCaesarCipher("We Attack At Dawn", -1) == "Vd Zsszbj Zs Czvm")
    # And now, the whole point...
    assert(applyCaesarCipher(applyCaesarCipher('This is Great', 25), -25)
           == 'This is Great')
    print("Passed!")

def testLargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3") == 3)
    assert(largestNumber("3 I saw!") == 3)
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("I saw 3 dogs, 1700 cats, and 14 cows!") == 1700)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed!")

def testTopScorer():
    print('Testing topScorer()...', end='')
    data = '''\
Fred,10,20,30,40
Wilma,10,20,30
'''
    assert(topScorer(data) == 'Fred')

    data = '''\
Fred,10,20,30
Wilma,10,20,30,40
'''
    assert(topScorer(data) == 'Wilma')

    data = '''\
Fred,11,20,30
Wilma,10,20,30,1
'''
    assert(topScorer(data) == 'Fred,Wilma')
    assert(topScorer('') == None)
    print('Passed!')

def testCollapseWhitespace():
    print("Testing collapseWhitespace()...", end="")
    assert(collapseWhitespace("a\nb") == "a b")
    assert(collapseWhitespace("a\n   \t    b") == "a b")
    assert(collapseWhitespace("a\n   \t    b  \n\n  \t\t\t c   ") == "a b c ")
    assert(collapseWhitespace("abc") == "abc")
    assert(collapseWhitespace("   \n\n  \t\t\t  ") == " ")
    assert(collapseWhitespace(" A  \n\n  \t\t\t z  \t\t ") == " A z ")
    print("Passed!")

def testPatternedMessage():
    print("Testing patternedMessage()...", end="")

    # Test case 0
    message0 = "abc def"
    pattern0 = "***** ***** ****"
    solution0 = "abcde fabcd efab"
    assert(patternedMessage(message0, pattern0) == solution0.strip('\n'))

    # Test case 1
    message1 = "abc def"
    pattern1 = "\n***** ***** ****\n"
    solution1 = "abcde fabcd efab"
    assert(patternedMessage(message1, pattern1) == solution1.strip('\n'))

    # Test case 2
    message2 = "Go Pirates!!!"
    pattern2 = """
***************
******   ******
***************
"""
    solution2 = """
GoPirates!!!GoP
irates   !!!GoP
irates!!!GoPira
"""
    assert(patternedMessage(message2, pattern2) == solution2.strip('\n'))


    # Test case 3
    message3 = "Three Diamonds!"
    pattern3 = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *
"""
    solution3 = """
    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n
"""
    assert(patternedMessage(message3, pattern3) == solution3.strip('\n'))

    # Test case 4
    message4 = "Go Steelers!"
    pattern4 = """
                          oooo$$$$$$$$$$$$oooo
                      oo$$$$$$$$$$$$$$$$$$$$$$$$o
                   oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o         o$   $$ o$
   o $ oo        o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o       $$ $$ $$o$
oo $ $ '$      o$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$o       $$$o$$o$
'$$$$$$o$     o$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$o    $$$$$$$$
  $$$$$$$    $$$$$$$$$$$      $$$$$$$$$$$      $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$    $$$$$$$$$$$$$$  '$$$
   '$$$'$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$
    $$$   o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     '$$$o
   o$$'   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$       $$$o
   $$$    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$' '$$$$$$ooooo$$$$o
  o$$$oooo$$$$$  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$   o$$$$$$$$$$$$$$$$$
  $$$$$$$$'$$$$   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$'
 ''''       $$$$    '$$$$$$$$$$$$$$$$$$$$$$$$$$$$'      o$$$
            '$$$o     '$$$$$$$$$$$$$$$$$$'$$'         $$$
              $$$o          '$$'$$$$$$'           o$$$
               $$$$o                                o$$$'
                '$$$$o      o$$$$$$o'$$$$o        o$$$$
                  '$$$$$oo     '$$$$o$$$$$o   o$$$$'
                     '$$$$$oooo  '$$$o$$$$$$$$$'
                        '$$$$$$$oo $$$$$$$$$$
                                '$$$$$$$$$$$
                                    $$$$$$$$$$$$
                                     $$$$$$$$$$'
                                      '$$$'
"""
    solution4 = """
                          GoSteelers!GoSteeler
                      s!GoSteelers!GoSteelers!GoS
                   teelers!GoSteelers!GoSteelers!GoS         te   el er
   s ! Go        Steelers!GoSteelers!GoSteelers!GoSteel       er s! GoSt
ee l e rs      !GoSteeler    s!GoSteelers!    GoSteelers       !GoSteel
ers!GoSte     elers!GoSt      eelers!GoSt      eelers!GoSt    eelers!G
  oSteele    rs!GoSteele      rs!GoSteele      rs!GoSteelers!GoSteeler
  s!GoSteelers!GoSteelers    !GoSteelers!G    oSteelers!GoSt  eele
   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSteel     ers!
    GoS   teelers!GoSteelers!GoSteelers!GoSteelers!GoSteelers     !GoSt
   eele   rs!GoSteelers!GoSteelers!GoSteelers!GoSteelers!GoSt       eele
   rs!    GoSteelers!GoSteelers!GoSteelers!GoSteelers!Go Steelers!GoSteele
  rs!GoSteelers  !GoSteelers!GoSteelers!GoSteelers!GoS   teelers!GoSteelers
  !GoSteelers!G   oSteelers!GoSteelers!GoSteelers!Go     Steel
 ers!       GoSt    eelers!GoSteelers!GoSteelers!G      oSte
            elers     !GoSteelers!GoSteelers!         GoS
              teel          ers!GoSteel           ers!
               GoSte                                elers
                !GoSte      elers!GoSteele        rs!Go
                  Steelers     !GoSteelers!   GoStee
                     lers!GoSte  elers!GoSteeler
                        s!GoSteele rs!GoSteel
                                ers!GoSteele
                                    rs!GoSteeler
                                     s!GoSteeler
                                      s!GoS
"""
    assert(patternedMessage(message4, pattern4) == solution4.strip('\n'))
    print("Passed!")

def testMastermindScore():
    print("Testing mastermindScore()...", end="")
    assert(mastermindScore('abcd', 'aabd') ==
                           '2 exact matches, 1 partial match')
    assert(mastermindScore('efgh', 'abef') ==
                           '2 partial matches')
    assert(mastermindScore('efgh', 'efef') ==
                           '2 exact matches')
    assert(mastermindScore('ijkl', 'mnop') ==
                           'No matches')
    assert(mastermindScore('cdef', 'cccc') ==
                           '1 exact match')
    assert(mastermindScore('cdef', 'bccc') ==
                           '1 partial match')
    assert(mastermindScore('wxyz', 'wwwx') ==
                           '1 exact match, 1 partial match')
    assert(mastermindScore('wxyz', 'wxya') ==
                           '3 exact matches')
    assert(mastermindScore('wxyz', 'awxy') ==
                           '3 partial matches')
    assert(mastermindScore('wxyz', 'wxyz') ==
                           'You win!!!')
    print("Passed!")

def testBonusTopLevelFunctionNames():
    print("Testing bonusTopLevelFunctionNames()...", end="")

    # no fn defined
    code = """\
# This has no functions!
# def f(): pass
print("Hello world!")
"""
    assert(bonusTopLevelFunctionNames(code) == "")

    # f is redefined
    code = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # def not at start of line
    code = """\
def f(): return "def g(): pass"
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (''')
    code = """\
def f(): return '''
def g(): pass'''
"""
    assert(bonusTopLevelFunctionNames(code) == "f")

    # g() is in triple-quotes (""")
    code = '''\
def f(): return """
def g(): pass"""
'''
    assert(bonusTopLevelFunctionNames(code) == "f")

    # triple-quote (''') in comment
    code = """\
def f(): return 42 # '''
def g(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # triple-quote (""") in comment
    code = '''\
def f(): return 42 # """
def g(): pass # """
'''
    assert(bonusTopLevelFunctionNames(code) == "f.g")

    # comment character (#) in quotes
    code = """\
def f(): return '#' + '''
def g(): pass # '''
def h(): return "#" + '''
def i(): pass # '''
def j(): return '''#''' + '''
def k(): pass # '''
"""
    assert(bonusTopLevelFunctionNames(code) == "f.h.j")
    print("Passed!")

def testBonusGetEvalSteps():
    print("Testing bonusGetEvalSteps()...", end="")
    assert(bonusGetEvalSteps("0") == "0 = 0")
    assert(bonusGetEvalSteps("2") == "2 = 2")
    assert(bonusGetEvalSteps("3+2") == "3+2 = 5")
    assert(bonusGetEvalSteps("3-2") == "3-2 = 1")
    assert(bonusGetEvalSteps("3**2") == "3**2 = 9")
    assert(bonusGetEvalSteps("31%16") == "31%16 = 15")
    assert(bonusGetEvalSteps("31*16") == "31*16 = 496")
    assert(bonusGetEvalSteps("32//16") == "32//16 = 2")
    assert(bonusGetEvalSteps("2+3*4") == "2+3*4 = 2+12\n      = 14")
    assert(bonusGetEvalSteps("2*3+4") == "2*3+4 = 6+4\n      = 10")
    assert(bonusGetEvalSteps("2+3*4-8**3%3") == """\
2+3*4-8**3%3 = 2+3*4-512%3
             = 2+12-512%3
             = 2+12-2
             = 14-2
             = 12""")
    assert(bonusGetEvalSteps("2+3**4%2**4+15//3-8") == """\
2+3**4%2**4+15//3-8 = 2+81%2**4+15//3-8
                    = 2+81%16+15//3-8
                    = 2+1+15//3-8
                    = 2+1+5-8
                    = 3+5-8
                    = 8-8
                    = 0""")
    print("Passed!")

#################################################
# Graphics Test Functions
#################################################

def testDrawFlagOfTheEU(app, canvas):
    canvas.create_rectangle(0, 0, app.width, app.height, fill='lightYellow')
    drawFlagOfTheEU(canvas, 50, 125, 350, 275)
    drawFlagOfTheEU(canvas, 425, 100, 575, 200)
    drawFlagOfTheEU(canvas, 450, 275, 550, 325)
    canvas.create_text(app.width/2, app.height-40, fill='black',
                       text="Testing drawFlagOfTheEU")
    canvas.create_text(app.width/2, app.height-25, fill='black',
                       text="You should see three labeled flags.")
    canvas.create_text(app.width/2, app.height-10, fill='black',
                       text="This does not need to resize properly!")

def testDrawNiceRobot(app, canvas):
    drawNiceRobot(canvas, app.width, app.height)
    canvas.create_text(app.width/2, app.height-20, 
          text=('Testing drawNiceRobot' +
            f'(canvas, {app.width}, {app.height})'))
    canvas.create_text(app.width/2, app.height-10, 
          text=f'''Comment out these print lines if they mess up your art!''')

def drawSplashScreen(app, canvas):
    text = f'''\
Press the number key for the 
exercise you would like to test!

1. drawFlagOfTheEU
2. drawNiceRobot

Press any other key to return
to this screen.
'''
    textSize = min(app.width,app.height) // 40
    canvas.create_text(app.width/2, app.height/2, text=text, fill='black',
                       font=f'Arial {textSize} bold')


def appStarted(app):
    app.lastKeyPressed = None
    app.timerDelay = 10**10

def keyPressed(app, event):
    app.lastKeyPressed = event.key

def redrawAll(app, canvas):
    if app.lastKeyPressed == '1':
      testDrawFlagOfTheEU(app, canvas)
    elif app.lastKeyPressed == '2':
      testDrawNiceRobot(app, canvas)
    else:
      drawSplashScreen(app, canvas)

def testGraphicsFunctions():
    runApp(width=700, height=600)

#################################################
# testAll and main
#################################################

def testAll():
    # comment out the tests you do not wish to run!
    testRotateStringLeft()
    testApplyCaesarCipher()
    testLargestNumber()
    # testTopScorer()
    # testCollapseWhitespace()
    # testPatternedMessage()
    # testMastermindScore()

    # Test all Graphics:
    # testGraphicsFunctions()

    # Bonus:
    # testBonusTopLevelFunctionNames()
    # testBonusGetEvalSteps()

def main():
    cs112_f22_week3_linter.lint()
    testAll()

if __name__ == '__main__':
    main()
