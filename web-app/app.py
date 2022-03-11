from flask import Flask, render_template, request
app = Flask(__name__)

import model

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prediction, probability = model.get_prediction(request.form['image_url'])
        
        return render_template('index.html', 
                                prediction=prediction,
                                probability=probability)

    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
    