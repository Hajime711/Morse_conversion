import unittest
import morse

class Test(unittest.TestCase):
    def test_1_(self):
        print("\nRunning test1: single letter")
        data = '.-'
        result = morse.decode(data)
        self.assertEqual(result,'a')
    def test_2_(self):
        print("\nRunning test2: single word(us)")
        data = '..- ...'
        result = morse.decode(data)
        self.assertEqual(result,'us')
    def test_3_(self):
        print("\nRunning test3: spaces only")
        data = '/ / /'
        result = morse.decode(data)
        self.assertEqual(result,'   ')
    def test_4_(self):
        print("\nRunning test4: two words(hello there)")
        data = '.... . .-.. .-.. --- / - .... . .-. .'
        result = morse.decode(data)
        self.assertEqual(result,'hello there')
    def test_5_(self):
        print("\nRunning test5: long sentence")
        data = '.... . .-.. .-.. --- / - .... . .-. . / .. -- / -.. --- .. -. --. / .--. -.-- - .... --- -. / .--. .-. --- --. .-. .- -- -- .. -. --. / .- -. -.. / . -. .--- --- -.-- .. -. --. / .. - / ...- . .-. -.-- / -- ..- -.-. .... / .-. .. --. .... - / -. --- .--'
        result = morse.decode(data)
        self.assertEqual(result,'hello there im doing python programming and enjoying it very much right now')
if __name__ == '__main__':
    unittest.main()