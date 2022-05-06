import codewars_test as test

from sevenkyu.list_filtering import filter_list


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(filter_list([1, 2, 'a', 'b']), [1, 2], 'For input [1, 2, "a", "b"]')
        test.assert_equals(filter_list([1, 'a', 'b', 0, 15]), [1, 0, 15], 'Fot input [1, "a", "b", 0, 15]')
        test.assert_equals(filter_list([1, 2, 'aasf', '1', '123', 123]), [1, 2, 123],
                           'For input [1, 2, "aasf", "1", "123", 123]')
