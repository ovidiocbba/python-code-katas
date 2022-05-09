import codewars_test as test

from sevenkyu.filter_long_words import filter_long_words


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(filter_long_words("The quick brown fox jumps over the lazy dog", 4),
                           ['quick', 'brown', 'jumps'])
