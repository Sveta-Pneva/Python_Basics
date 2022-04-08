import requests
import xml.dom.minidom as xml

def currency_rates(n):
    n = n.upper()
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    res = requests.get(url)
    res = res.text
    dom = xml.parseString(res)
    elements = dom.getElementsByTagName("Valute")
    result = {}
    for i in elements:
        for j in i.childNodes:
            if j.tagName == 'Value':
                if j.firstChild.nodeType == 3:
                    value = float(j.firstChild.data.replace(',', '.'))
            elif j.tagName == 'CharCode':
                if j.firstChild.nodeType == 3:
                    char_code = j.firstChild.data
        if char_code == n:
            result[char_code] = value
            for key in result.keys():
                result = key + " " + str(result[key])
            return result
            break
    return None

if __name__ == '__main__':
    cur_code = input()
    print(currency_rates(cur_code))