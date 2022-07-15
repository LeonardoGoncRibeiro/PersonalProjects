from django.apps import AppConfig
import pickle

class CreditcardmodelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'creditcardmodel'

class CatBst_ModelConfig(AppConfig):
    serialized_model = open('apps/creditcardmodel/CatBstModel/FraudDetect_CreditCard_OptCatBoost.sav', 'rb')
    CatBst_model = pickle.load(serialized_model)
    serialized_model.close( )
    opt_thresh = 0.309658