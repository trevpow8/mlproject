# ⚾ MLB First Inning Run Predictor

An end-to-end machine learning project that predicts the probability of runs being scored in the first inning of MLB games using historical game data and key player statistics.

## 🎯 Current Features

### **Working ML Pipeline**
- **Data Ingestion**: Automated reading and processing of MLB game data
- **Data Transformation**: Feature engineering with preprocessing pipelines for numerical and categorical data
- **Model Training**: Logistic regression classifier optimized for first inning run prediction
- **Model Persistence**: Trained models saved as pickle files for consistent predictions

### **Web Application**
- **Beautiful Flask Interface**: Modern, responsive web UI for making predictions
- **Real-time Predictions**: Input game parameters and get instant probability predictions
- **Probability Display**: Shows both binary prediction and percentage probabilities for "no run" vs "run"

### **Key Input Features**
- Home team leadoff hitter batting average
- Away team leadoff hitter batting average  
- Home starting pitcher ERA
- Away starting pitcher ERA
- Venue/Stadium selection (accounts for park factors)

### **Model Performance**
- **Algorithm**: Logistic Regression
- **Current Accuracy**: ~52.6% on test data
- **Output**: Probability of no runs in first inning (primary focus)

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

## 🔮 Future Enhancements & Roadmap

### **Immediate Improvements**
- [ ] **Real-time Data Integration**: Connect to live MLB APIs for upcoming game predictions
- [ ] **Enhanced Model Performance**: 
  - Experiment with ensemble methods (Random Forest, XGBoost, CatBoost)
  - Feature engineering: weather data, recent team performance, pitcher matchups
  - Hyperparameter tuning and cross-validation
- [ ] **Additional Features**:
  - Recent team scoring trends (last 10 games)
  - Pitcher vs opposing team historical performance
  - Weather conditions (temperature, wind, humidity)
  - Day/night game factors
  - Team rest days

### **Advanced Features Planned**
- [ ] **Live Game Integration**: 
  - Fetch upcoming games from MLB API
  - Real-time roster and lineup updates
  - Injury reports and player status
- [ ] **Model Improvements**:
  - Deep learning models for complex pattern recognition
  - Time series analysis for team momentum
  - Player-specific performance trends
  - Ballpark factor analysis
- [ ] **Enhanced UI/UX**:
  - Today's games dashboard
  - Historical prediction accuracy tracking
  - Betting odds comparison
  - Mobile-responsive design improvements

### **Long-term Vision**
- [ ] **Multi-inning Predictions**: Expand beyond first inning to predict total runs
- [ ] **Player Impact Analysis**: Individual player contribution to first inning scoring
- [ ] **Historical Backtesting**: Validate model performance across multiple seasons
- [ ] **API Development**: REST API for external integrations
- [ ] **Database Integration**: PostgreSQL for scalable data storage
- [ ] **Deployment**: Docker containerization and cloud deployment (AWS/GCP)

## 📈 Technical Improvements Needed

### **Data Quality**
- Expand dataset with more historical seasons
- Add real-time data validation and cleaning
- Implement data drift detection

### **Model Performance**
- Current accuracy of 52.6% needs improvement
- Implement model versioning and A/B testing
- Add confidence intervals for predictions

### **Infrastructure**
- Add automated testing suite
- Implement CI/CD pipeline
- Add monitoring and alerting for model performance

## 🤝 Contributing

This project is currently in active development. Future contributions will focus on:
- Model performance improvements
- Real-time data integration
- Enhanced feature engineering
- UI/UX improvements

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