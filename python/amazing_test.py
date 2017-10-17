import amazing
import random
import unittest

class TestAmazing(unittest.TestCase):

    def testSeed0size15x20(self):
        expected = """Amazing - Copyright by Creative Computing, Morristown, NJ
:--:--:--:--:--:--:--:--:  :--:--:--:--:--:--:
I                       I                    I 
:  :--:  :--:--:--:--:  :  :--:--:--:--:--:  :
I     I           I     I                 I  I 
:--:  :--:--:--:  :--:--:--:--:--:--:--:  :  :
I     I        I     I           I     I  I  I 
:--:  :--:--:  :  :  :  :  :--:--:  :  :  :--:
I     I        I  I     I     I     I        I 
:  :--:  :--:--:  :--:  :--:  :  :--:--:--:  :
I     I     I  I     I  I     I  I        I  I 
:--:  :--:  :  :--:  :  :--:--:  :--:--:  :  :
I  I     I     I     I           I     I  I  I 
:  :  :  :  :  :  :--:--:  :--:--:  :  :  :  :
I  I  I     I  I        I     I     I     I  I 
:  :--:--:  :--:  :--:  :  :--:  :--:--:--:  :
I           I     I     I  I     I           I 
:--:--:  :--:  :--:  :--:--:  :--:  :--:--:--:
I     I  I        I        I     I  I        I 
:  :  :--:  :--:  :--:--:  :--:  :  :  :--:  :
I  I        I  I  I     I  I     I  I     I  I 
:  :--:--:--:  :  :  :  :  :  :--:  :--:  :--:
I           I  I     I  I  I     I  I  I     I 
:  :--:--:  :  :  :--:--:  :  :  :  :  :--:  :
I     I        I  I        I  I  I     I     I 
:--:  :  :--:--:--:  :--:--:  :--:  :--:  :--:
I     I     I     I     I  I     I     I     I 
:  :--:--:  :  :  :--:  :  :  :  :--:  :--:  :
I  I     I     I     I     I  I  I           I 
:  :  :--:  :--:--:--:--:--:  :--:  :--:--:  :
I  I        I        I        I     I     I  I 
:  :--:--:--:  :  :  :  :--:--:  :--:  :  :--:
I              I  I  I        I        I     I 
:  :--:--:--:--:--:  :--:--:  :--:  :--:--:  :
I     I        I     I     I     I     I     I 
:--:  :  :--:--:  :--:  :--:  :  :--:--:  :--:
I              I     I     I  I        I     I 
:--:--:--:--:  :  :  :--:  :  :--:--:  :--:  :
I              I  I     I  I        I     I  I 
:  :--:--:--:--:--:--:  :  :--:--:--:  :  :  :
I                    I                 I  I  I 
:--:--:--:--:--:--:--:--:--:--:--:--:--:--:  :"""
        random.seed(0)
        Amazing.doit(15, 20)
        self.assertEqual(expected, result.to_s)

    def testSeed100size4x5(self):
        expected = """Amazing - Copyright by Creative Computing, Morristown, NJ
:--:--:  :--:
I           I 
:  :--:--:  :
I  I     I  I 
:  :  :  :  :
I     I  I  I 
:  :--:  :  :
I  I     I  I 
:  :  :--:  :
I  I  I     I 
:--:  :--:--:"""
        random.seed(100)
        Amazing.doit(4, 5)
        self.assertEqual(expected, result.to_s)

