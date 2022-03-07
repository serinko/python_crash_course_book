import unittest

from try_yourself_11_1_city_country import get_cities_formatted


class CitiesTestCase(unittest.TestCase):
    """Test for city_country"""

    def test_city_country(self):
        """Do items like Rome, Italy work?"""

        cities_formatted = get_cities_formatted('rome', 'italy')
        self.assertEqual(cities_formatted, 'Rome, Italy')

    def test_city_country_population(self):
        """Does city, country - population come out"""
        cities_formatted = get_cities_formatted(
            'rome',
            'italy',
            5000000
        )
        self.assertEqual(cities_formatted,
                         'Rome, Italy - Population 5000000'
                         )


if __name__ == '__main__':
    unittest.main()
