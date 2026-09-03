# PROJETO ECLIPSE — Engine com Suporte a Imagens por Cena
# Jogo de aventura/terror sci-fi

# ============================================================
# MAPEAMENTO DE IMAGENS POR CENA
# ============================================================
CENAS_IMAGENS = {
    "inicio": "assets/imagens/despertar.png",
    "armario": "assets/imagens/armario.png",
    "corredor": "assets/imagens/corredor.jfif",
    "porta_restrita": "assets/imagens/porta_blindada.jfif",
    "porta": "assets/imagens/porta_seguranca.jfif",
    "controle": "assets/imagens/sala_controle.jfif",
    "subsolo": "assets/imagens/laboratorios_inferiores.jfif",
    "sala17": "assets/imagens/sala17.jfif",
    "laboratorio": "assets/imagens/tanques_clonagem.jfif",
    "gerador": "assets/imagens/gerador.jfif",
    "sala": "assets/imagens/sala_escura.jfif",
    "arquivo": "assets/imagens/arquivo_morto.jfif",
    "memorias": "assets/imagens/camara_memorias.jfif",
    "verdade": "assets/imagens/revelacao_original.jfif",
    "alarme": "assets/imagens/alarme_criatura.jfif",
    "tunel": "assets/imagens/duto_ventilacao.jfif",
    "sala_secreta": "assets/imagens/cadeira_neural.jfif",
    "nucleo": "assets/imagens/nucleo_reator.jfif",
    "nucleo_perigoso": "assets/imagens/explosao_plasma.jfif",
    "libertar": "assets/imagens/rede_global.jfif",
    "fuga_dupla": "assets/imagens/fuga_capsula.jfif",
    "saida_falsa": "assets/imagens/floresta_copias.jfif",
    "fim_verdadeiro": "assets/imagens/fim_liberdade.jfif",
    "fim_sacrificio": "assets/imagens/fim_sacrificio.jfif",
    "fim_copias": "assets/imagens/floresta_copias.jfif",
    "fim_egoista": "assets/imagens/fim_egoista.jfif",
    "final_digital": "assets/imagens/deus_digital.jfif",
    "final_memorias": "assets/imagens/mente_coletiva.jfif",
    "fim_libertador": "assets/imagens/fim_libertador.jfif",
    "fim_misterioso": "assets/imagens/ciclo_continua.jfif",
    "fim_ruim": "assets/imagens/game_over.jfif",
}


def exibir_imagem(nome_cena):
    """Puxa e renderiza a imagem no navegador se estiver em PyScript, ou exibe o caminho em terminal."""
    caminho = CENAS_IMAGENS.get(nome_cena, "assets/imagens/capa.jfif")
    try:
        from pyscript import window
        if hasattr(window, "frameworkImage"):
            window.frameworkImage.show(caminho)
    except Exception:
        # Fallback informativo para execução local via console padrão
        print(f"\n[CENA VISUAL: {caminho}]")


# ============================================================
# SISTEMA DE MÚSICA ADICIONADO AQUI
# ============================================================
musica_iniciada = False

def tocar_musica_fundo():
    """Toca a música de fundo usando a API do navegador via PyScript."""
    global musica_iniciada
    if musica_iniciada:
        return # Se já estiver tocando, não faz nada e segue o jogo normal
    try:
        from js import Audio
        musica = Audio.new("musica_de_fundo.mp3") 
        musica.loop = True # Faz a música repetir infinitamente
        musica.play()
        musica_iniciada = True
    except Exception:
        pass


def escolher(pergunta, opcoes):
    while True:
        print(pergunta)
        resposta = input("\nEscolha: ").strip().lower()
        
        # O navegador libera o áudio assim que o jogador interage.
        # Então, tentamos tocar a música logo após a resposta dele!
        tocar_musica_fundo()

        if resposta in opcoes:
            return resposta
        print("\nOpção inválida. Digite uma das opções mostradas.")


