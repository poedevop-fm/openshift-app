from flask import Flask

app = Flask(_name_)
@app.route("/")
def hello():
    return "hello world"

if __name__ == "__main__":
    app.run()



