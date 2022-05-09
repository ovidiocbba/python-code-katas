import codewars_test as test

from sevenkyu.password_hashes import pass_hash


@test.describe("Tests")
def basic_tests():
    @test.it("Basic tests")
    def basics():
        test.assert_equals(pass_hash('password'), '5f4dcc3b5aa765d61d8327deb882cf99');
        test.assert_equals(pass_hash('abc123'), 'e99a18c428cb38d5f260853678922e03');