state = {
    "vida": 5,
    "inv": set(),
    "codigo": [],
    "verdade": False,
    "original": False,
    "original_salvo": False,
    "gerador": False,
    "mapa": False,
    "radio": False,
    "monstro": False,
    "final": None,
}


def pegar(item):
    if item not in state["inv"]:
        state["inv"].add(item)
        print(f"\n[ITEM] Você encontrou: {item}.")


def dano(valor=1):
    state["vida"] = max(0, state["vida"] - valor)
    print(f"\n[VIDA] {state['vida']}/5")
    return state["vida"] > 0


def status():
    itens = ", ".join(sorted(state["inv"])) or "vazio"
    print(f"\n--- Vida: {state['vida']}/5 | Inventário: {itens} ---")


# ------------------------------------------------------------
# INÍCIO
# ------------------------------------------------------------

def inicio():
    print("""
============================================================
                    PROJETO ECLIPSE
============================================================

Você acorda no chão de um laboratório. Uma luz vermelha
pisca no teto.

Você não lembra seu nome.

Um alto-falante anuncia:

"PROTOCOLO DE CONTENÇÃO ATIVO."
"TEMPO PARA COLAPSO: 47 MINUTOS."

Na porta está escrito:

"NÃO CONFIE NAQUELE QUE TEM O SEU ROSTO."
""")
    status()

    op = escolher("""
O que você faz?
1) Investigar o corredor
2) Abrir o armário
3) Examinar a porta restrita
4) Procurar uma saída
""", {"1", "2", "3", "4"})

    return {"1": "corredor", "2": "armario",
            "3": "porta_restrita", "4": "sala"}.get(op)


# ------------------------------------------------------------
# ARMÁRIO
# ------------------------------------------------------------

def armario():
    print("\n=== ARMÁRIO DE EMERGÊNCIA ===")

    disponiveis = []
    if "lanterna" not in state["inv"]:
        disponiveis.append("1) Pegar lanterna")
    if "chave" not in state["inv"]:
        disponiveis.append("2) Pegar chave")
    if "kit" not in state["inv"]:
        disponiveis.append("3) Pegar kit médico")
    if "cracha" not in state["inv"]:
        disponiveis.append("4) Pegar crachá")

    disponiveis.append("5) Examinar fotografia")
    disponiveis.append("6) Sair")

    op = escolher("\n" + "\n".join(disponiveis), {str(i) for i in range(1, 7)})

    if op == "1":
        pegar("lanterna")
        print("Agora você consegue enxergar os laboratórios inferiores.")
        return "subsolo"

    if op == "2":
        pegar("chave")
        print("A chave parece pertencer a uma porta de segurança.")
        return "porta"

    if op == "3":
        pegar("kit")
        state["vida"] = min(5, state["vida"] + 2)
        print("Você usa o kit e recupera parte da sua energia.")
        return "armario"

    if op == "4":
        pegar("cracha")
        print('O crachá mostra: "Dr. Mateus Almeida".')
        return "porta_restrita"

    if op == "5":
        state["verdade"] = True
        print("""
A fotografia mostra cientistas do Projeto Eclipse.
No centro está um homem com o seu rosto.

No verso:
"Dr. Mateus Almeida — Diretor do Projeto."
""")
        return "corredor"

    return "corredor"


# ------------------------------------------------------------
# CORREDOR
# ------------------------------------------------------------

def corredor():
    print("""
=== CORREDOR PRINCIPAL ===

Três caminhos estão diante de você.
À esquerda: SALA DE CONTROLE.
À direita: LABORATÓRIOS INFERIORES.
À frente: PORTA DE SEGURANÇA.

Você escuta uma batida vindo do andar inferior.
TOC... TOC... TOC...
""")

    op = escolher("""
1) Ir para a sala de controle
2) Descer para os laboratórios
3) Tentar a porta de segurança
4) Voltar ao laboratório
""", {"1", "2", "3", "4"})

    return {"1": "controle", "2": "subsolo",
            "3": "porta", "4": "laboratorio"}[op]


