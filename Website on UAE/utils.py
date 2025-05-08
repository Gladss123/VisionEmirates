import xgboost as xgb
from xgboost import XGBClassifier
from xgboost import XGBRegressor
def load_model(path):
    model = xgb.XGBClassifier()
    model.load_model(path)
    return model
