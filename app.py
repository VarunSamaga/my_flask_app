from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<img src="https://cdn.britannica.com/39/226539-050-D21D7721/Portrait-of-a-cat-with-whiskers-visible.jpg">'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
