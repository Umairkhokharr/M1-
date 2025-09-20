# MerchSentAI MVP Demo

A working demonstration of the MerchSentAI fraud detection and merchant intelligence platform.

## Features
- Merchant data enrichment
- Real-time fraud detection
- Risk scoring (0-100)
- Professional web interface
- Sample test data

## Live Demo
Deployed on Vercel: [Your Vercel URL]

## How to Run Locally
1. Install Python 3.7+
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python app.py`
4. Open: http://localhost:5000

## Test Scenarios
- Low Risk: Grocery store, normal amount
- Medium Risk: Location mismatch, high amount
- High Risk: Suspicious merchant, high velocity

## Deployment Instructions

### GitHub Setup
1. Create a new repository on GitHub
2. Upload all files to the repository
3. Make sure the folder structure is correct

### Vercel Deployment
1. Go to vercel.com
2. Sign up with GitHub
3. Click "New Project"
4. Import your repository
5. Click "Deploy"

## File Structure
```
merchsentai-mvp/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── vercel.json        # Vercel deployment config
├── README.md          # This file
└── templates/
    └── index.html     # Web interface
```

## What This MVP Demonstrates
- Converts cryptic merchant codes to business information
- Real-time fraud detection with multiple flags
- Risk scoring and decision making
- Professional user interface
- Fast processing (<150ms response time)

## Next Steps
- Add more merchant data sources
- Implement ML models for fraud detection
- Add more fraud detection flags
- Improve UI/UX
- Add analytics dashboard


