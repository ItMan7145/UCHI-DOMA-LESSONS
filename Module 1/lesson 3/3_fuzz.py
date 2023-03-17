from thefuzz import fuzz

# help(fuzz)

# print(fuzz.ratio("this is a test", "this is a test!"))

print(fuzz.ratio('Плохой код на самом деле не плохой', 'Его просто не так поняли'))
print(fuzz.ratio('Работает? Не трогай', 'Работает? Не трогай'))
