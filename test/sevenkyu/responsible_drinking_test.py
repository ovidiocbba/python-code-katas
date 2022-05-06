import codewars_test as test

from sevenkyu.responsible_drinking import hydrate


@test.describe("Tests")
def basic_tests():
    @test.it("Basic test cases")
    def basic_test_cases():
        test.assert_equals(hydrate("1 beer"), "1 glass of water")
        test.assert_equals(hydrate("1 shot, 5 beers, 2 shots, 1 glass of wine, 1 beer"), "10 glasses of water")