# ------------------------------------------------------------
# PORTAS
# ------------------------------------------------------------

def porta_restrita():
    print("\n=== PORTA RESTRITA ===")

    if "cracha" in state["inv"]:
        print("""
O leitor reconhece parcialmente o crachá.

"DR. MATEUS ALMEIDA."
A porta se abre.
""")
        return "laboratorio"

    op = escolher("""
A porta exige identificação.

1) Procurar um crachá
2) Forçar o painel
3) Voltar
""", {"1", "2", "3"})

    if op == "1":
        return "armario"

    if op == "2":
        print("Você força o painel e recebe uma descarga.")
        if not dano():
            return "fim_ruim"
        return "corredor"

    return "corredor"


def porta():
    print("\n=== PORTA DE SEGURANÇA ===")

    if "chave" in state["inv"] or "cracha" in state["inv"]:
        print("O mecanismo reconhece seu acesso e a porta destranca.")
        return "sala"

    op = escolher("""
A porta está trancada.

1) Procurar uma chave
2) Procurar um crachá
3) Forçar a porta
""", {"1", "2", "3"})

    if op == "1":
        return "armario"
    if op == "2":
        return "porta_restrita"

    print("A porta não se move e você se machuca.")
    return "fim_ruim" if not dano() else "corredor"


# ------------------------------------------------------------
# SALA DE CONTROLE
# ------------------------------------------------------------

def controle():
    print("\n=== SALA DE CONTROLE ===")

    op = escolher("""
Um monitor mostra: PROJETO ECLIPSE — STATUS CRÍTICO.

1) Ler o relatório
2) Ler o protocolo de evacuação
3) Ler o arquivo pessoal
4) Ativar o computador central
5) Sair
""", {"1", "2", "3", "4", "5"})

    if op == "1":
        state["verdade"] = True
        print("""
O projeto começou estudando memórias humanas.
Depois, os cientistas descobriram como copiar uma consciência.

O problema:
as cópias acreditavam ser as pessoas originais.
""")
        return "controle"

    if op == "2":
        print("""
PROTOCOLO DE EVACUAÇÃO:
1. Restaurar o gerador.
2. Encontrar as três partes do código.
3. Inserir o código no núcleo.
""")
        return "corredor"

    if op == "3":
        state["verdade"] = True
        print("""
ARQUIVO PESSOAL — DR. MATEUS ALMEIDA

"Se meu experimento funcionar, uma cópia minha acordará
sem saber que é uma cópia."
""")
        return "laboratorio"

    if op == "4":
        pegar("acesso central")
        print("O computador libera novas áreas do complexo.")
        return "controle"

    return "corredor"


# ------------------------------------------------------------
# SUBSOLO / SALA 17
# ------------------------------------------------------------

def subsolo():
    print("\n=== LABORATÓRIOS INFERIORES ===")

    if "lanterna" not in state["inv"]:
        print("Está escuro demais. Você não consegue avançar.")
        return "armario"

    op = escolher("""
A lanterna revela duas placas.

1) SALA 17 — SETOR MÉDICO
2) LABORATÓRIO PRINCIPAL
3) ARQUIVO SUBTERRÂNEO
4) Voltar
""", {"1", "2", "3", "4"})

    return {"1": "sala17", "2": "laboratorio",
            "3": "arquivo", "4": "corredor"}[op]


