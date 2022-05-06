import codewars_test as test

from sevenkyu.battle_of_the_characters import battle


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basics():
        test.assert_equals(battle("AAA", "Z"), "Z", "Unfair fight!")
        test.assert_equals(battle("ONE", "TWO"), "TWO", "Unfair fight!")
        test.assert_equals(battle("ONE", "NEO"), "Tie!", "Unfair fight!")
        test.assert_equals(battle("FOUR", "FIVE"), "FOUR", "Unfair fight!")
