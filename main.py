import morse

if __name__=='__main__':

    e = morse.encode('hello There')
    print('%s'%e)
    e = morse.encode("$(hello i'm here)$")
    print('%s'%e)
    e = morse.encode('us')
    print('%s'%e)
    e = morse.encode('sos')
    print('%s'%e)
    d = morse.decode('.... . .-.. .-.. --- / - .... . .-. .')
    print('%s'%d)
    d = morse.decode('...-..- -.--. .... . .-.. .-.. --- / .. .----. -- / .... . .-. . -.--.- ...-..-')
    print('%s'%d)
    d = morse.decode('..- ...')
    print('%s'%d)
    d = morse.decode('... --- ...')
    print('%s'%d)
    
    