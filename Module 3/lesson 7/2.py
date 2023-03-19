import re

text = "Е825ХО21 Т164МВ777 АА111121 Ц123АА21 А777АА777"

result = re.findall(r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}', text)
print(result)
