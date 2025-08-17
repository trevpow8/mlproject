# ⚾ MLB First Inning Run Predictor

An end-to-end machine learning project that predicts the probability of runs being scored in the first inning of MLB games using historical game data and key player statistics.

## 🎯 Current Features

- **Complete ML Pipeline**: Data ingestion, transformation, and model training using scikit-learn
- **Logistic Regression Model**: Trained on historical MLB game data with ~52.6% accuracy
- **Flask Web Interface**: Clean, responsive UI for making predictions
- **Probability Predictions**: Shows percentage probability of runs vs no runs in first inning

### **Input Features**
- Home/Away team leadoff hitter batting averages
- Home/Away starting pitcher ERAs
- Stadium/Venue selection

### **Tech Stack**
- Python, Flask, scikit-learn, pandas, numpy
- HTML/CSS for frontend
- Pickle files for model persistence

## 🚀 How to Run Locally

### **Prerequisites**
- Python 3.11+ with conda environment
- All dependencies listed in `requirements.txt`

### **Setup & Execution**
1. **Activate Environment**:
   ```bash
   conda activate /Users/trevorpowell/mlproject/venv
   ```

2. **Navigate to Project**:
   ```bash
   cd /Users/trevorpowell/mlproject
   ```

3. **Train Model** (if needed):
   ```bash
   python train.py
   ```

4. **Run Web Application**:
   ```bash
   python app.py
   ```

5. **Access Interface**: Open browser to `http://localhost:4000`

## 📊 Project Structure

```
mlproject/
├── app.py                          # Flask web application
├── train.py                        # Model training script
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
├── artifacts/                      # Generated model files
│   ├── model.pkl                   # Trained logistic regression model
│   ├── preprocessor.pkl            # Data preprocessing pipeline
│   ├── train.csv                   # Training dataset
│   ├── test.csv                    # Test dataset
│   └── data.csv                    # Full dataset
├── src/                            # Source code modules
│   ├── components/                 # ML pipeline components
│   │   ├── data_ingestion.py       # Data loading and splitting
│   │   ├── data_transformation.py  # Feature engineering
│   │   └── model_trainer.py        # Model training logic
│   ├── pipeline/                   # Prediction pipelines
│   │   ├── predict_pipeline.py     # Inference pipeline
│   │   └── train_pipeline.py       # Training pipeline
│   ├── utils.py                    # Utility functions
│   ├── logger.py                   # Logging configuration
│   └── exception.py                # Custom exception handling
├── templates/                      # HTML templates
│   ├── index.html                  # Landing page
│   └── home.html                   # Prediction interface
└── notebook/                       # Jupyter notebooks & raw data
    ├── data/
    │   └── mlb_game_data.csv        # Raw MLB data
    └── EDA MLB First Inning.ipynb  # Exploratory data analysis
```

## 🔮 Future Plans

- **Model Improvements**: Experiment with better algorithms and additional features
- **Live Data Integration**: Connect to MLB APIs for upcoming game predictions  
- **Cloud Deployment**: Move from local hosting to cloud platform (AWS/GCP) for public access

## 📋 Dependencies

Key libraries used:
- **Flask**: Web framework for the prediction interface
- **scikit-learn**: Machine learning algorithms and preprocessing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **dill**: Model serialization

See `requirements.txt` for complete dependency list.

---

*This project demonstrates end-to-end ML pipeline development from data ingestion to web deployment, with a focus on practical baseball analytics and real-world prediction scenarios.*