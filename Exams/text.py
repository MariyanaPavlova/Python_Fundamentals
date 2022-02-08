import re
text = input()
pattern = r'(#|@)([A-Za-z)]{3,})\1(#|@)([A-Za-z)]{3,})\1'

matched_iter = re.finditer(pattern,text)
matched_all = re.findall(pattern, text)
search = re.search(pattern, text)
matched = re.match(pattern, text)
a=5
print(matched_iter)
print(matched_all)
print(search)
print(matched)

#Вход
#@mix#tix3dj#poOl##loOp#wl@@bong&song%4very$long@thong#Part##traP##@@leveL@@Level@##car#rac##tu@pack@@ckap@#rr#sAw##wAs#r#@w1r