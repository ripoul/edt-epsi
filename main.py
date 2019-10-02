from datetime import date
from flask import Flask, escape, request, redirect

app = Flask(__name__)


@app.route('/', defaults={'user_id': "jules.lebris"})
@app.route('/<user_id>')
def index(user_id):
    today = date.today()

    url = "https://edtmobiliteng.wigorservices.net//WebPsDyn.aspx?action=posEDTBEECOME&serverid=C&Tel={idUser}&date={date}".format(
        idUser=user_id, date=today.strftime("%m/%d/%Y")
    )

    return redirect(url)

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
