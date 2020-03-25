def auth():
    api = twitter.Api(consumer_key='your_consumer_key',
                        consumer_secret='your_consumer_secret',
                        access_token_key='your_access_token_key',
                        access_token_secret='your_access_token_secret')

def get_msg():
    api = auth()
    response = api.GetSearch(term="teste")
    for r in response:
        print(r.__getattribute__('text'))

if __name__ == "__main__":
    get_msg()
