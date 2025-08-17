from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application

## Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['GET','POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data=CustomData(
                home_leadoff_avg=float(request.form.get('home_leadoff_avg')),
                away_leadoff_avg=float(request.form.get('away_leadoff_avg')),
                home_starting_pitcher_era=float(request.form.get('home_starting_pitcher_era')),
                away_starting_pitcher_era=float(request.form.get('away_starting_pitcher_era')),
                venue=request.form.get('venue')
            )
            pred_df=data.get_data_as_data_frame()
            print("Input DataFrame:")
            print(pred_df)
            
            predict_pipeline=PredictPipeline()
            
            # Get both prediction and probabilities
            prediction=predict_pipeline.predict(pred_df)
            print("Prediction:", prediction)
            
            probabilities=predict_pipeline.predict_proba(pred_df)
            print("Probabilities:", probabilities)
            
            # Extract probability of no run (class 0) and run (class 1)
            prob_no_run = probabilities[0][0]  # Probability of False (no run)
            prob_run = probabilities[0][1]     # Probability of True (run)
            
            results = {
                'prediction': int(prediction[0]),
                'prob_no_run': prob_no_run,
                'prob_run': prob_run
            }
            
            return render_template('home.html', results=results)
        except Exception as e:
            print(f"Error in prediction: {e}")
            import traceback
            traceback.print_exc()
            return render_template('home.html', error=str(e))
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)