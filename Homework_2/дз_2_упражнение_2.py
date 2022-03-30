text = ['в', '5', 'часов', '17', 'минут',
      'температура', 'воздуха', 'была', '+5', 'градусов']
new_text = []
for i in range(len(text)):
    if text[i].isdigit() or "+" in text[i]:
        if len(text[i]) == 1:
            new_text.append('"' + "0" + text[i] + '"')
        elif len(text[i]) == 2 and "+" in text[i]:
            new_text.append('"' + str(text[i])[:1] + "0" + str(text[i])[1:] + '"')
        else:
            new_text.append('"' + text[i] + '"')
    else:
        new_text.append(text[i])
print(*new_text)