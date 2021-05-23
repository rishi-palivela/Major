from flask import Flask, flash, request, redirect, render_template, jsonify
import model_final,db

app = Flask(__name__)


@app.route('/old')
def upload_form():
    return render_template('TV.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("data", data)
    
    brand = data["brand"]
    hd = data["hd"]
    rating = int(data["rating"])
    speaker = int(data["speaker"])
    size = int(data["size"])
    hdmi = int(data["hdmi"])
    usb = int(data["usb"])
    result = model_final.output(brand, rating, speaker, size, hd, hdmi, usb)
    tv1,tv2,tv3 = db.output(speaker, size, hd, hdmi, usb)
    return jsonify({"price": result}) #tv1,tv2,tv3

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        brand = (request.form.get('brand'))
        hd = (request.form.get('hd'))
        rating = int(request.form.get('rating'))
        usb = int(request.form.get('usb'))
        size = float(request.form.get('size'))
        hdmi = int(request.form.get('hdmi'))
        speaker = int(request.form.get('speaker'))

        result = model_final.output(brand, rating, speaker, size, hd, hdmi, usb)
        return render_template("result.html", prediction=result)
	
	


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
