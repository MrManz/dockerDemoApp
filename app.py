from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hallo aus Container"

if __name__ == "__main__":
    app.run(port=80)