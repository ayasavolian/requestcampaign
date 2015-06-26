import marketo_wrapper
import settings

if __name__ == "__main__":
    munchkin = settings.MUNCHKIN
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    marketo = MarketoWrapper(munchkin, client_id, client_secret)
    
    id = 1263
    tokens = [  {
                    "name": "{{my.URL}}",
                    "value": INSERT HERE
                }
             ]
    marketo.schedule_campaign(id, tokens)