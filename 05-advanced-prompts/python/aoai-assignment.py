from flask import Flask, request
import html

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', 'World')
    safe_name = html.escape(name)
    return f'Hello, {safe_name}!'

if __name__ == '__main__':
    app.run()