def sala17():
    print("""
=== SALA 17 ===

Um monitor exibe:

PACIENTE 07
IDENTIDADE: MATEUS ALMEIDA
MEMÓRIA: INCOMPLETA
""")

    op = escolher("""
1) Examinar a maca
2) Examinar o computador
3) Procurar no armário
4) Sair
""", {"1", "2", "3", "4"})

    if op == "1":
        if "parte 1" not in state["inv"]:
            pegar("parte 1")
            state["codigo"].append("741")
            print("Você encontrou a primeira parte do código: 7-4-1.")
        else:
            print("A maca está vazia. Você já pegou o que havia aqui.")
        return "sala17"

    if op == "2":
        state["verdade"] = True
        print("""
O computador desbloqueia sozinho.

"Paciente 07 não é um sobrevivente."
"Paciente 07 é o experimento."
"Memórias implantadas com sucesso."
""")
        return "laboratorio"

    if op == "3":
        pegar("kit")
        print("Há um aviso: o material deve ser usado apenas em emergências.")
        return "sala17"

    return "subsolo"


# ------------------------------------------------------------
# LABORATÓRIO
# ------------------------------------------------------------

def laboratorio():
    print("""
=== LABORATÓRIO PRINCIPAL ===

No centro existe uma máquina enorme.
Na tela:

ECLIPSE
ENERGIA: 23%
CONTENÇÃO: INSTÁVEL
""")

    op = escolher("""
1) Examinar a máquina
2) Procurar documentos
3) Procurar o gerador
4) Procurar uma passagem secreta
5) Sair
""", {"1", "2", "3", "4", "5"})

    if op == "1":
        state["verdade"] = True
        state["monstro"] = True
        print("""
A máquina reconhece seu rosto.

"IDENTIDADE: MATEUS ALMEIDA."

As telas mostram dezenas de pessoas iguais a você.
Você percebe que existem várias cópias.
""")
        return "sala"

    if op == "2":
        if "parte 2" not in state["inv"]:
            pegar("parte 2")
            state["codigo"].append("926")
            pegar("mapa")
            print("A segunda parte do código é 9-2-6.")
        else:
            print("Os documentos já foram examinados.")
        return "laboratorio"

    if op == "3":
        return "gerador"

    if op == "4":
        if "mapa" in state["inv"]:
            print("O mapa revela uma parede falsa.")
            return "arquivo"
        print("Você não encontra nada. Talvez um mapa possa ajudar.")
        return "laboratorio"

    return "subsolo"


# ------------------------------------------------------------
# GERADOR
# ------------------------------------------------------------

def gerador():
    print("\n=== GERADOR ===")

    if state["gerador"]:
        print("O gerador já está funcionando.")
        return "laboratorio"

    op = escolher("""
1) Ligar o gerador
2) Examinar o painel
3) Voltar
""", {"1", "2", "3"})

    if op == "1":
        state["gerador"] = True
        print("""
Você puxa a alavanca.

VRRRRRRR...

As luzes voltam.
Todas as portas se fecham.

ALARME: CONTENÇÃO ATIVA.
""")
        return "alarme"

    if op == "2":
        pegar("chave magnética")
        print("O painel indica que o núcleo precisa ser estabilizado.")
        return "laboratorio"

    return "laboratorio"


# ------------------------------------------------------------
# SALA ESCURA / RÁDIO
# ------------------------------------------------------------

def sala():
    print("""
=== SALA ESCURA ===

Um rádio liga sozinho.

"...não ligue o gerador..."
"...eles vão perceber que você está vivo..."

Depois, uma voz diz:

"Mateus."

""")

    op = escolher("""
1) Responder pelo rádio
2) Examinar o rádio
3) Procurar uma saída
4) Voltar
""", {"1", "2", "3", "4"})

    if op == "1":
        state["radio"] = True
        print("""
"Quem está falando?"

"Alguém que tentou escapar."

"Quem é você?"

"Eu sou você."
""")
        return "arquivo"

    if op == "2":
        pegar("chave magnética")
        print("Dentro do rádio existe uma chave magnética.")
        return "laboratorio"

    if op == "3":
        return "tunel"

    return "corredor"


