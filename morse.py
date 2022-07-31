import morsebt

tree = morsebt.initMorseBT()
##un-comment if you want to print Morse Tree in pre-order
#print('Morse Binary Tree:')
#tree.traversePreOrder()
#print('\n')

def encode(msg:str)->str:
    msg = msg.upper()
    morsecode = ''
    for character in msg:
        code = []
        charcode = ''
        if character==' ': #space
            morsecode+='/ '
            continue
        morsebt.morseEncode(tree,character,code)
        charcode = charcode.join(code)
        charcode = charcode[::-1]#reverse
        morsecode += charcode + " "
    return morsecode[0:len(morsecode)-1:]#remove extra space

def decode(msg:str)->str:
    morsedecode = ''
    for char_code in msg.split(' '):
        character = ''
        if char_code=='/': #for space
            morsedecode = morsedecode + " "
        else:
            character = morsebt.morseDecode(tree,char_code,0)
            morsedecode = morsedecode + character
    return morsedecode.lower()
