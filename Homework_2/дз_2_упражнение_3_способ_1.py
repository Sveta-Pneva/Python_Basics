text  = ['в', '5', 'часов', '17', 'минут',
      'температура', 'воздуха', 'была', '+5', 'градусов']
text = " ".join(text)
text_change = ""
j = 0
for i in text:
    if i.isdigit():
        if text_change[j - 1] == "0":
            text_change += "9"
        text_change += "1"
    else:
        if i == "+" or i == "-" or\
                j > 0 and text_change[j - 1] == "1":
            text_change += "2"
        else:
            text_change += "0"
    j = len(text_change)
j = 0
last_i = ""
for i in text_change:
      if i == "9":
            text = text[:j] + '"' + text[j:]
      elif i == "2":
            text = text[:j] + '"' + text[j:]
            j += 1
      elif i != last_i and i == "1":
            text = text[:j] + '0' + text[j:]
            j += 1
      elif i == last_i and i == "1":
            text = text[:j - 2] + text[j - 1:]
            j -= 1
      last_i = i
      j += 1
print(text)
