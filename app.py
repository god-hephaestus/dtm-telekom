import os
from flask import Flask, render_template, session, request, redirect, url_for
# from flask_mail import Mail, Message
app = Flask(__name__)
__ROOTFOLDER__ = os.path.dirname(os.path.abspath(__file__))
print(f"Rootfolder: {__ROOTFOLDER__}")
app.secret_key = 'random string'


###################
#   TRANSLATION   #
###################

translations = [
    [],
    []
]

##################
#    FUNCTION    #
##################

def get_lang():
    try:
        if 'language' not in session:  # if session does not contain a language variable, if it exists no need to manually re-add it on else.
            session["language"] = 0 #1
        return int(session["language"])
    except Exception as e:
        print(e)


@app.route('/set_lang', methods = ['POST'])
def set_lang():
    if request.method == 'POST':
        session["language"] = int(request.form['langval']) # make eng -> eng returns a '1'
    return redirect(url_for('root'))

##################
# ROUTE HANDLING #
##################

@app.route("/")
def root():
    lang_id = get_lang()
    return render_template('index.html', translation = translations[lang_id])

@app.route("/products")
def page_products():
    lang_id = get_lang()
    return render_template('products.html', translation = translations[lang_id])

@app.route("/product-details")
def page_products():
    lang_id = get_lang()
    return render_template('product-details.html', translation = translations[lang_id])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5500")