# ✅ app.py — Flask Backend with Real CO₂ Factors
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    FACTORS = {
        'Car': 0.192,
        'Bike': 0.07,
        'Bus': 0.105,
        'Train': 0.041,
        'Flights': 0.15,
        'Electricity': 0.82,
        'Lpg': 2.983,
        'Cigarettes': 0.014,
        'Plastic': 0.0828
    }

    emissions = {}
    total = 0.0

    for key, factor in FACTORS.items():
        raw = float(data.get(key, 0))
        if key == "Cigarettes":
            raw *= 30
        emissions[key] = round(raw * factor, 2)
        total += raw * factor

    emissions['Total'] = round(total, 2)
    return jsonify({"total": round(total, 2), "emissions": emissions})

if __name__ == '__main__':
    app.run(debug=True)

