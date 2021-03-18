#coding=utf-8
#Um dicionário em um dicionário

#Como a função input() trabalha
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#Escrevendo prompts claros
name = input("Please enter your name:")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print("\nHello, " + name)
