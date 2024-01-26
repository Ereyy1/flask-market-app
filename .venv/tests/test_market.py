
def test_home(client):
    response = client.get('/home')
    assert b"Market" in response.data