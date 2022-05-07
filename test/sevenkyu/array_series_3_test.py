import codewars_test as test

from sevenkyu.array_series_3 import array_leaders


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basics():
        test.it("Positive Values")
        test.assert_equals(array_leaders([1, 2, 3, 4, 0]), [4])
        test.assert_equals(array_leaders([16, 17, 4, 3, 5, 2]), [17, 5, 2])
        test.it("Negative Values")
        test.assert_equals(array_leaders([-1, -29, -26, -2]), [-1])
        test.assert_equals(array_leaders([-36, -12, -27]), [-36, -12])
        test.it("Mixed Values")
        test.assert_equals(array_leaders([5, 2]), [5, 2])
        test.assert_equals(array_leaders([0, -1, -29, 3, 2]), [0, -1, 3, 2])
