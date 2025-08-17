import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self, features):
        try:
            model_path = 'artifacts/model.pkl'
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds
        except Exception as e:
            logging.error(f"Error occurred during prediction: {e}")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 home_leadoff_avg: float,
                 away_leadoff_avg: float,
                 home_starting_pitcher_era: float,
                 away_starting_pitcher_era: float,
                 venue: str):
        self.home_leadoff_avg = home_leadoff_avg
        self.away_leadoff_avg = away_leadoff_avg
        self.home_starting_pitcher_era = home_starting_pitcher_era
        self.away_starting_pitcher_era = away_starting_pitcher_era
        self.venue = venue

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "home_leadoff_avg": [self.home_leadoff_avg],
                "away_leadoff_avg": [self.away_leadoff_avg],
                "home_starting_pitcher_era": [self.home_starting_pitcher_era],
                "away_starting_pitcher_era": [self.away_starting_pitcher_era],
                "venue": [self.venue]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logging.info("Custom data frame created")
            return df
        except Exception as e:
            logging.error(f"Error in creating data frame: {e}")
            raise CustomException(e, sys)