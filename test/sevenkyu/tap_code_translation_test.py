import codewars_test as test

from sevenkyu.tap_code_translation import tap_code_translation


@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(tap_code_translation("breaks"), ". .. .... .. . ..... . . . ... .... ...")
        test.assert_equals(tap_code_translation("taps"), ".... .... . . ... ..... .... ...")
        test.assert_equals(tap_code_translation("knocks"), ". ... ... ... ... .... . ... . ... .... ...")
