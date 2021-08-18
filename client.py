import json

import fitbit

import gather_keys_oauth2 as Oauth2


def get_client() -> fitbit.Fitbit:
    with open('secret_config.json') as json_file:
        data = json.load(json_file)
    CLIENT_ID = data['client_id']
    CLIENT_SECRET = data['client_secret']
    REDIRECT_URL = data['redirect_url']
    server = Oauth2.OAuth2Server(CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)
    server.browser_authorize()
    ACCESS_TOKEN = str(server.fitbit.client.session.token['access_token'])
    REFRESH_TOKEN = str(server.fitbit.client.session.token['refresh_token'])
    auth2_client = fitbit.Fitbit(CLIENT_ID, CLIENT_SECRET, oauth2=True, access_token=ACCESS_TOKEN,
                                 refresh_token=REFRESH_TOKEN)
    return auth2_client

