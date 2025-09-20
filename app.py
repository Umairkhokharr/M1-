from flask import Flask, request, jsonify, render_template
import json
import time
import random
from datetime import datetime

app = Flask(__name__)

# Mock merchant database
MERCHANT_DB = {
    "MCC_5411_12345": {
        "name": "Whole Foods Market",
        "category": "Grocery Store",
        "location": "123 Main St, New York, NY",
        "risk_level": "Low",
        "mcc_code": "5411"
    },
    "MCC_5812_67890": {
        "name": "McDonald's",
        "category": "Fast Food Restaurant",
        "location": "456 Oak Ave, Los Angeles, CA",
        "risk_level": "Medium",
        "mcc_code": "5812"
    },
    "MCC_5999_11111": {
        "name": "Suspicious Store",
        "category": "Unknown Business",
        "location": "999 Dark Alley, High Risk City",
        "risk_level": "High",
        "mcc_code": "5999"
    },
    "MCC_4121_22222": {
        "name": "Uber",
        "category": "Transportation Service",
        "location": "San Francisco, CA",
        "risk_level": "Low",
        "mcc_code": "4121"
    }
}

# Fraud detection rules
def detect_fraud(transaction_data):
    flags = []
    risk_score = 0
    
    # Velocity check (max 10 transactions per hour)
    if transaction_data.get('velocity', 0) > 10:
        flags.append("high_velocity")
        risk_score += 20
    
    # Amount check (flag if > $1000)
    if transaction_data.get('amount', 0) > 1000:
        flags.append("unusual_amount")
        risk_score += 15
    
    # Location mismatch check
    if transaction_data.get('ip_location') != transaction_data.get('billing_location'):
        flags.append("location_mismatch")
        risk_score += 25
    
    # Card validation check
    if not transaction_data.get('card_valid', True):
        flags.append("invalid_card")
        risk_score += 30
    
    # Time-based check (unusual hours)
    hour = datetime.now().hour
    if hour < 6 or hour > 22:
        flags.append("unusual_timing")
        risk_score += 10
    
    # Random fraud pattern (for demo)
    if random.random() < 0.1:  # 10% chance
        flags.append("suspicious_pattern")
        risk_score += 15
    
    return flags, min(risk_score, 100)

def get_decision(risk_score):
    if risk_score <= 25:
        return "APPROVE"
    elif risk_score <= 50:
        return "REVIEW"
    elif risk_score <= 75:
        return "DECLINE"
    else:
        return "BLOCK"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze-transaction', methods=['POST'])
def analyze_transaction():
    try:
        data = request.json
        merchant_id = data.get('merchant_id', '')
        
        # Get merchant info
        merchant_info = MERCHANT_DB.get(merchant_id, {
            "name": "Unknown Merchant",
            "category": "Unknown Category",
            "location": "Unknown Location",
            "risk_level": "Medium",
            "mcc_code": "0000"
        })
        
        # Detect fraud
        fraud_flags, risk_score = detect_fraud(data)
        
        # Get decision
        decision = get_decision(risk_score)
        
        # Calculate processing time
        processing_time = random.randint(50, 150)  # 50-150ms
        
        result = {
            "transaction_id": f"TXN_{int(time.time())}",
            "merchant_info": merchant_info,
            "fraud_flags": fraud_flags,
            "risk_score": risk_score,
            "decision": decision,
            "processing_time": f"{processing_time}ms",
            "timestamp": datetime.now().isoformat()
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/merchants')
def get_merchants():
    return jsonify(list(MERCHANT_DB.keys()))

if __name__ == '__main__':
    app.run(debug=True)
