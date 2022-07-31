import unittest
import morse

class Test(unittest.TestCase):
    def test_1_(self):
        print("\nRunning test1: single symbols")
        data = '!'
        result = morse.encode(data)
        self.assertEqual(result,'-.-.--')
        data = '-'
        result = morse.encode(data)
        self.assertEqual(result,'-....-')
        data = '¡'
        result = morse.encode(data)
        self.assertEqual(result,'--...-')
        data = '"'
        result = morse.encode(data)
        self.assertEqual(result,'.-..-.')
        data = '¿'
        result = morse.encode(data)
        self.assertEqual(result,'..-.-')
        data = '$'
        result = morse.encode(data)
        self.assertEqual(result,'...-..-')
    def test_2_(self):
        print("\nRunning test2: multiple symbols")
        data = '¿!¡   $$$ ;:'
        result = morse.encode(data)
        self.assertEqual(result,'..-.- -.-.-- --...- / / / ...-..- ...-..- ...-..- / -.-.-. ---...')
    def test_3_(self):
        print("\nRunning test3: words with special symbols")
        data = "hello I'm here"
        result = morse.encode(data)
        self.assertEqual(result,'.... . .-.. .-.. --- / .. .----. -- / .... . .-. .')
        data = "hello I'm here and ... I w!ll $a$$ k¿ll y()"
        result = morse.encode(data)
        self.assertEqual(result,'.... . .-.. .-.. --- / .. .----. -- / .... . .-. . / .- -. -.. / .-.-.- .-.-.- .-.-.- / .. / .-- -.-.-- .-.. .-.. / ...-..- .- ...-..- ...-..- / -.- ..-.- .-.. .-.. / -.-- -.--. -.--.-')

if __name__ == '__main__':
    unittest.main()