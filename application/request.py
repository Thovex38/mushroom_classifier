import requests

url = 'http://localhost:5000/results'
input1 = {'cap_shape': 'b', 'cap_surface': 'f', 'cap_color': 'n', 'bruises': 't', 'odor': 'a', 'gill_attachment': 'a',
          'gill_spacing': 'c', 'gill_size': 'b', 'gill_color': 'k', 'stalk_shape': 'e', 'stalk_root': 'b',
          'stalk_surface_above_ring': 'f', 'stalk_surface_below_ring': 'f', 'stalk_color_above_ring': 'n',
          'stalk_color_below_ring': 'n', 'veil_type': 'p', 'veil_color': 'n', 'ring_number': 'n', 'ring_type': 'e',
          'spore_print_color': 'k', 'population': 'a', 'habitat': 'g'}
input2 = {'cap_shape': 'c', 'cap_surface': 'f', 'cap_color': 'n', 'bruises': 't', 'odor': 'a', 'gill_attachment': 'a',
          'gill_spacing': 'c', 'gill_size': 'b', 'gill_color': 'k', 'stalk_shape': 'e', 'stalk_root': 'b',
          'stalk_surface_above_ring': 'f', 'stalk_surface_below_ring': 'f', 'stalk_color_above_ring': 'n',
          'stalk_color_below_ring': 'n', 'veil_type': 'p', 'veil_color': 'n', 'ring_number': 'n', 'ring_type': 'e',
          'spore_print_color': 'k', 'population': 'a', 'habitat': 'g'}
input3 = [input1, input2]
r = requests.post(url, json=input3)
r1 = requests.post(url, json=[input1])
print(r.json())
print(r1.json())
