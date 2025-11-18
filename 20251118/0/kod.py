import locale

print(locale.getlocale())
print('Привет'.encode())
print('Привет'.encode('CP1251'))

print('Привет'.encode('CP1251').decode('KOI8-R'))

# преобразовать слово "вопрос" в "БНОПНЯ" с помощью encdode() и decode(); 
# найти слова, из которых можно получить тем же способом "бМХЛЮМХЕ" и "ОХРЮМХЕ" 
# (используются кодировки cp1251 и koi8-r)

print('вопрос'.encode('CP1251').decode('KOI8-R'))
print('бМХЛЮМХЕ'.encode('KOI8-R').decode('CP1251')) #внимание
print('ОХРЮМХЕ'.encode('KOI8-R').decode('CP1251')) #питание