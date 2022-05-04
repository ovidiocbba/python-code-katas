import codewars_test as test

from sevenkyu.higher_order_functions_series_1 import count_developers


@test.describe("Example")
def basic_tests():
    @test.it("test case")
    def basic_test_cases():
        list1 = [
            {'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
             'language': 'JavaScript'},
            {'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
             'language': 'JavaScript'},
            {'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35,
             'language': 'HTML'},
            {'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
             'language': 'CSS'}
        ]

        list2 = [
            {'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19,
             'language': 'HTML'},
            {'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89,
             'language': 'HTML'}
        ]

        test.assert_equals(count_developers(list1), 1)
        test.assert_equals(count_developers(list2), 0)
