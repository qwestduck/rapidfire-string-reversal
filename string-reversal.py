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

class TestReversalWordSwap(unittest.TestCase):
    def test_emptyString(self):
        s = ""
        res = ReversalWordSwap(s).reverse()

        self.assertEqual(res, "")

    def test_nonemptyString(self):
        s = "cats are neat"
        res = ReversalWordSwap(s).reverse()

        self.assertEqual(res, "neat are cats")

    def test_multispacedWords(self):
        s = "cats   are pretty     cool"
        res = ReversalWordSwap(s).reverse()

        self.assertEqual(res, "cool   pretty are     cats")

class ReversalInPlace:
    def __init__(self, s):
        if type(s) is str:
            self.str = s
            self.lst = list(s)

        if type(s) is list:
            self.lst = s[:]

    def reverse(self, sep=''):
        ret = self.lst

        r = range(0, int(len(ret) / 2))
        debug("range -> {}".format(str(r)))

        for i in r:
            j = -(i + 1)
            c = ret[j]
            ret[j] = ret[i]
            ret[i] = c
        
        return sep.join(ret)

class ReversalPerWord:
    def __init__(self, s):
        self.str = s

    def reverse(self):
        words = self.str.split(" ")

        return " ".join([ReversalInPlace(w).reverse() for w in words])

class ReversalWordSwap:
    def __init__(self, s):
        self.str = s

    def reverse(self):
        ret = []

        words = self.str.split(' ')

        words_nospace = self.str.split()
        rev_words_nospace = ReversalInPlace(words_nospace).reverse(' ').split(' ')

        i = 0
        for w in words:
            if w != '':
                ret.append(rev_words_nospace[i])
                i = i + 1
            else:
                ret.append('')

        return " ".join(ret)

def main():
    s = "cats   are pretty     cool"

    print(s)
    print()
    print(ReversalInPlace(s).reverse())
    print(ReversalPerWord(s).reverse())
    print(ReversalWordSwap(s).reverse())

if __name__ == "__main__":
    unittest.main(exit=False)
    main()