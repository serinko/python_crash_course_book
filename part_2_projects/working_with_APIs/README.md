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

**Steps:**
+check python_repos_visual.py*

1. import:  import Bar from plotly.graph_objs, and from plotly import offline
2. no need to import the Layout as we use the dict approach
3. print the API status to see if there is no problem (200 return is good)
4. create two lists (values later used in axis)
5. name of each project to label the bars
6. in the loop append each name and the number of stars
7. define the data list, containing the dictionary, type of plot, data for x and y values, # of stars
8. define the layout for this chart usig the dictionary approach
9. define a title and label for each axis

## Refining Plotly Charts
We can add all the styling directives as key-value pairs in the data and my_layout dictionaries.
Changes affect the bars. Ie color, clear border etc

- Marker settings affect the design of the bars:
```python
# --snip--
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {
            'width': 1.5,
            'color': 'rgb(25,25,25)',
        },
    },
    'opacity': 0.6,
}]
# --snip--
```
- my_layout modifies the titles and ticks settings:
```python
# --snip--
my_layout = {
    'title': 'Most-Starred Python Projects on Github',
    'titlefont': {'size': 30},
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    }
}
# --snip--
```
## Adding Custom Tooltips
Tooltip is the information showed when hover over a bar in plotly
- Add annother list with the info you want to have for tooltips - 'labels'
- define a label - in our case owner and description
- fill the list with the defined labels

```python
# --snip--
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
    
    owner = repo_dict['owner']['login']
    decription = repo_dict['description']
    label = f"{owner}<br />{decription}"
    labels.append(label)
    
```
- Add this list to the data seetings:
```python
# --snip--
# Make visualisation
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext':labels,
    'marker': {
# --snip--
```
## Adding Clickable Links to the Graph
Plotly allows to use HTML on text elements - we can add links to the chart.

- In this case, we use x-axis labels:

```python
# --snip--
# Process results
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    decription = repo_dict['description']
    label = f"{owner}<br />{decription}"
    labels.append(label)

# --snip--

# Make visualisation
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
# --snip--
```

**Steps:**
1. update the name of the list to 'repo_links'
2. pull the URL from the project and asign it to a temporary variable repo_url
3. use HTML anchor tag *'f"<a href='{repo_url}'>{repo_name}</a>"'*
4. append this link to the list of repo links
5. update the list name in x-values for the new one

## Notes: Plotly, Github API

**Links**:

- [Plotly user guide](https://plot.ly/python/reference/) list all the settings
- [GitHub API dpcumentation](https://developer.github.com/v3/) offers all kinda specific information from GitHub.

# The Hacker News API

- [Hacker News](https://news.ycombinator.com/) is a website where people share articles about programming, technology and discuss.
- The API (no registration required) providdes access to all the data.
  - Ie current top articles: *https://hacker-news.firebaseio.com/v0/item/item/19155826.json*

## Download, format and a dictionary from Hacker News API
```python
import requests
import json

# Make an API call and store the response
url = \
    'https://hacker-news.firebaseio.com/v0/item/item/19155826.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data:
response_dict = r.json()
readable_file = 'readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
```
As previously done - this code will download a JSON file with dictionary, save it and reformat it with a correct indentation.

## Work with Submissions - Hacker NEws

```python
from operator import itemgetter
import requests

# Make an API call and store the response
url = \
    'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts,
    key=itemgetter('comments'),
    reverse=True,
)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

**Steps:**
1. Make an API call, print the status of the reponse. It is a list of IDs containing the 500 most popular articles.
2. Convert the response to a Python list stored as *submission_ids* - these IDs will be used to get information about each submission
3. Set up an empty list called *submission_dicts*
4. Loop through the top 30 submission IDs
5. Make a new API call for each of them by generating a URL containing the ID#
6. Print the status to see if each of them was successful or not
7. Create a dict for submission currently processed: store title, discussion link, number of comments
8. append each *submission_dict* to the list of *submission_dicts*
9. sort the list according the amount of comments using function *itemgetter()* from the *operator module*. PAss the function the key *'comments'* - it pulls the value from each dict associatted with that key.
10. *sorted()* function uses this value as a basis to sort the list
11. Sort the list in reverse order to place the most commented stories onthe top.
12. Once store - loop through the list and print out the information you want (in the example: the title, link to discussion page and the number of comments)

**Note:**

Similar proccess to access and analyze information with any API. To learn more about what kind of information you can access on the Hacker News, visit:
[github.com/HackerNews/API/](https://github.com/HackerNews/API/)