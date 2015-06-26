from flask import Flask, render_template
import httplib2
from urllib import urlencode
import marketo_wrapper
import settings

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('home.html')

@app.route("/test")
def test():
  print "not in"
  munchkin = settings.MUNCHKIN
  client_id = settings.CLIENT_ID
  client_secret = settings.CLIENT_SECRET
  print "about to create object"
  marketo = marketo_wrapper.MarketoWrapper(munchkin, client_id, client_secret)
  print "object created"
  camp_id = "1263"
  tokens = [  {
                  "name": "{{my.URL}}",
                  "value": "http://www.marketaxess.com/research/blog/single.php?permalink=open%20trading%20offers%20new%20trading%20opportunities%20in%20the%20high-yield%20markets#.VY2euxNViko"
              }
           ]
  marketo.schedule_campaign(camp_id, tokens)
  print "finished"
if __name__ == '__main__':
    app.run()