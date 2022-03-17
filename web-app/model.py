import tensorflow as tf
from tensorflow import keras
import numpy as np
import requests
import json
import os

def get_nutrition(recipe_name):
    api_url = 'https://api.calorieninjas.com/v1/nutrition?query='
    try: 
        query = recipe_name.replace('_', ' ')
    except AttributeError:
        return None

    response = requests.get(api_url + query, headers={'X-Api-Key': 'Nc/Q87KbQA0LD0QbT7fUyQ==cPxr3NJhdeA7FpaS'})
    if response.status_code == requests.codes.ok:
        text = response.text
        return json.loads(text)['items'][0]
    else:
        print("Warning:", response.status_code, response.text)
        return None


def get_prediction(img_url, warning=None):
    if img_url:
        class_names = ['apple_pie', 'baby_back_ribs', 'baklava', 'beef_carpaccio', 'beef_tartare', 'beet_salad', 'beignets', 'bibimbap', 'bread_pudding', 'breakfast_burrito', 'bruschetta', 'caesar_salad', 'cannoli', 'caprese_salad', 'carrot_cake', 'ceviche', 'cheese_plate', 'cheesecake', 'chicken_curry', 'chicken_quesadilla', 'chicken_wings', 'chocolate_cake', 'chocolate_mousse', 'churros', 'clam_chowder', 'club_sandwich', 'crab_cakes', 'creme_brulee', 'croque_madame', 'cup_cakes', 'deviled_eggs', 'donuts', 'dumplings', 'edamame', 'eggs_benedict', 'escargots', 'falafel', 'filet_mignon', 'fish_and_chips', 'foie_gras', 'french_fries', 'french_onion_soup', 'french_toast', 'fried_calamari', 'fried_rice', 'frozen_yogurt', 'garlic_bread', 'gnocchi', 'greek_salad', 'grilled_cheese_sandwich', 'grilled_salmon', 'guacamole', 'gyoza', 'hamburger', 'hot_and_sour_soup', 'hot_dog', 'huevos_rancheros', 'hummus', 'ice_cream', 'lasagna', 'lobster_bisque', 'lobster_roll_sandwich', 'macaroni_and_cheese', 'macarons', 'miso_soup', 'mussels', 'nachos', 'omelette', 'onion_rings', 'oysters', 'pad_thai', 'paella', 'pancakes', 'panna_cotta', 'peking_duck', 'pho', 'pizza', 'pork_chop', 'poutine', 'prime_rib', 'pulled_pork_sandwich', 'ramen', 'ravioli', 'red_velvet_cake', 'risotto', 'samosa', 'sashimi', 'scallops', 'seaweed_salad', 'shrimp_and_grits', 'spaghetti_bolognese', 'spaghetti_carbonara', 'spring_rolls', 'steak', 'strawberry_shortcake', 'sushi', 'tacos', 'takoyaki', 'tiramisu', 'tuna_tartare', 'waffles']

        img_height, img_width = 224, 224
        image_url = img_url
        try:
            image_path = tf.keras.utils.get_file('', origin=image_url)
        except:
            return None, None, 'Bad URL !'

        img = tf.keras.utils.load_img(
            image_path, target_size=(img_height, img_width)
        )

        img_array = tf.keras.utils.img_to_array(img)
        img_array = img_array / 255.
        img_array = tf.expand_dims(img_array, 0) # Create a batch
        model = keras.models.load_model('trained_model.h5')
        predictions = model.predict(img_array)
        score = predictions[0]

        print(
            "This image most likely belongs to {} with a {:.5f} percent confidence."
            .format(class_names[np.argmax(score)], 100 * np.max(score))
        )
        
        os.remove(image_path)
        prediction = class_names[np.argmax(score)].replace('_', ' ')
        probability = round(100 * np.max(score), 3)
    else:
        prediction  = None
        probability = None
        
    return prediction, probability, warning