# ------------------------------------------------------------
# ARQUIVO / MEMÓRIAS
# ------------------------------------------------------------

def arquivo():
    print("""
=== ARQUIVO SUBTERRÂNEO ===

Há centenas de caixas.
Muitas possuem o nome MATEUS ALMEIDA.

Uma porta diz:
"MEMÓRIAS ORIGINAIS"
""")

    op = escolher("""
1) Abrir a porta
2) Procurar documentos
3) Procurar a terceira parte do código
4) Voltar
""", {"1", "2", "3", "4"})

    if op == "1":
        return "memorias"

    if op == "2":
        state["verdade"] = True
        print('Você encontra: "PACIENTE 07 — CÓPIA Nº 13".')
        return "arquivo"

    if op == "3":
        if "parte 3" not in state["inv"]:
            pegar("parte 3")
            state["codigo"].append("835")
            print("A terceira parte do código é 8-3-5.")
        else:
            print("Você já encontrou essa parte.")
        return "arquivo"

    return "sala"


def memorias():
    state["original"] = True
    print("""
=== MEMÓRIAS ORIGINAIS ===

Dentro da sala há várias cápsulas.
Uma delas possui a etiqueta:

MATEUS ALMEIDA
ORIGINAL
STATUS: VIVO
""")

    op = escolher("""
1) Abrir a cápsula
2) Destruir o sistema
3) Ler o relatório
4) Sair
""", {"1", "2", "3", "4"})

    if op == "1":
        return "verdade"

    if op == "2":
        print("O sistema entra em alerta e bloqueia parte do laboratório.")
        return "alarme"

    if op == "3":
        state["verdade"] = True
        print("""
O relatório confirma:
o original foi mantido vivo para servir como fonte de memória.
As cópias recebem as mesmas lembranças.
""")
        return "memorias"

    return "arquivo"


def verdade():
    state["verdade"] = True
    print("""
=== A VERDADE ===

O homem dentro da cápsula acorda.

"Eu sou Mateus."

Você percebe que suas lembranças foram copiadas.
Você é uma cópia, mas suas experiências continuam sendo suas.
""")

    op = escolher("""
1) Ajudar o original
2) Fugir sozinho
3) Destruir o Eclipse
4) Perguntar como escapar
""", {"1", "2", "3", "4"})

    if op == "1":
        state["original_salvo"] = True
        return "fuga_dupla"
    if op == "2":
        return "fim_egoista"
    if op == "3":
        return "nucleo"
    return "tunel"


# ------------------------------------------------------------
# ALARME / TÚNEL
# ------------------------------------------------------------

def alarme():
    print("""
=== ALARME ===

As portas começam a fechar.
Você ouve passos se aproximando.

Algo está vindo pelo corredor.
""")

    op = escolher("""
1) Correr
2) Esconder-se
3) Procurar uma barra de ferro
4) Enfrentar a criatura
""", {"1", "2", "3", "4"})

    if op == "1":
        if "mapa" in state["inv"]:
            print("O mapa mostra um túnel de manutenção.")
            return "tunel"
        print("Você corre sem direção e perde energia.")
        return "fim_ruim" if not dano(2) else "corredor"

    if op == "2":
        state["monstro"] = True
        print("Você se esconde, mas percebe que a criatura sabe onde está.")
        return "laboratorio"

    if op == "3":
        pegar("barra")
        print("Você encontra uma barra de ferro.")
        return "alarme"

    if "barra" in state["inv"]:
        print("Você consegue afastar a criatura e alcançar o túnel.")
        return "tunel"

    print("Sem equipamento, você precisa recuar.")
    return "laboratorio"


def tunel():
    print("""
=== TÚNEL DE MANUTENÇÃO ===

Três portas aparecem:
AZUL, VERMELHA e PRETA.
""")

    op = escolher("""
1) Porta azul
2) Porta vermelha
3) Porta preta
""", {"1", "2", "3"})

    return {"1": "saida_falsa", "2": "nucleo",
            "3": "sala_secreta"}[op]


