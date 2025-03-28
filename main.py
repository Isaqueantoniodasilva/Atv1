cenario = input("Qual o cenário da história? ")
personagem = input("Quem é o personagem? ")
objeto = input("O que o personagem achou? ")
local_objeto = input("Onde estava a coisa que ele achou? ")

if "floresta" in cenario or "Floresta" in cenario:
    historia = (f"{personagem} caminhava pela {cenario} quando, de repente, avistou {objeto} "
                f"{local_objeto}. Com o coração acelerado decidiu se aproximar para investigar.")
elif "cidade" in cenario or "Cidade" in cenario:
    historia = (f"Nas ruas movimentadas da {cenario}, {personagem} se deparou com {objeto} "
                f"{local_objeto}. Seria aquilo um sinal do destino?")
else:
    historia = (f"Em um dia comum na {cenario}, {personagem} fez uma descoberta inesperada: "
                f"{objeto} {local_objeto}. O que isso significava?")

print(historia)
