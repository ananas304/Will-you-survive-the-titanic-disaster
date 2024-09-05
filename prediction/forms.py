# prediction/forms.py
from django import forms

class PredictionForm(forms.Form):
    SibSp = forms.IntegerField(label='Number of Siblings/Spouses Aboard')
    Parch = forms.IntegerField(label='Number of Parents/Children Aboard')
    Fare = forms.FloatField(label='Fare')
    Title = forms.ChoiceField(
        choices=[('Miss', 'Miss'), ('Mr', 'Mr'), ('Mrs', 'Mrs'), ('Rare', 'Rare')],
        label='Title'
    )
    Embarked = forms.ChoiceField(
        choices=[('Q', 'Queenstown'), ('S', 'Southampton'),('C','Cherbourg')],
        label='Embarked'
    )
    Sex = forms.ChoiceField(
        choices=[('male', 'Male'), ('female', 'Female')],
        label='Sex'
    )
    Pclass = forms.ChoiceField(
        choices=[('1', '1st Class'), ('2', '2nd Class'), ('3', '3rd Class')],
        label='Pclass'
    )
