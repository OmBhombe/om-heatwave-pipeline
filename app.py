
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Heatwave Risk Checker</h1>
    <p>Current Temperature: 42°C</p>
    <p>Risk Level: High</p>
    """

if __name__ == "__main__":
    app.run()
