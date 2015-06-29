from flask import Flask, render_template
import httplib2
import marketo_wrapper
import settings

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route("/test")
def test():
    print("executing")
    munchkin = settings.MUNCHKIN
    client_id = settings.CLIENT_ID
    client_secret = settings.CLIENT_SECRET
    marketo = marketo_wrapper.MarketoWrapper(munchkin, client_id, client_secret)
    print("going going going")
    id = "1263"
    tokens = [  {
                    "name": "{{my.URL}}",
                    "value": "www.marketaxess.com"
                }
             ]
    print(marketo.schedule_campaign(id, tokens))

if __name__ == '__main__':
    app.run()