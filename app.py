from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    print("App läuft in Container")
    return "Hallo aus Container"

if __name__ == "__main__":
    app.run(port=80)