import unittest
import morse

class Test(unittest.TestCase):
    def test_1_(self):
        print("\nRunning test1: single letter")
        data = 'A'
        result = morse.encode(data)
        self.assertEqual(result,'.-')
    def test_2_(self):
        print("\nRunning test2: single word(us)")
        data = 'us'
        result = morse.encode(data)
        self.assertEqual(result,'..- ...')
    def test_3_(self):
        print("\nRunning test3: spaces only")
        data = '   '
        result = morse.encode(data)
        self.assertEqual(result,'/ / /')
    def test_4_(self):
        print("\nRunning test4: two words(hello there)")
        data = 'hello there'
        result = morse.encode(data)
        self.assertEqual(result,'.... . .-.. .-.. --- / - .... . .-. .')
    def test_5_(self):
        print("\nRunning test5: long sentence")
        data = 'hello there im doing python programming and enjoying it very much right now'
        result = morse.encode(data)
        self.assertEqual(result,'.... . .-.. .-.. --- / - .... . .-. . / .. -- / -.. --- .. -. --. / .--. -.-- - .... --- -. / .--. .-. --- --. .-. .- -- -- .. -. --. / .- -. -.. / . -. .--- --- -.-- .. -. --. / .. - / ...- . .-. -.-- / -- ..- -.-. .... / .-. .. --. .... - / -. --- .--')
if __name__ == '__main__':
    unittest.main()