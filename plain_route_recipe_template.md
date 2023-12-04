# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Sort names route
POST /sort-names
  names: string

# Names route
GET /names?add=<string>
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /sort-names
# Parameters:
#   names: Joe,Alice,Zoe,Julia,Kieran
# Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# GET /names?add=Matt
# Expected ressponse (200 OK):
"""
Alice, Julia, Karim, Matt
"""

# GET /names?add=Eddie
# Expected ressponse (200 OK):
"""
Alice, Eddie, Julia, Karim
"""

# GET /names?add=Matt, Zac, Eddie
# Expected response (200 OK)
"""
Alice, Eddie, Julia, Karim, Matt, Zac
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /sort-names
Parameters:
  names: Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK):
  "Alice,Joe,Julia,Kieran,Zoe"
"""
def test_post_sort_names(web_client):
  response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
  assert response.status_code == 200
  assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

```

<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fweb-applications-in-python&prefill_File=resources%2Fplain_route_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
