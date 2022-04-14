import unittest


def living_people(people):
    '''
    16.10 Living People: Given a list of people with their birth and death years, 
    implement a method to compute the year with the most number of people alive. 
    You may assume that all people were born between 1900 and 2000 (inclusive). 
    If a person was alive during any portion of that year, they should be included 
    in that year's count. For example. Person (birth = 1908, death = 1909) is included 
    in the counts for both 1908 and 1909.
    '''
    years = [(0, 0)] * 200

    for birth_year, death_year in people:
        n_births, n_deaths = years[birth_year - 1900]
        years[birth_year - 1900] = n_births + 1, n_deaths

        n_births, n_deaths = years[death_year - 1900]
        years[death_year - 1900] = n_births, n_deaths + 1

    n_alive = 0
    max_n_alive = 0
    max_index = 0

    for i in range(len(years)):
        n_births, n_deaths = years[i]
        n_alive += n_births

        if n_alive > max_n_alive:
            max_n_alive = n_alive
            max_index = i

        n_alive -= n_deaths

    return 1900 + max_index


class LivingPeopleTest(unittest.TestCase):
    def test_living_people(self):
        people = [
            (1926, 1962), (1963, 1997), (1928, 1939), (1943, 1967), (1958, 2000), 
            (1912, 1922), (1919, 1943), (1929, 1953), (1907, 1953), (1940, 1984), 
            (1998, 2003), (1992, 2033), (1961, 1968), (1969, 1970), (1907, 1952), 
            (1991, 2020), (1959, 2008), (1947, 1991), (1924, 1967), (1965, 2013), 
            (1978, 2008), (1943, 1974), (1972, 1997), (1993, 2031), (1958, 1962), 
            (1926, 1939), (1948, 1950), (1992, 2016), (1996, 2017), (1943, 1956)
        ]
        actual = living_people(people)
        self.assertEqual(1948, actual)


if __name__ == '__main__':
    unittest.main()
