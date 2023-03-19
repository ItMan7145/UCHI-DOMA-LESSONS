import re

text = '8(918)654-89-12, телефон 7(987)456-45-45 или 8(456)1212123 8(456)123-45-45'

result = re.findall(r'8\(\d{3}\)\d{3}-\d{2}-\d{2}', text)
print(*result)
