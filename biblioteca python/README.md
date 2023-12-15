# Documentação python para NGS

## Strings

* Método split
  
  ```python
  string = 'Hello, World!'
  string_splited = string.split(',')
  print(string_splited)

  # ['Hello', ' World!']
  ```

* Método len

  ```python
  string = 'Hello'
  print(len(string))
  
  # 5
  ```

* Método strip

  ```python
  string = '   foo    '
  print(string.strip())  # -> 'foo'
  print(string.lstrip()) # -> 'foo    '
  print(string.rstrip()) # -> '   foo'
  ```

* Método ljust e rjust

  ```python
  string = 'foo'
  print(string.rjust(10)) # -> '       foo'
  print(string.ljust(10)) # -> 'foo       '
  ```

* For em string

  ```python
  string = 'aleatory'

  for word in string:
    print(word)
  
  # a
  # l
  # e
  # a
  # t
  # o
  # r
  # y
  ```

* Método .lower() e .upper()

  ```python
  'FOO'.lower() # -> 'foo'
  'baa'.upper() # -> 'BAA'
  ```


## Array

*

  ```python
  
  ```