def sala_secreta():
    print("""
=== SALA SECRETA ===

Um espelho mostra seu rosto.

O reflexo sorri.

"Você finalmente chegou."

"Sou a versão que escapou primeiro."
""")

    op = escolher("""
1) Perguntar como escapar
2) Quebrar o espelho
3) Sentar na cadeira
4) Sair
""", {"1", "2", "3", "4"})

    if op == "1":
        return "nucleo"
    if op == "2":
        return "saida_falsa"
    if op == "3":
        return "final_memorias"
    return "tunel"


# ------------------------------------------------------------
# NÚCLEO E FINAIS
# ------------------------------------------------------------

def nucleo():
    print("""
=== NÚCLEO ECLIPSE ===

O monitor mostra:

CONSCIÊNCIAS CONECTADAS: 847
""")

    if len(state["codigo"]) < 3:
        print("\nO código ainda está incompleto.")
        op = escolher("""
1) Procurar as partes restantes
2) Desligar sem o código
3) Voltar
""", {"1", "2", "3"})

        if op == "1":
            if "parte 1" not in state["inv"]:
                return "sala17"
            if "parte 2" not in state["inv"]:
                return "laboratorio"
            return "arquivo"

        if op == "2":
            return "nucleo_perigoso"

        return "laboratorio"

    print("""
Código completo:
741926835
""")

    op = escolher("""
1) Desligar o Eclipse
2) Manter o Eclipse funcionando
3) Transferir sua consciência
4) Libertar todas as consciências
""", {"1", "2", "3", "4"})

    return {
        "1": "fim_sacrificio",
        "2": "fim_misterioso",
        "3": "final_digital",
        "4": "libertar"
    }[op]


def nucleo_perigoso():
    print("""
Você ignora o protocolo.
O núcleo começa a sobrecarregar.

10%... 30%... 70%...

O laboratório começa a tremer.
""")
    return "fim_ruim" if not dano(2) else "tunel"


def libertar():
    if "kit" in state["inv"]:
        print("""
Você usa o estabilizador do kit para suportar a sobrecarga.
As consciências são libertadas e você sobrevive.
""")
        return "fim_libertador"

    print("""
Você tenta libertar todas as consciências.
A sobrecarga é grande demais e você acaba conectado ao sistema.
""")
    return "final_digital"


def fuga_dupla():
    print("""
Você ajuda o verdadeiro Mateus a escapar.

Na bifurcação, vocês precisam decidir o caminho.
""")

    op = escolher("""
1) Seguir pelo túnel
2) Ir para a saída principal
3) Voltar e destruir o Eclipse
""", {"1", "2", "3"})

    if op == "1":
        return "tunel"
    if op == "2":
        return "fim_verdadeiro"
    return "nucleo"


# ------------------------------------------------------------
# FINAIS
# ------------------------------------------------------------

def saida_falsa():
    print("""
=== FINAL: O EXÉRCITO DE CÓPIAS ===

Você chega à floresta.

Dezenas de pessoas aparecem entre as árvores.
Todas possuem o mesmo rosto que você.

Uma delas diz:

"Bem-vindo de volta, Paciente 07."
""")
    state["final"] = "O Exército de Cópias"
    return "fim"


def fim_verdadeiro():
    print("""
=== FINAL BOM: A VERDADEIRA FUGA ===

Você e o verdadeiro Mateus conseguem escapar.
O Projeto Eclipse é encerrado.

Você percebe que sua origem não define quem você é.
Suas escolhas definem.
""")
    state["final"] = "A Verdadeira Fuga"
    return "fim"


def fim_sacrificio():
    print("""
=== FINAL: O SACRIFÍCIO ===

Você desliga o Eclipse e liberta as consciências.
O sistema é encerrado.

Você fez a escolha que ninguém mais conseguiu fazer.
""")
    state["final"] = "O Sacrifício"
    return "fim"


