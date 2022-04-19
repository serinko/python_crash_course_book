import requests
import unittest
import python_repos as pr

# Make an API call and store the response
url = \
    'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers)

# Store API response
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories:
repo_dicts = response_dict['items']


class PythonReposTestCase(unittest.TestCase):

    def test_status_code(self, st_cd=200):
        """Correct status code return is 200 on http"""
        status_code = r.status_code
        self.assertEqual(status_code, st_cd)

    def test_repositories_returned(self, rep_rtn=30):
        """We expect GH to return only 30 best rated repos"""
        rtrn_repos = len(repo_dicts)
        self.assertEqual(rtrn_repos, rep_rtn)


if __name__ == '__main__':
    unittest.main()
