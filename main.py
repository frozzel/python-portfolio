from flask import Flask, abort, render_template, redirect, url_for, flash, request


app = Flask(__name__)

@app.route('/')
def index():
    print("Index page accessed")
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    
    