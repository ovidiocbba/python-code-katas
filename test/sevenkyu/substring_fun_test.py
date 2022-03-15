import codewars_test as test

from sevenkyu.substring_fun import nth_char


@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(nth_char(['yoda', 'best', 'has']), 'yes')
        test.assert_equals(nth_char([]), '')
        test.assert_equals(nth_char(['X-ray']), 'X')
        test.assert_equals(nth_char(['No', 'No']), 'No')
        test.assert_equals(
            nth_char(['Chad', 'Morocco', 'India', 'Algeria', 'Botswana', 'Bahamas', 'Ecuador', 'Micronesia']),
            'Codewars')
