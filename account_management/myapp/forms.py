from django import forms

class CoordinateForm(forms.Form):
    lon1 = forms.FloatField(label='最初の座標の経度')
    lat1 = forms.FloatField(label='最初の座標の緯度')
    lon2 = forms.FloatField(label='2番目の座標の経度')
    lat2 = forms.FloatField(label='2番目の座標の緯度')