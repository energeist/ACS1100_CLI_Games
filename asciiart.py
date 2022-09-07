import requests

r = requests.get('http://artii.herokuapp.com/make?text=Awesomesauce')
print(r.text)
print("It's busted :(")