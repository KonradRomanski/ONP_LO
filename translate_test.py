import unittest
from translate import to_onp


class TestONP(unittest.TestCase):

    def test_1(self):
        actual, expected = to_onp("a p/1".split()), "p(a)"
        self.assertEqual(expected, actual)

    def test_2(self):
        actual, expected = to_onp("Z Z p/1 EXISTS".split()), "(EXISTS Z p(Z))"
        self.assertEqual(expected, actual)

    def test_3(self):
        actual, expected = to_onp(
            "Z X X a f/2 p/1 EXISTS Y Y Z f/1 p/2 FORALL IMPLIES FORALL".split()), "(FORALL Z ((EXISTS X p(f(X, a))) IMPLIES (FORALL Y p(Y, f(Z)))))"
        self.assertEqual(expected, actual)

    def test_4(self):
        actual, expected = to_onp(
            "Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS".split()), "(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))"
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
