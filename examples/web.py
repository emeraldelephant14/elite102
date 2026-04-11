from flask import Flask

def main():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "Hello, World!"

    app.run(host='0.0.0.0', debug=True)

if __name__ == "__main__":
    main()
