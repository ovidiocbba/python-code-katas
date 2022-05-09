import codewars_test as test

from sevenkyu.are_the_numbers_in_order import in_asc_order


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basics():
        # Array of 2 integers
        arr = [1, 2]
        test.assert_equals(in_asc_order(arr), True)

        arr = [2, 1]
        test.assert_equals(in_asc_order(arr), False)

        # Array of 3 integers
        arr = [1, 2, 3]
        test.assert_equals(in_asc_order(arr), True)

        arr = [1, 3, 2]
        test.assert_equals(in_asc_order(arr), False)

        # More complex cases
        arr = [1, 4, 13, 97, 508, 1047, 20058]
        test.assert_equals(in_asc_order(arr), True)

        arr = [56, 98, 123, 67, 742, 1024, 32, 90969]
        test.assert_equals(in_asc_order(arr), False)
