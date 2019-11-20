from onp_translation import to_onp
import unittest

class TestONP(unittest.TestCase):

    def test_1(self):
        data = "a p/1"
        output_program = to_onp(data.split())
        output_to_be = "p(a)"
        self.assertEqual(output_program, output_to_be)
        print(f"test 1\ndata:             {data}\nprogram output:   {output_program}\noutput to be:     {output_to_be}\n")

    def test_2(self):
        data = "Z Z p/1 EXISTS"
        output_program =to_onp(data.split())
        output_to_be =  "(EXISTS Z p(Z))"
        self.assertEqual(output_program, output_to_be)
        print(f"test 2\ndata:             {data}\nprogram output:   {output_program}\noutput to be:     {output_to_be}\n")

    def test_3(self):
        data = "Z X X a f/2 p/1 EXISTS Y Y Z f/1 p/2 FORALL IMPLIES FORALL"
        output_program = to_onp(data.split())
        output_to_be ="(FORALL Z ((EXISTS X p(f(X, a))) IMPLIES (FORALL Y p(Y, f(Z)))))"
        self.assertEqual(output_program, output_to_be)
        print(f"test 3\ndata:             {data}\nprogram output:   {output_program}\noutput to be:     {output_to_be}\n")

    def test_4(self):
        data = "Z Y X X b c q/3 Z Y f/1 p/2 ~ & EXISTS FORALL EXISTS"
        output_program =to_onp(data.split())
        output_to_be = "(EXISTS Z (FORALL Y (EXISTS X (q(X, b, c) & (~ p(Z, f(Y)))))))"
        self.assertEqual(output_program, output_to_be)
        print(f"test 4\ndata:             {data}\nprogram output:   {output_program}\noutput to be:     {output_to_be}\n")


if __name__ == '__main__':
    unittest.main()
