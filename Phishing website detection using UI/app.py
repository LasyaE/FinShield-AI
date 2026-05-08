from flask import Flask,render_template,request

import FeatureExtraction
import pickle
import sklearn.ensemble
import sklearn.tree
import sys
sys.modules['sklearn.ensemble.forest'] = sklearn.ensemble
sys.modules['sklearn.ensemble.forest'] = sklearn.ensemble
sys.modules['sklearn.tree.tree'] = sklearn.tree


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        data = FeatureExtraction.getAttributess(url)
        print(data)
        url_lower = url.lower()
        suspicious_words = [
            "login",
            "verify",
            "security",
            "banking",
            "update",
            "free",
            "bonus",
            "gift",
            "paypal",
            "wallet"
]

        if "127.0.0.1" in url_lower or "localhost" in url_lower:
            predicted_value = 0
        elif "https" not in url_lower:
            predicted_value = 1
        elif any(word in url_lower for word in suspicious_words):
            predicted_value = 1
        elif len(url) > 75:
            predicted_value = 1
        else:
            predicted_value = 0
        #print(predicted_value)
        if predicted_value == 0:    
            value = "Legitimate"
            return render_template("home.html",error=value)
        else:
            value = "Phishing"
            return render_template("home.html",error=value)
if __name__ == "__main__":
    app.run()