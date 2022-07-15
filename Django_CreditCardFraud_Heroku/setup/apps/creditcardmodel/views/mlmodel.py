from django.shortcuts import render
from apps.creditcardmodel.forms.forms import MLModelForms
from apps.creditcardmodel.apps import CatBst_ModelConfig

import numpy as np
import pandas as pd
from cmath import nan

def index(request):
    if request.method == "POST":
        model_form = MLModelForms(request.POST)

        if model_form.is_valid( ):
            CatBst_model = CatBst_ModelConfig.CatBst_model
            opt_thresh   = CatBst_ModelConfig.opt_thresh

            d_home = np.log(float(model_form.cleaned_data['distance_home']))
            d_last = np.log(float(model_form.cleaned_data['distance_last']))
            value  = np.log(float(model_form.cleaned_data['value']))

            same = 1 if (model_form.cleaned_data['same_seller'] == 'SIM') else 0
            phys = 1 if (model_form.cleaned_data['physical'] == 'SIM') else 0
            pswd = 1 if (model_form.cleaned_data['password'] == 'SIM') else 0
            onln = 1 if (model_form.cleaned_data['online'] == 'SIM') else 0

            X_v = pd.DataFrame( {'Distance_home' : d_home, 'Distance_last_transaction' : d_last, 'Transaction_value' : value, 'Same_seller' : same, 'Physical_card' : phys, 'Password' : pswd, 'Online' : onln}, index = [0] )
            (y_pred, y_prob) = pred_threshold(CatBst_model, X_v, opt_thresh)

            resultado = {'fraude' : y_pred[0], 'prob' : round(y_prob[0]*100, 2)}
        else:
            resultado = {'fraude' : -1}
            
        contexto = {'model_form' : model_form, 'resultado' : resultado}
        return render(request, 'creditcardmodel/index.html', contexto)
    else:
        model_form = MLModelForms( )
        resultado = {'fraude' : -1}
        contexto = {'model_form' : model_form, 'resultado' : resultado}
        return render(request, 'creditcardmodel/index.html', contexto)

def pred_threshold(model, X, t):
  y_prob = model.predict_proba(X)[::, 1]
  y_pred = []
  for i in range(len(y_prob)):
    y_pred.append(0 if (y_prob[i] < t) else 1)

  return (y_pred, y_prob)