import json

def test_get_episodes(client, seed_data):
    response = client.get('/episodes')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 2

def test_get_episode_by_id(client, seed_data):
    eid = seed_data['episodes'][0].id
    response = client.get(f'/episodes/{eid}')
    data = response.get_json()
    assert response.status_code == 200
    assert data['id'] == eid

def test_get_episode_not_found(client):
    response = client.get('/episodes/999')
    assert response.status_code == 404

def test_delete_episode(client, seed_data):
    eid = seed_data['episodes'][0].id
    response = client.delete(f'/episodes/{eid}')
    assert response.status_code == 204
    # Confirm deletion
    response = client.get(f'/episodes/{eid}')
    assert response.status_code == 404

def test_get_guests(client, seed_data):
    response = client.get('/guests')
    data = response.get_json()
    assert response.status_code == 200
    assert len(data) == 2

def test_post_appearance(client, seed_data):
    g_id = seed_data['guests'][0].id
    e_id = seed_data['episodes'][1].id
    response = client.post('/appearances', 
                           json={'rating': 5, 'episode_id': e_id, 'guest_id': g_id})
    data = response.get_json()
    assert response.status_code == 201
    assert data['rating'] == 5

def test_post_appearance_validation_error(client):
    response = client.post('/appearances', 
                           json={'rating': 10, 'episode_id': 1, 'guest_id': 1})
    assert response.status_code == 400
