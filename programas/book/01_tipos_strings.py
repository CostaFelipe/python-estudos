print("this also a string")
print('this is a string')
print('this is perfect')

message = 'I told my friends "Python is my favorite language"'
print(message)

name = "Linda"
hello = 'Hello my name is ' + name
print(hello)

#letras maiusculas e minusculas
name = "ada lovelace"
print(name.title())

nome = "levi de lima"
print(nome.title())

name = "ADA LOVELACE"
print(name.lower())

language = "ELIXIR IS THE BEST"
print(language.lower())

name = "Ada Lovelace"
print(name.upper())

language = "Phoenix framework"
print(language.upper())

#Combinando ou concatenando strings
first_name = "Ada"
last_name = "Lovelace"
print(first_name + " " + last_name)

language = "Elixir"
framework = "Phoenix"
print(language +  " your framework is " + framework)

#Acrescentando espacos em branco em strings com tabulacoes ou quebras de linha
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")

#Removendo espacos em branco
#lado direito de um string
favorite_language = 'python '
print(favorite_language.rstrip())

#para sempre
favorite_language = favorite_language.rstrip()
print(favorite_language)

#lado esquerdo
favorite_language = " Ada"
print(favorite_language.lstrip())

#Ambos os lados
favorite_language = " Erlang "
print(favorite_language.strip())

#Apostrophe
message = "One of Python's strengths is its diverse community."
print(message)

#exercicios strings
#1)
personal_message = "Hello Eric, good morning?"
print(personal_message)

#2)
name = "esther oliveira"
print(name.upper())

name = "ESTHER"
print(name.lower())
print(name.title())

#3)
message = 'Albert Einstein certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."'
print(message)

#4)
famous_person = "Albert Einstein"
message = famous_person + ' certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo."'
print(message)

#5)
message = famous_person + ' certa vez disse: "Uma pessoa que nunca cometeu um erro jamais tentou nada novo." '
print(message.strip())
