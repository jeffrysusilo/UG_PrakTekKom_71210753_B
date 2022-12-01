def is_palindrome(w):
  rw = str(w)[::-1]
  print('jika dibalik: ',rw)
  if str(w) == rw:
    x='yes, ini palindrom boss'
    return x
  else :
    y='no, ini bukan palindrom boss'
    return y

inputan=(str(input('masukan kata: ')))
print(is_palindrome(inputan))

