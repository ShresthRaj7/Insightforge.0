import sys
import pandas as pd
from src.exception import CustomException
from src.utlis import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path="artifacts/model.pkl"
            preprocess_path="artifacts/preprocess.pkl"
            model=load_object(model_path)
            preprocess=load_object(preprocess_path)
            data_scaled=preprocess.transform(features)
            pred =model.predict(data_scaled)
            return pred
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,
        gender:str,
        race_enthnicity:str,
        parental_level_of_education,
        lunch:int,
        test_preparation_course:int,
        reading_score:int,
        writing_score:int):

        self.gender=gender
        self.race_enthnicity=race_enthnicity
        self.parental_level_of_education=parental_level_of_education
        self.lunch=lunch
        self.test_preparation_course=test_preparation_course
        self.reading_score=reading_score
        self.writing_score=writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict={
                "gender":[self.gender],
                "race_enthnicity":[self.race_enthnicity],
                "parental_level_of_education":[self.parental_level_of_education],
                "lunch":[self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "reading_score":[self.reading_score],
                "writing_score":[self.writing_score]
            }

            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
      
        