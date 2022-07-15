from django import forms
from creditcardmodel.forms.forms_valid import *
from creditcardmodel.models import MLModel

class MLModelForms(forms.ModelForm):
    class Meta:
        model = MLModel
        fields = '__all__'

        labels = {'distance_home' : 'Distância da compra até a casa do titular do cartão (km)',
                  'distance_last' : 'Distância da compra até o local da última compra (km)',
                  'value'         : 'Valor da compra (R$)',
                  'same_seller'   : 'A compra foi feita no mesmo local que a última compra?',
                  'physical'      : 'A compra foi feita utilizando o cartão de crédito físico?',
                  'password'      : 'A compra foi feita utilizando a senha do cartão?',
                  'online'        : 'A compra foi feita de forma on-line?'}