import unittest

from try_yourself_11_1_city_country import get_cities_formatted


class CitiesTestCase(unittest.TestCase):
    """Test for city_country"""

    def test_city_country(self):
        """Do items like Rome, Italy work?"""

        cities_formatted = get_cities_formatted('rome', 'italy')
        self.assertEqual(cities_formatted, 'Rome, Italy')


if __name__ == '__main__':
    unittest.main()
