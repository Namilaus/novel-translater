from flask import Flask

app = Flask(__name__)

@app.route("/")
def homePage():

    return """ welcome to 69shu autotranslate. you just need to give the link of the first page of the book you want to be translated:
        like;
        url:url,
        length:200

            """


app.run()
