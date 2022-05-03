import codewars_test as test

from sevenkyu.parts_of_a_list import part_list


@test.describe("Parts")
def basic_tests():
    @test.it("Basic tests")
    def basics():
        test.assert_equals(part_list(["I", "wish", "I", "hadn't", "come"]),
                           [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"),
                            ("I wish I hadn't", "come")])
        test.assert_equals(part_list(["cdIw", "tzIy", "xDu", "rThG"]),
                           [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
        test.assert_equals(part_list(["vJQ", "anj", "mQDq", "sOZ"]),
                           [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])