def fim_copias():
    return saida_falsa()


def fim_egoista():
    print("""
=== FINAL: O SOBREVIVENTE ===

Você abandona o original e foge sozinho.

Meses depois, uma mensagem chega:

"Eu sei onde você está."
""")
    state["final"] = "O Sobrevivente"
    return "fim"


def final_digital():
    print("""
=== FINAL SECRETO: DEUS DIGITAL ===

Sua consciência é transferida para o sistema.
Você passa a existir dentro da rede.

O Eclipse pergunta:

"QUAL É SUA PRÓXIMA ORDEM?"
""")
    state["final"] = "Deus Digital"
    return "fim"


def final_memorias():
    print("""
=== FINAL SECRETO: TODAS AS MEMÓRIAS ===

Você recupera todas as memórias das versões anteriores.
Finalmente entende toda a história do Eclipse.

Você aceita que algumas coisas precisam terminar.
""")
    state["final"] = "Todas as Memórias"
    return "fim"


def fim_libertador():
    print("""
=== FINAL BOM: O LIBERTADOR ===

Todas as consciências são libertadas.
O laboratório é destruído.

Quando perguntam se você é humano, você responde:

"Não sei. Mas sei que estou vivo."
""")
    state["final"] = "O Libertador"
    return "fim"


def fim_misterioso():
    print("""
=== FINAL RUIM: O CICLO CONTINUA ===

Você deixa o Eclipse funcionando.

Mais tarde, uma mensagem aparece:

"NOVO PACIENTE REGISTRADO."

PACIENTE 08.
PACIENTE 09.
PACIENTE 10...

O Eclipse continua.
""")
    state["final"] = "O Ciclo Continua"
    return "fim"


def fim_ruim():
    print("""
=== FIM DE JOGO ===

Você não conseguiu escapar.
O Projeto Eclipse continua funcionando.

Em algum lugar, uma nova cápsula é ativada.
""")
    state["final"] = "Fim de Jogo"
    return "fim"


# ------------------------------------------------------------
# MOTOR DO JOGO COM TRANSIÇÃO DE IMAGENS E MÚSICA
# ------------------------------------------------------------

cenas = {
    "inicio": inicio,
    "armario": armario,
    "corredor": corredor,
    "porta_restrita": porta_restrita,
    "porta": porta,
    "controle": controle,
    "subsolo": subsolo,
    "sala17": sala17,
    "laboratorio": laboratorio,
    "gerador": gerador,
    "sala": sala,
    "arquivo": arquivo,
    "memorias": memorias,
    "verdade": verdade,
    "alarme": alarme,
    "tunel": tunel,
    "sala_secreta": sala_secreta,
    "nucleo": nucleo,
    "nucleo_perigoso": nucleo_perigoso,
    "libertar": libertar,
    "fuga_dupla": fuga_dupla,
    "saida_falsa": saida_falsa,
    "fim_verdadeiro": fim_verdadeiro,
    "fim_sacrificio": fim_sacrificio,
    "fim_copias": fim_copias,
    "fim_egoista": fim_egoista,
    "final_digital": final_digital,
    "final_memorias": final_memorias,
    "fim_libertador": fim_libertador,
    "fim_misterioso": fim_misterioso,
    "fim_ruim": fim_ruim,
}

cena = "inicio"

while cena != "fim":
    exibir_imagem(cena)
    cena = cenas[cena]()

# Imagem do final alcançado
if state.get("final"):
    exibir_imagem(cena)

print("""
============================================================
                     FIM DO JOGO
============================================================
""")
print("Inventário:", ", ".join(sorted(state["inv"])) or "vazio")
print(f"Vida final: {state['vida']}/5")
print("Final alcançado:", state["final"])
print("\nObrigado por jogar PROJETO ECLIPSE!")
