# Tests for your routes go here
"""
When: I make a GET request to /
Then: I should get a 200 response
"""
def test_get_wave(web_client):
    # We'll simulate sending a GET request to /wave?name=Dana
    # This returns a response object we can test against.
    response = web_client.get('/wave?name=Dana')

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'I am waving at Dana'

"""
When: I make a POST request to /submit
And: I send a name and message as body parameters
Then: I should get a 200 response with the right content
"""
def test_post_submit(web_client):
    # We'll simulate sending a POST request to /submit with a name and message
    # This returns a response object we can test against.
    response = web_client.post('/submit', data={'name': 'Dana', 'message': 'Hello'})

    # Assert that the status code was 200 (OK)
    assert response.status_code == 200

    # Assert that the data returned was the right string
    assert response.data.decode('utf-8') == 'Thanks Dana, you sent this message: "Hello"'

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
When: I make a POST request to /sort-names
And: I send 'Joe,Alice,Zoe,Julia,Kieran' as the body parameter names
Then: I should get a 200 response back with the names sorted alphabetically
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data={'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'

"""
When: I make a POST request to /sort-names
And: I send 'Matt,Jess,Ollie,Tom,Holly' as the body parameter names
Then: I should get a 200 response back with the names sorted alphabetically
"""
def test_post_sort_names_2(web_client):
    response = web_client.post('/sort-names', data={'names': 'Matt,Jess,Ollie,Tom,Holly'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Holly,Jess,Matt,Ollie,Tom'

# GET /names?add=Matt
# Expected ressponse (200 OK):
# """
# Alice, Julia, Karim, Matt
# """
def test_get_names_add_one_name(web_client):
    response = web_client.get('/names?add=Matt')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Julia, Karim, Matt'

# GET /names?add=Eddie
# Expected ressponse (200 OK):
# """
# Alice, Eddie, Julia, Karim
# """
def test_get_names_add_one_name_2(web_client):
    response = web_client.get('/names?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim'

# GET /names?add=Matt,Zac,Eddie
# Expected response (200 OK)
# """
# Alice, Eddie, Julia, Karim, Matt, Zac
# """
def test_get_names_add_multiple_names(web_client):
    response = web_client.get('/names?add=Matt,Zac,Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Eddie, Julia, Karim, Matt, Zac'

# GET /names
# Expected response (400)
# """
# You didn't submit any names!
# """
def test_get_names_with_no_names(web_client):
    response = web_client.get('/names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't submit any names!"