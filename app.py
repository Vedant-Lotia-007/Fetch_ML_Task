from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the predictions into a DataFrame
predictions_df = pd.read_csv('monthly_predictions_2022.csv')


@app.route('/')
def index():
    # Pass the months to the frontend
    months = predictions_df['month'].tolist()
    return render_template('index.html', months=months)


@app.route('/predict-year', methods=['GET'])
def predict_year():
    predictions = predictions_df.to_dict(orient='records')
    return jsonify(predictions)


@app.route('/predict', methods=['POST'])
def predict():
    selected_month = request.form.get('month')
    prediction = predictions_df[predictions_df['month'] == selected_month]['predicted_receipts'].iloc[0]
    return jsonify({'month': selected_month, 'predicted_receipts': prediction})


if __name__ == '__main__':
    app.run(debug=True)
