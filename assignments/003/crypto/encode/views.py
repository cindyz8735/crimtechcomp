from django.shortcuts import render

def encode(msg, key):
  x = ""
  key = key.upper()
  counter = 0
  for ch in msg:
    val = ord(key[counter]) - ord('A') + 1
    if ch.islower():
      x += chr(((ord(ch) - ord('a') + val) % 26) + ord('a'))
    elif ch.isupper():
      x += chr(((ord(ch) - ord('A') + val) % 26) + ord('A'))
    else:
      x += ch
    if counter == len(key) - 1:
      key = key[::-1]
      counter = 0
    else:
      counter += 1
  return x

def encode_view(request): #<-- this is a view
  if request.method == 'POST':
    context = {'calculation': None}

    x, y = request.POST['x'], request.POST['y']
    fun = request.POST['function']

    context['calculation'] = calculate(x, y, fun)

    return render(request, 'encode.html', context=context)

  else:
    return render(request, 'encode.html')
