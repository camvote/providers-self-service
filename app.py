from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello(provider_name="Test JCR", current_admins="tes104\nlw664"):
    return render_template('main.html', provider_name=provider_name, current_admins=current_admins)
