import codewars_test as test

from sevenkyu.kill_the_monsters import kill_monsters


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(kill_monsters(50, 7, 10), "hits: 2, damage: 20, health: 30", "For input (50, 7, 10)")
        test.assert_equals(kill_monsters(20, 1, 10), "hits: 0, damage: 0, health: 20", "For input (20, 1, 10)")
        test.assert_equals(kill_monsters(30, 4, 50), "hero died", "For input (30, 4, 50)")
        test.assert_equals(kill_monsters(42, 30, 2), "hits: 9, damage: 18, health: 24", "For input (42, 30, 2)")
        test.assert_equals(kill_monsters(10, 7, 5), "hero died", "For input (10, 7, 5)")
