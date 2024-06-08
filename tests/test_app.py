from unittest.mock import patch

def test_predict_endpoint(client):
    with patch('app.main.model_predict', return_value = 1):
        response = client.get('/predict?amt=1&merchant_1=2&merchant_2=3&category=4&year=5&city_pop=6')
        assert response.status_code == 200
        assert b'It is a fraud!' in response.data

    with patch('app.main.model_predict', return_value = 0):
        response = client.get('/predict?amt=1&merchant_1=2&merchant_2=3&category=4&year=5&city_pop=6')
        assert response.status_code == 200
        assert b'It is not a fraud!' in response.data