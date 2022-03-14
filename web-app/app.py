from flask import Flask, render_template, request
app = Flask(__name__)

import model

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prediction, probability, warning = model.get_prediction(request.form['image_url'])
        nutrition_score = model.get_nutrition(prediction)
        if nutrition_score:
            recipe_calories = nutrition_score['calories']
        else:
            recipe_calories = None

        return render_template('index.html', 
                                prediction=prediction,
                                probability=probability,
                                warning=warning,
                                calories=recipe_calories,
                                img_url=request.form['image_url'])

    return render_template('index.html')
    
def create_app():
   return app

if __name__ == "__main__":
    app.run(host='localhost', debug=True)
    