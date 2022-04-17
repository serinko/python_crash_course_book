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
r = requests.get(url, headers, headers)
print(f"Status code: {r.status_code}")

# Store API response
response_dict = r.json()

```
