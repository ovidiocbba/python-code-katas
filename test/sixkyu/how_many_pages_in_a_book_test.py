import codewars_test as test

from sixkyu.how_many_pages_in_a_book import amount_of_pages


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(amount_of_pages(5), 5)
        test.assert_equals(amount_of_pages(25), 17)
        test.assert_equals(amount_of_pages(1095), 401)
        test.assert_equals(amount_of_pages(185), 97)
        test.assert_equals(amount_of_pages(660), 256)
