teksts = input("Ievadi tekstu: ")
def replace0 (text):
  if text.count("o")>0 or text.count("O")>0:
    text = text.replace("o","%")
    text = text.replace("o","%")
    print(text)
  else:
    text = "Nav burtu O vai o."
    print(text)
  return text
replace0 (teksts)