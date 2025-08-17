#!/usr/bin/env python3
"""
Training script using the existing component structure
"""

import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

def train_model():
    """
    Complete training pipeline using existing components
    """
    try:
        print("🏟️ Starting MLB First Inning Run Prediction Model Training...")
        
        # Data Ingestion
        print("📊 Step 1: Data Ingestion...")
        logging.info("Starting data ingestion...")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        print(f"✅ Data ingestion completed!")
        print(f"   Train data: {train_data_path}")
        print(f"   Test data: {test_data_path}")
        
        # Data Transformation
        print("\n🔧 Step 2: Data Transformation...")
        logging.info("Starting data transformation...")
        data_transformation = DataTransformation()
        train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
        print(f"✅ Data transformation completed!")
        print(f"   Preprocessor saved: {preprocessor_path}")
        print(f"   Training data shape: {train_arr.shape}")
        print(f"   Test data shape: {test_arr.shape}")
        
        # Model Training
        print("\n🎯 Step 3: Model Training...")
        logging.info("Starting model training...")
        model_trainer = ModelTrainer()
        accuracy_score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        print(f"✅ Model training completed!")
        print(f"   Best Model: Logistic Regression")
        print(f"   Accuracy Score: {accuracy_score:.4f}")
        print(f"   Model saved: artifacts/model.pkl")
        
        print(f"\n🎉 Training pipeline completed successfully!")
        print(f"📈 Final Model Accuracy: {accuracy_score:.4f}")
        print(f"\n🚀 You can now run the Flask app with: python app.py")
        
        return accuracy_score
        
    except Exception as e:
        logging.error(f"Error in training pipeline: {e}")
        print(f"❌ Training failed: {e}")
        raise CustomException(e, sys)

if __name__ == "__main__":
    train_model()