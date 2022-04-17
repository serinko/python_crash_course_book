# Dependencies
- The request package
`$ python -m pip install --user requests`

# Procesing an API Response
```python
import requests

# Make an API call and store the response
url = \
    'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

# Store API response
response_dict = r.json()

# Process results
print(response_dict.keys())
```
**Steps:**

1. import the request module
2. store URL of the APIcall in the variable
3. define the current version of API (3)
4. use request and call get(), pass the URL and the header and store to a variable
5. print the value of status_code - response object has an attribute called status_code - status code 200 tells that the request was successful
6. API returns it in JSON so we use json() to convert the info to Python dictionary
7. we store the dictionary in response_dict

# Working with the Response Dictionary
There is many info coming from API - to understand it all one need to read the documentation or work through it with a code.
We can work with the data stored as dictionary from previous step

```python 
# --snip--
# Store API response
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories:
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

**Steps:**

1. print value of 'total_count' - total number of Python repos on github
2. 'items' - dict's each containing data about an individual Python repo
3. print length of repo_dicts 
4. pull first item and store in and store it in repo_dict to look closer
5. print # keys in the dict to see how much info is there
6. print all dict keys to see what kind of info is included

We can code a template of info we are interested and then just feed it with different dict (index of dicts):
```python
# --snip--
repo_dict = repo_dicts[0]
print("\nSelected information about first repository: ")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
```
## Sumarizing the Top Repositories

```python
# --snip--
# Sumarizing all the top repos
print("\nSelected information about each repository")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository: ")
# --snip--
```
# API Rate Limit on GH
Check [api.github.com/rate_limit](https://api.github.com/rate_limit)
To see your request limit/left rate.

**Note:**

Many APIs require you to register and obtain an API key to make API calls.

# Visualising Repositories Using Plotly
We can visualize anything - at this example will visualize relative popularity of Python projects on GitHub.

An interactive bar chart:
- each bar represents the # stars of the project
- also works as an interactive link
- it is a good template for other use

