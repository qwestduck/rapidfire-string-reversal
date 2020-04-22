#!/usr/bin/python3

import unittest

def debug(str):
    print("Debug: {}".format(str))

class TestReversalInPlace(unittest.TestCase):
    def test_emptyString(self):
        str = ""
        res = ReversalInPlace(str).reverse()

        self.assertEqual(res, "")
    
    def test_nonemptyStringOdd(self):
        str = "cat"
        res = ReversalInPlace(str).reverse()

        self.assertEqual(res, "tac")
    
    def test_nonemptyStringEven(self):
        str = "cats"
        res = ReversalInPlace(str).reverse()

        self.assertEqual(res, "stac")

class ReversalInPlace:
    def __init__(self, str):
        self.str = str
        self.lst = list(str)
    
    def reverse(self):
        ret = self.lst

        r = range(0, int(len(ret) / 2))
        debug("range -> {}".format(str(r)))

        for i in r:
            j = -(i + 1)
            c = ret[j]
            ret[j] = ret[i]
            ret[i] = c
        
        return ''.join(ret)

def main():
    str = "cat"
    print(ReversalInPlace(str).reverse())

if __name__ == "__main__":
    unittest.main(exit=False)
    main()