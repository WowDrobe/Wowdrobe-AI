from flask import Flask, request, jsonify
import google.generativeai as genai  
import requests  
import os
from dotenv import load_dotenv
from PIL import Image
import requests
from io import BytesIO
import pandas as pd
from flask_cors import CORS
from io import StringIO
import io
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)
CORS(app)

@app.route('/recommend', methods=['GET'])
def body_analyse():
   
    img_url = request.args.get('img_url')

    if img_url:
        
        response = requests.get(img_url)

        
        if response.status_code == 200:
          
            image = Image.open(BytesIO(response.content))

           
            model = genai.GenerativeModel('gemini-pro-vision')

            response = model.generate_content([" analyze uploaded images of people and generates personalized outfit suggestions based on their attire, style preferences, and contextual information such as weather and occasion. The model should output a list of clothing items or a styled image reflecting the suggested outfit. pls conisder the gender of the person and recommend accordingly", image], stream=True)
            response.resolve()

           
            return jsonify({"result": response.text})
        else:
            return jsonify({"error": "Failed to retrieve the image"}), 400
    else:
        return jsonify({"error": "img_url parameter is required"}), 400
    


if __name__ == '__main__':
    app.run(debug=True)

