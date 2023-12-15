# string = 'Hello, World!'
# string_splited = string.split(',')
# print(string_splited)

# print(len(string_splited))

# string = 'foo'
# string2 = 'adryan'
# print(f'"{string}".lstrip() = "{string.lstrip()}"')
# print(f'"{string}".rstrip() = "{string.rstrip()}"')
# print(f'"{string}".strip() = "{string.strip()}"')

# print(f'"{string.rjust(10)}"')
# print(f'"{string.ljust(10)}"')
# print(f'"{string.upper()}"')

# string = 'aleatório'

# for word in string:
#   print(word)
  
# string = []

# for word in range(len(string)):
#   print(string[word])

# print(list(string))


# while True:
#   print('FOO'.lower() , 'baa'.upper())
#   if input('digite (s) para sair: ').lower() == 's':
#     break

name = 'Adryan Maikel da Cunha Kuhne'

name = name.lower()

# print(name.capitalize()) # -> Adryan maikel da cunha kuhne

def adjust_name(full_name: str) -> str:
  '''Função para ajustar o nome de uma pessoa, pegando de exemplo o método
  .title()

  Args:
    full_name (str): Nome completo de alguém ou algum lugar ex: 'fOO baa da fooBaa'

  Returns:
    str: Nome formatado ex: "Foo Baa da Foobaa"
  '''
  return ' '.join([
    name if len(name) <= 2 else name.capitalize()
    for name in full_name.lower().split(' ')
  ])

# name = adjust_name('adRYan maikel da cunha kuhne')
# print(name) # -> Adryan Maikel da Cunha Kuhne

name = adjust_name()
print(name)
# print(name.title()) # -> Adryan Maikel Da Cunha Kuhne

