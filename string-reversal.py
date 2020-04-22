#!/usr/bin/python3

import unittest

def debug(s):
    print("Debug: {}".format(s))
    pass

class TestReversalInPlace(unittest.TestCase):
    def test_emptyString(self):
        s = ""
        res = ReversalInPlace(s).reverse()

        self.assertEqual(res, "")
    
    def test_nonemptyStringOdd(self):
        s = "cat"
        res = ReversalInPlace(s).reverse()

        self.assertEqual(res, "tac")
    
    def test_nonemptyStringEven(self):
        s = "cats"
        res = ReversalInPlace(s).reverse()

        self.assertEqual(res, "stac")

class TestReversalPerWord(unittest.TestCase):
    def test_emptyString(self):
        s = ""
        res = ReversalPerWord(s).reverse()

        self.assertEqual(res, "")

    def test_nonemptyString(self):
        s = "cats are pretty cool"
        res = ReversalPerWord(s).reverse()

        self.assertEqual(res, "stac era ytterp looc")

    def test_multispacedWords(self):
        s = "cats   are pretty     cool"
        res = ReversalPerWord(s).reverse()

        self.assertEqual(res, "stac   era ytterp     looc")

class ReversalInPlace:
    def __init__(self, s):
        self.str = s
        self.lst = list(s)
    
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

class ReversalPerWord:
    def __init__(self, s):
        self.str = s

    def reverse(self):
        words = self.str.split(" ")

        return " ".join([ReversalInPlace(w).reverse() for w in words])


def main():
    s = "cats   are pretty     cool"
    print(ReversalInPlace(s).reverse())
    print(ReversalPerWord(s).reverse())

if __name__ == "__main__":
    unittest.main(exit=False)
    main()