from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# mesma lista de perguntas e respostas aceitas do código original
perguntas = [
    {
        "pergunta": "Quem são as pessoas capazes de direitos e deveres na ordem civil?",
        "aceitas": ["todas as pessoas", "sociedade civil", "pessoas jurídicas", "o ser humano", "a pessoa física", "sociedade", "a pessoa natural"]
    },
    {
        "pergunta": "Quando começa a personalidade civil da pessoa natural?",
        "aceitas": ["no nascimento com vida", "o nascimento com vida", "quando nasce com vida", "a partir do nascimento com vida", "nascimento"]
    },
    {
        "pergunta": "Quem são os absolutos incapazes de exercer pessoalmente os atos da vida civil?",
        "aceitas": ["menores de 16 anos", "menores de 16 anos completos", "menores de 16 anos de idade", "menores de 16 anos de idade completos", "menores de dezesseis anos", "menor de 16 anos", "absolutamente incapaz", "absolutamente incapazes"]
    },
    {
        "pergunta": "Quem são os relativamente incapazes de exercer pessoalmente os atos da vida civil?",
        "aceitas": ["16 a 18 anos", "ébrios habituais", "viciados em tóxicos", "pródigos", "relativamente incapaz", "relativamente incapazes"]
    },
    {
        "pergunta": "Quando a menor idade cessa e no que isso acarreta?",
        "aceitas": ["18 anos", "maioridade", "plenamente capaz", "totalmente capaz"]
    },
    {
        "pergunta": "Quando a existência da pessoa natural termina?",
        "aceitas": ["com a morte da pessoa natural", "com a morte", "com a morte do indivíduo", "com a morte do ser humano", "com a morte do ser humano natural", "morte"]
    },
    {
        "pergunta": "Quando pode ser declarada a morte presumida da pessoa natural?",
        "aceitas": ["morte presumida", "extremamente provável", "desaparecimento", "perigo de vida", "naufrágio", "calamidade pública"]
    },
    {
        "pergunta": "Se dois indivíduos falecerem na mesma ocasião, sem a possibilidade de determinar quem morreu primeiro, o que acontece?",
        "aceitas": ["simultaneamente mortos", "mesmo tempo", "ambos mortos", "comorientes"]
    },
    {
        "pergunta": "O que será registrado no registro público?",
        "aceitas": ["nascimento", "casamento", "óbito", "emancipação", "interdição", "ausência", "morte presumida"]
    },
    {
        "pergunta": "Quando acontece a averbação em registro público?",
        "aceitas": ["anulação do casamento", "divórcio", "separação judicial", "restabelecimento da sociedade conjugal", "reconhecimento da filiação", "filiação"]
    }
]


@app.route("/")
def home():
    return render_template("index.html", total=len(perguntas))


@app.route("/pergunta/<int:numero>")
def pegar_pergunta(numero):
    if numero < 0 or numero >= len(perguntas):
        return jsonify({"fim": True})
    return jsonify({"fim": False, "pergunta": perguntas[numero]["pergunta"]})


@app.route("/verificar", methods=["POST"])
def verificar():
    dados = request.get_json()
    numero = dados.get("numero")
    resposta = dados.get("resposta", "").strip().lower()

    aceitas = perguntas[numero]["aceitas"]
    acertou = any(frase in resposta for frase in aceitas)

    if acertou:
        mensagem = "Parabéns futuro(a) Ministro(a) da Justiça! Você arrasa no Civil!"
    else:
        mensagem = "Ops, o STF perdoa essa, mas vamos revisar?"

    return jsonify({"acertou": acertou, "mensagem": mensagem})


if __name__ == "__main__":
    app.run(debug=True)
