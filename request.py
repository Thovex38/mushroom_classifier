import requests

url = 'http://localhost:5000/results'
input1 = {'cap-shape': 'b', 'cap-surface': 'f', 'cap-color': 'n', 'bruises': 't', 'odor': 'a', 'gill-attachment': 'a', 'gill-spacing': 'c', 'gill-size': 'b', 'gill-color': 'k', 'stalk-shape': 'e', 'stalk-root': 'b', 'stalk-surface-above-ring': 'f', 'stalk-surface-below-ring': 'f', 'stalk-color-above-ring': 'n', 'stalk-color-below-ring': 'n', 'veil-type': 'p', 'veil-color': 'n', 'ring-number': 'n', 'ring-type': 'e', 'spore-print-color': 'k', 'population': 'a', 'habitat': 'g'}
input2 = {'cap-shape': 'c', 'cap-surface': 'f', 'cap-color': 'n', 'bruises': 't', 'odor': 'a', 'gill-attachment': 'a', 'gill-spacing': 'c', 'gill-size': 'b', 'gill-color': 'k', 'stalk-shape': 'e', 'stalk-root': 'b', 'stalk-surface-above-ring': 'f', 'stalk-surface-below-ring': 'f', 'stalk-color-above-ring': 'n', 'stalk-color-below-ring': 'n', 'veil-type': 'p', 'veil-color': 'n', 'ring-number': 'n', 'ring-type': 'e', 'spore-print-color': 'k', 'population': 'a', 'habitat': 'g'}
input3 = [input1,input2]
r = requests.post(url,json=input3)
print(r.json())