import codewars_test as test

from sixkyu.fire_and_fury import fire_and_fury


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(fire_and_fury("FURYYYFIREYYFIRE"), "I am furious. You and you are fired!")
        test.assert_equals(fire_and_fury("FIREYYFURYYFURYYFURRYFIRE"),
                           "You are fired! I am really furious. You are fired!")
        test.assert_equals(fire_and_fury("FYRYFIRUFIRUFURE"), "Fake tweet.")
