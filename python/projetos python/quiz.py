print("Seja muito bem vindo ao quiz do Felipe!")
answer_user = input("Quer começar? (S/N)")
print(answer_user)

if answer_user != "S":
    quit()


print("Começando...")
print("Quem desenvolveu o jogo Grand Theft Auto (GTA)? \n (A) Rockstar Games (B) Ubisoft \n (C) Activision \n (D) EA \n")
answer_1 = input("Resposta: ")

if answer_1 == "A":
    print("Correto!")

else:
    print("Incorreto!")

print("Qual o nome do protagonista do jogo GTA San Andreas? \n (A) Carlos John \n (B) Carl Jonhson \n (C) Carl Jaqueline \n (D) Carlos Jonhson \n")
answer_2 = input("Resposta: ")


if answer_2 == "B":
    print("Correto!")

else:
    print("Incorreto!")

    print(f"Quiz acabou ... pontuação : ")
