text = ['в', '5', 'часов', '17', 'минут',
      'температура', 'воздуха', 'была', '+5', 'градусов']
for i in range(len(text)):
    if text[i].isdigit() or "+" in text[i]:
        if len(text[i]) == 1:
           text.append('"' + "0" + text[i] + '"')
        elif len(text[i]) == 2 and "+" in text[i]:
            text.append('"' + str(text[i])[:1] + "0" + str(text[i])[1:] + '"')
        else:
            text.append('"' + text[i] + '"')
    else:
        text.append(text[i])
text = text[len(text) // 2:]
print(*text)