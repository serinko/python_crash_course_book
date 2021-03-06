import matplotlib.pyplot as plt
import requests

from plotly.graph_objs import Bar
from plotly import offline
import matplotlib.pyplot as plt

import plotly.express as px

wlcm_msg = "\nPlease choose a GitHub language which will be sorted from the " \
           "top-rated one. Here is a full list of GitHub languages " \
           "https://github.com/github/linguist/blob/master/lib/linguist/languages.yml." \
           "(press 'Q' to exit)"
print(wlcm_msg)
language = input("\nLanguage: ")
if language.lower() == 'q':
    quit()

language_formatted = f"{language.lower()}"

# Make an API call and store the response
url = \
    f'https://api.github.com/search/repositories?q=language:{language_formatted}&sort=stars'
headers = {
    'Accept': 'application/vnd.github.v3+json'
}
r = requests.get(url, headers)
print(f"Status code: {r.status_code}")

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

stars_max = int(repo_dicts[0]['stargazers_count'])

# Make visualisation
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,

    'marker': {
        'cmax': stars_max,
        'cmin': 0,
        'color': stars,
        'colorscale': 'Viridis',

        'line': {
            'width': 1.5,
            'color': 'rgb(25,25,25)',
        },
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': f'Most-Starred {language.title()} Projects on Github',
    'template': 'plotly_dark',
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
    },
}
plt.style.use('seaborn-dark')
fig = {'data': data, 'layout': my_layout}

offline.plot(fig, filename=f'{language}_repos.html')
