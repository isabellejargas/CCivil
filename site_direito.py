# artigos do códig civil do 1° ao 10°
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

# Artigo 1
art_1 = "Quem são as pessoas capazes de direitos e deveres na ordem civil? ".strip().lower()
#lower para converter a resposta do usuário em letras minúsculas

#Lista de respostas que serão aceitas para o Artigo 1
respostas_aceitas_1 = [
"todas as pessoas",
"sociedade civil",
"pessoas jurídicas",
"o ser humano",
"a pessoa física",
"sociedade",
"a pessoa natural"]

# Loop para que o usuário tente até acertar a resposta + any para que o código procure palavras-chave na resposta do usuário
# Resposta do usuário é convertida para minúsculas (lower()) e espaços em branco são removidos (strip()) para evitar erros de digitação
# Output de feedback para o usuário, caso a resposta esteja certa ou errada
# Se errada, o usuário é incentivado a revisar o conteúdo e tentar novamente
# A ideia se mantém em todos os artigos, com variações nas perguntas e respostas aceitas.

while True:
    resposta_1 = input("Quem são as pessoas capazes de direitos e deveres na ordem civil? ").strip().lower()

    if any(frase in resposta_1 for frase in respostas_aceitas_1):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 2
art_2 = "Quando começa a personalidade civil da pessoa natural?"

#Lista de respostas que serão aceitas para o Artigo 2
respostas_aceitas_2 = [
"no nascimento com vida",
"o nascimento com vida",
"quando nasce com vida",
"a partir do nascimento com vida",
"nascimento"]

while True:
    resposta_2 = input("Quando começa a personalidade civil da pessoa natural? ").strip().lower()

    if any(frase in resposta_2 for frase in respostas_aceitas_2):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 3
art_3 = "Quem são os absolutos incapazes de exercer pessoalmente os atos da vida civil?"

#Lista de respostas que serão aceitas para o Artigo 3
respostas_aceitas_3 = [
"menores de 16 anos",
"menores de 16 anos completos",
"menores de 16 anos de idade",
"menores de 16 anos de idade completos",
"menores de dezesseis anos",
"menor de 16 anos",
"absolutamente incapaz",
"absolutamente incapazes"]

while True:
    resposta_3 = input("Quem são os absolutos incapazes de exercer pessoalmente os atos da vida civil? ").strip().lower()

    if any(frase in resposta_3 for frase in respostas_aceitas_3):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 4
art_4 = "Quem são os relativamente incapazes de exercer pessoalmente os atos da vida civil?"

# Lista de respostas que serão aceitas para o Artigo 4
respostas_aceitas_4 = [
'16 a 18 anos',
'ébrios habituais',
'viciados em tóxicos',
'pródigos',
'relativamente incapaz',
'relativamente incapazes'
]

while True:
    resposta_4 = input("Quem são os relativamente incapazes de exercer pessoalmente os atos da vida civil? ").strip().lower()
    if any(frase in resposta_4 for frase in respostas_aceitas_4):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 5
art_5 = "Quando a menor idade cessa e no que isso acarreta?"
# Lista de respostas que serão aceitas para o Artigo 5
respostas_aceitas_5 = [
'18 anos',
'maioridade',
'plenamente capaz',
'totalmente capaz'
]

while True:
    resposta_5 = input("Quando a menor idade cessa e no que isso acarreta? ").strip().lower()
    if any(frase in resposta_5 for frase in respostas_aceitas_5):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 6
art_6 = "Quando a existência da pessoa natural termina?"
respostas_aceitas_6 = [
'com a morte da pessoa natural',
'com a morte',
'com a morte do indivíduo',
'com a morte do ser humano',
'com a morte do ser humano natural',
'morte'
]
while True:
    resposta_6 = input("Quando a existência da pessoa natural termina? ").strip().lower()
    if any(frase in resposta_6 for frase in respostas_aceitas_6):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 7
art_7 = "Quando pode ser declarada a morte presumida da pessoa natural?"
respostas_aceitas_7 = [
"morte presumida",
"extremamente provável",
"desaparecimento",
"perigo de vida",
"naufrágio",
"calamidade pública"
]

while True:
    resposta_7 = input("Quando pode ser declarada a morte presumida da pessoa natural? ").strip().lower()
    if any(frase in resposta_7 for frase in respostas_aceitas_7):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 8
art_8 = "Se dois indivíduos falecerem na mesma ocasião, sem a possibilidade de determinar quem morreu primeiro, o que acontece?"
respostas_aceitas_8 = [
"simultaneamente mortos",
"mesmo tempo",
"ambos mortos",
"comorientes"
]

while True:
    resposta_8 = input("Se dois indivíduos falecerem na mesma ocasião, sem a possibilidade de determinar quem morreu primeiro, o que acontece? ").strip().lower()
    if any(frase in resposta_8 for frase in respostas_aceitas_8):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 9
art_9 = "O que será registrado no registro público?"
respostas_aceitas_9 = [
"nascimento",
"casamento",
"óbito",
"emancipação",
"interdição",
"ausência",
"morte presumida"
]
while True:
    resposta_9 = input("O que será registrado no registro público? ").strip().lower()
    if any(frase in resposta_9 for frase in respostas_aceitas_9):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")

# Artigo 10
art_10 = "Quando acontece a averbação em registro público?"
respostas_aceitas_10 = [
"anulação do casamento",
"divórcio",
"separação judicial",
"restabelecimento da sociedade conjugal",
"reconhecimento da filiação",
"filiação"
]
while True:
    resposta_10 = input("Quando acontece a averbação em registro público? ").strip().lower()
    if any(frase in resposta_10 for frase in respostas_aceitas_10):
        print("Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!")
        break
    else:
        print("Ops, o STF perdoa essa, mas vamos revisar?")
