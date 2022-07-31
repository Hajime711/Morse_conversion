import unittest
import morse

class Test(unittest.TestCase):
    def test_1_(self):
        print("\nRunning test1: single symbols")
        data = '-.-.--'
        result = '!'
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '-....-'
        result = '-'
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '--...-'
        result = '¡'
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '.-..-.'
        result = '"'
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '..-.-'
        result = '¿'
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '...-..-'
        result = '$'
        output = morse.decode(data)
        self.assertEqual(result,output)
    def test_2_(self):
        print("\nRunning test2: multiple symbols")
        data = '..-.- -.-.-- --...- / / / ...-..- ...-..- ...-..- / -.-.-. ---...'
        result = '¿!¡   $$$ ;:'
        output = morse.decode(data)
        self.assertEqual(result,output)
    def test_3_(self):
        print("\nRunning test3: words with special symbols")
        data = '.... . .-.. .-.. --- / .. .----. -- / .... . .-. .'
        result = "hello i'm here"
        output = morse.decode(data)
        self.assertEqual(result,output)
        data = '.... . .-.. .-.. --- / .. .----. -- / .... . .-. . / .- -. -.. / .-.-.- .-.-.- .-.-.- / .. / .-- -.-.-- .-.. .-.. / ...-..- .- ...-..- ...-..- / -.- ..-.- .-.. .-.. / -.-- -.--. -.--.-'
        result = "hello i'm here and ... i w!ll $a$$ k¿ll y()"
        output = morse.decode(data)
        self.assertEqual(result,output)

if __name__ == '__main__':
    unittest.main()