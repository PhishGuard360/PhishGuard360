from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        url_content = data.get('urlContent')

        if url_content:
            # Define the endpoint and headers with Hugging Face credentials
            hf_api_url = "https://cluz3abygwtyi7gj.us-east-1.aws.endpoints.huggingface.cloud"
            headers = {"Authorization": "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"}
            
            response = requests.post(hf_api_url, headers=headers, json={"inputs": url_content})

            
            if response.status_code == 200:
                result_data = response.json()
               
                if isinstance(result_data, list) and len(result_data) > 0:
                    result = result_data[0].get('label', 'No result')
                    accuracy = result_data[0].get('score', 'No accuracy')

            else:
                result = "Error: Unable to get result"
                accuracy = "N/A"

            return jsonify({"URL Prediction": result, "Accuracy": accuracy})

    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/products')
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)







# from flask import Flask, request, jsonify, render_template

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         data = request.get_json()
#         url_content = data.get('urlContent')

#         if url_content:
#             # Simulate API response for testing
#             result = "Sample Prediction: Safe URL"
#             accuracy = "Sample Accuracy: 95.67%"

#             return jsonify({"URL Prediction": result, "Accuracy": accuracy})
        
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

