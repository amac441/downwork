import upwork

public_key='8b4e214913168000580280e93e9a2b66'
secret_key='5a38eba13351a43d'
client = upwork.Client(public_key, secret_key)
client.auth.get_request_token()
data = {'q': 'python', 'title': 'Web Developer'}
response=client.provider_v2.search_providers(data=data, page_offset=0, page_size=20)
a=1