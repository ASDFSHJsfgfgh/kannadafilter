from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'https://t.me/askanymovie6666'


if __name__ == "__main__":
    app.run()