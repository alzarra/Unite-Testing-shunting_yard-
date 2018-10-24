import unittest
import shunting_yard as sy


class TokenizeTest(unittest.TestCase):
    def test_single_operator(self):
        tokens = list(sy.tokenize('1+2'))
        self.assertListEqual(tokens, ['1', '+', '2'])

    def test_isDigit(self):
        # test all number
        self.assertEqual(sy.isDigit('1'), True)
        self.assertEqual(sy.isDigit('2'), True)
        self.assertEqual(sy.isDigit('3'), True)
        self.assertEqual(sy.isDigit('4'), True)
        self.assertEqual(sy.isDigit('5'), True)
        self.assertEqual(sy.isDigit('6'), True)
        self.assertEqual(sy.isDigit('7'), True)
        self.assertEqual(sy.isDigit('8'), True)
        self.assertEqual(sy.isDigit('9'), True)
        self.assertEqual(sy.isDigit('0'), True)
        #test a latter
        self.assertEqual(sy.isDigit('a'), False) 
        #test a symbal 
        self.assertEqual(sy.isDigit('!'), False)

    def test_isLeftBracket(self):
        # test all kind of bracket
        self.assertEqual(sy.isLeftBracket('('), True)
        self.assertEqual(sy.isLeftBracket('['), True)
        # this is left bracket but not include in orginal function ( False ) 
        self.assertEqual(sy.isLeftBracket('{'), False)
        # test opposite side bracket
        self.assertEqual(sy.isLeftBracket(')'), False)
        self.assertEqual(sy.isLeftBracket('}'), False)
        self.assertEqual(sy.isLeftBracket(']'), False)
        # test number
        self.assertEqual(sy.isLeftBracket('1'), False)
        # test sumbal 
        self.assertEqual(sy.isLeftBracket('%'), False)

    def test_isNumber(self):
        # test all number
        self.assertEqual(sy.isNumber('1'), True)
        self.assertEqual(sy.isNumber('2'), True)
        self.assertEqual(sy.isNumber('3'), True)
        self.assertEqual(sy.isNumber('4'), True)
        self.assertEqual(sy.isNumber('5'), True)
        self.assertEqual(sy.isNumber('6'), True)
        self.assertEqual(sy.isNumber('7'), True)
        self.assertEqual(sy.isNumber('8'), True)
        self.assertEqual(sy.isNumber('9'), True)
        self.assertEqual(sy.isNumber('0'), True)
        # test a latter 
        self.assertEqual(sy.isNumber('b'), False)
        # test a symbal 
        self.assertEqual(sy.isNumber('$'), False)

    def test_isOperator(self):
        # test all including operator
        self.assertEqual(sy.isOperator('+'), True)
        self.assertEqual(sy.isOperator('-'), True)
        self.assertEqual(sy.isOperator('/'), True)
        self.assertEqual(sy.isOperator('*'), True)
        # test numbers
        self.assertEqual(sy.isOperator('5'), False)
        # test symbal
        self.assertEqual(sy.isOperator('&'), False)
        # test latter
        self.assertEqual(sy.isOperator('e'), False)
        # test similer operator 
        self.assertEqual(sy.isOperator('_'), False)
        self.assertEqual(sy.isOperator('\/'), False)

    def test_isRightBracket(self):
         # test all kind of bracket
        self.assertEqual(sy.isRightBracket(')'), True)
        self.assertEqual(sy.isRightBracket(']'), True)
        # this is left bracket but not include in orginal function ( False ) 
        self.assertEqual(sy.isRightBracket('}'), False)
        # test opposite side bracket
        self.assertEqual(sy.isRightBracket('('), False)
        self.assertEqual(sy.isRightBracket('{'), False)
        self.assertEqual(sy.isRightBracket('['), False)
        # test number
        self.assertEqual(sy.isRightBracket('1'), False)
        # test sumbal 
        self.assertEqual(sy.isRightBracket('%'), False)

    def test_peekAtStack(self):
        # test stak of size 1
        self.assertEqual(sy.peekAtStack(['1']), '1')
        # test stake of more than size 1
        self.assertEqual(sy.peekAtStack(['9','8','7','6','5','4','3']), '9')
        # test non digit stack 
        self.assertEqual(sy.peekAtStack(['+','-','*']), '+')
        # test empty stack 
##      self.assertEqual(sy.peekAtStack([]), False)
        # test other symbals(shouldn't exist but just in case) 
        self.assertEqual(sy.peekAtStack(['=','$','#']), '=')
        



    def test_popFromStack(self):
        # test stak of size 1
        self.assertEqual(sy.popFromStack(['1']), '1')
        # test stake of more than size 1
        self.assertEqual(sy.popFromStack(['9','8','7','6','5','4','3']), '9')
        # test non digit stack 
        self.assertEqual(sy.popFromStack(['+','-','*']), '+')
        # test empty stack 
##      self.assertEqual(sy.peekAtStack([]), False)
        # test other symbals(shouldn't exist but just in case) 
        self.assertEqual(sy.popFromStack(['=','$','#']), '=')

    def test_pushToStack(self):#I don't know how this function behave on asertEqual 
        # test empty stack 
 ##       self.assertEqual(sy.pushToStack([],'1',),['1'])
        # test stack with 1 item 
  ##      self.assertEqual(sy.pushToStack([1],'2'),['1','2'])
        # test stack with many item
  ##      self.assertEqual(sy.pushToStack(['a','4','*'],'2'),['2','a','4','*'])
          self.assertEqual(sy.pushToStack([],'1',),None)



    def test_stackIsEmpty(self):
        # test empty stack
        self.assertEqual(sy.stackIsEmpty([]),True)
        # test non empty with number
        self.assertEqual(sy.stackIsEmpty(['1']),False)

        # test non empty with latter
        self.assertEqual(sy.stackIsEmpty(['a']),False)

        # test non empty with others 
        self.assertEqual(sy.stackIsEmpty(['+']),False)
        self.assertEqual(sy.stackIsEmpty(['@']),False)







