from flask import Flask, render_template, request, url_for, flash, redirect
import json
import re

app = Flask(__name__)
# DO NOT COMMIT
app.config['SECRET_KEY'] = <secret_key>

def load_provider_data(provider_id):
    with open(f"providers-json/{provider_id}.json") as f:
        return json.load(f)

def update_provider_data(provider_id, data):
    with open(f"providers-json/{provider_id}.json", "w") as f:
        json.dump(data, f)

def update_provider_admins(data, new_admin_list):
    data["administrators"] = new_admin_list
    return data

def verify_crsids(admin_list):
    pattern = r'^[a-zA-Z]+\d+$'

    for crsid in admin_list:
        if re.match(pattern, crsid):
            continue
        else:
            return False
        
    return True

def santisie_crsid_list(string):
    """This function takes the string from the flask form and strips anything that isn't a number, letter, or newline character.
    It returns the list of crsids."""

    new_string = re.sub(r'[^a-zA-Z0-9\n]', '', string)
    return new_string.split("\n")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update', methods=('GET', 'POST'))
def update():
    provider_data = load_provider_data('test_provider')
    
    if request.method == "POST":
        admin_list = request.form["admin_list"]
        admin_list_sanitised = santisie_crsid_list(admin_list)
        
        if verify_crsids(admin_list_sanitised) == False:
            flash("Invalid CRSIDs. You must not include any special characters or the email domain. Example: abc123 not abc123@cam.ac.uk")

        elif len(admin_list_sanitised) == 0:
            flash("Admin list cannot be empty")
        
        elif provider_data["administrators"] == admin_list_sanitised:
            flash("Admin list identical: no changes made")
        
        else:
            provider_data = update_provider_admins(provider_data, admin_list_sanitised)
            update_provider_data('test_provider', provider_data)
            print(f"Updated provider admins to: {provider_data['administrators']}")
            return redirect(url_for('index'))

    return render_template('update.html', provider_name=provider_data["name"], current_admins="\n".join(provider_data["administrators"]), provider_image=provider_data["organisations"][provider_data["id"]]["logoLocation"])
