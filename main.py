ambiente = input("Qual o ambiente da história? ")
personagem = input("Quem é o personagem? ")
poder = input("poder do personagem?")
local_objeto = input("Onde estava a coisa que ele achou? ")

if "praia" in ambiente or "morro da conceição" in ambiente:
    historia = (f"{personagem} caminhava pela {ambiente} quando, de repente, avistou uma reliquia estranha... "
                f"{local_objeto}. Com o coração acelerado decidiu se aproximar para investigar.")
elif "cidade" in ambiente or "Cidade" in ambiente:
    historia = (f"Nas ruas movimentadas da {ambiente}, {personagem} se deparou com uma reliquia: {poder} no"
                f"{local_objeto}. Ganhando poderes misteriosos.")
else:
    historia = ("Aconeteceu nada hoje...")

print(historia)