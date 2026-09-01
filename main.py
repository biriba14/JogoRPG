# ============================================================
# PROJETO ECLIPSE - LÓGICA DINÂMICA E VALIDADA
# ============================================================

from pyscript import web, when, window

CONFIG = {
    "titulo": "PROJETO ECLIPSE",
    "subtitulo": "Uma aventura de terror sci-fi",
    "autor": "Anna Beatriz",
    "icone": "🌑",
    "capa": "assets/imagens/capa.jfif",
    "trilha_inicial": "assets/audios/tema_principal.mp3",
    "volume_inicial": 0.5,
    "vida_inicial": 5,
    "pontos_iniciais": 0,
    "cena_inicial": "inicio",
}

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],
    # Flags de controle de eventos únicos
    "armario_ferramentas_pego": False,
    "armario_suprimentos_pego": False,
    "computador_hackeado": False,
    "codigo2_pego": False,
    "codigo3_pego": False,
}

# ============================================================
# MAPA DE CENAS NARRATIVAS
# ============================================================

SCENES = {
    "inicio": {
        "title": "O Despertar",
        "image": "assets/imagens/laboratorio_inicio.jpg",
        "text": (
            "Você acorda deitado no chão frio de um laboratório. Sua cabeça dói. Uma luz vermelha pisca no teto.\n\n"
            "Você não sabe onde está e não consegue lembrar seu próprio nome. Há sangue nas suas mãos.\n\n"
            'Um som metálico ecoa: "PROTOCOLO DE CONTENÇÃO ATIVO. TEMPO ESTIMADO PARA COLAPSO: 47 MINUTOS."\n\n'
            'Uma porta à sua frente possui uma mensagem escrita com tinta vermelha:\n'
            '"NÃO CONFIE NAQUELE QUE TENHA O SEU ROSTO."'
        ),
    },

    "armario": {
        "title": "Armário de Emergência",
        "image": "assets/imagens/armario.jpg",
        "text": "O armário metálico range ao abrir. Prateleiras de metal oxidado guardam resquícios de equipamentos abandonados.",
    },

    "armario_foto": {
        "title": "A Fotografia",
        "image": "assets/imagens/armario.jpg",
        "text": (
            'Você observa a foto empoeirada. Um grupo de pesquisadores sorri. No centro, o homem é idêntico a você.\n\n'
            'No verso: "Equipe Eclipse - Ano 2038. Dr. Mateus Almeida."\n'
            'Sua cabeça lateja com uma lembrança falsa.'
        ),
        "options": [("Voltar ao armário", "armario")],
    },

    "corredor": {
        "title": "Corredor Principal",
        "image": "assets/imagens/corredor.jpg",
        "text": (
            "As luzes de emergência estalam. Três rotas se abrem diante de você:\n"
            "A Sala de Controle, a escadaria escura para os Laboratórios Inferiores e a Porta de Segurança trancada."
        ),
    },

    "porta_choque": {
        "title": "Descarga Elétrica!",
        "image": "assets/imagens/porta_trancada.jpg",
        "text": (
            "Você tenta forçar o painel sem a autorização ou ferramenta adequada.\n"
            "Faíscas azuis explodem em seu braço! Você perdeu 1 vida por descuido e recua tossindo fumaça."
        ),
        "options": [("Recuar para o corredor", "corredor")],
    },

    "queda_escada": {
        "title": "Queda no Escuro",
        "image": "assets/imagens/subsolo.jpg",
        "text": (
            "Você tentou tatear a descida para o subsolo sem nenhuma fonte de luz.\n"
            "O piso estava molhado de óleo; você escorregou e rolou escada abaixo no breu total. Perdeu 1 vida."
        ),
        "options": [("Levantar-se machucado", "corredor")],
    },

    "controle": {
        "title": "Sala de Controle",
        "image": "assets/imagens/sala_controle.jpg",
        "text": "Monitores cinzentos cercam a sala. Apenas um terminal central permanece ativo emitindo um zumbido abafado.",
    },

    "ler_arquivos": {
        "title": "Arquivos Confidenciais",
        "image": "assets/imagens/sala_controle.jpg",
        "text": (
            "RELATÓRIO: A transferência de mente gera réplicas perfeitas que herdam falsas memórias do original.\n"
            "AVISO: A única forma de desativar o complexo é reunir as 3 partes do código de segurança."
        ),
        "options": [("Fechar arquivos", "controle")],
    },

    "ouvir_gravacao": {
        "title": "Registro de Áudio #07",
        "image": "assets/imagens/sala_controle.jpg",
        "text": (
            '"Se você está ouvindo isso, o procedimento funcionou mal. Eu criei uma cópia exata de mim mesmo...\n'
            'Mas se ela descobrir a verdade, o laboratório inteiro cairá."'
        ),
        "options": [("Desligar áudio", "controle")],
    },

    "ativar_pc": {
        "title": "Terminal Hackeado",
        "image": "assets/imagens/sala_controle.jpg",
        "text": "Você digita impulsivamente a sequência numérica 071984. Acesso concedido! A PRIMEIRA PARTE DO CÓDIGO foi descarregada.",
        "options": [("Voltar à sala de controle", "controle")],
    },

    "subsolo": {
        "title": "Laboratórios Inferiores",
        "image": "assets/imagens/subsolo.jpg",
        "text": "O ar aqui embaixo é pesado e cheira a ozônio queimado. Marcas de unhas profundas arranham as paredes de aço reforçado.",
    },

    "sala17": {
        "title": "Sala 17 - Isolamento",
        "image": "assets/imagens/subsolo.jpg",
        "text": "Uma maca cirúrgica abandonada. No visor médico pisca: PACIENTE 07 - CÓPIA ATIVA.\nVocê vasculha o chão e acha a SEGUNDA PARTE DO CÓDIGO de segurança.",
    },

    "laboratorio": {
        "title": "Laboratório Principal",
        "image": "assets/imagens/laboratorio_principal.jpg",
        "text": "Tanques de clonagem vazios estourados. Rostos idênticos ao seu formam mosaicos nas telas quebradas.",
    },

    "gerador": {
        "title": "Sala do Gerador",
        "image": "assets/imagens/gerador.jpg",
        "text": "O motor auxiliar está estagnado. Uma alavanca pesada de emergência aguarda para ser acionada.",
    },

    "alarme": {
        "title": "Alarme Geral Disparado!",
        "image": "assets/imagens/alarme.jpg",
        "audio": "assets/audios/alarme.mp3",
        "text": "Luzes estroboscópicas vermelhas cegam você. Passos pesados ecoam correndo em sua direção... É uma criatura com o seu próprio rosto!",
        "options": [
            ("Disparar para o Túnel de Manutenção", "tunel"),
            ("Enfrentar o monstro de frente", "lutar_criatura"),
        ],
    },

    "dano_criatura": {
        "title": "Confronto Brutal",
        "image": "assets/imagens/alarme.jpg",
        "text": "Você tenta conter sua cópia irracional, mas ela é implacável. Você é jogado contra o painel e perde 2 vidas preciosas antes de escapar.",
        "options": [("Arrastar-se para o túnel", "tunel")],
    },

    "arquivo": {
        "title": "Arquivo Morto",
        "image": "assets/imagens/arquivo.jpg",
        "text": "Milhares de fichas de pacientes. Vasculhando a seção principal, você encontra a TERCEIRA PARTE DO CÓDIGO.",
    },

    "memorias": {
        "title": "Câmara de Memórias",
        "image": "assets/imagens/memorias.jpg",
        "text": "Uma cápsula central exibe o verdadeiro Dr. Mateus Almeida em animação suspensa. Ele desperta e sussurra: 'Você é apenas uma cópia...'",
        "options": [
            ("Libertar e ajudar o verdadeiro criador", "fuga_dupla"),
            ("Abandoná-lo à própria sorte", "fim_egoista"),
            ("Seguir direto para o Núcleo", "nucleo"),
        ],
    },

    "tunel": {
        "title": "Túnel de Ventilação",
        "image": "assets/imagens/tunel.jpg",
        "text": "Um duto claustrofóbico que se divide em três tubulações de escape.",
        "options": [
            ("Tomar o duto azul (Superfície)", "saida_falsa"),
            ("Tomar o duto vermelho (Núcleo Central)", "nucleo"),
            ("Tomar o duto preto (Sala Oculta)", "sala_secreta"),
        ],
    },

    "sala_secreta": {
        "title": "Laboratório Clandestino",
        "image": "assets/imagens/sala_secreta.jpg",
        "text": "Uma cadeira com eletrodos e um espelho intrigante. O seu reflexo sorri sozinho e pergunta: 'Deseja recuperar tudo o que perdeu?'",
        "options": [
            ("Conectar-se à máquina de memórias", "final_memorias"),
            ("Destruir o espelho e fugir", "saida_falsa"),
        ],
    },

    "nucleo": {
        "title": "Núcleo do Reator",
        "image": "assets/imagens/nucleo.jpg",
        "text": "O reator pulsa energia pura. O console principal aguarda o código completo de evacuação para desligamento seguro.",
        "options": [
            ("Digitar as 3 partes do código de segurança", "tentar_desligar"),
            ("Desconectar os cabos principais à força", "nucleo_perigoso"),
            ("Transmitir o sinal para toda a rede", "fim_libertador"),
        ],
    },

    "nucleo_perigoso": {
        "title": "Colapso Imediato!",
        "image": "assets/imagens/nucleo.jpg",
        "text": "Ao arrancar os cabos principais, o núcleo entra em fusão descontrolada! Você é soterrado por destroços ardentes e perde 2 vidas.",
        "options": [("Tentar escapar pelos escombros", "tunel")],
    },

    "fuga_dupla": {
        "title": "FINAL: A VERDADEIRA FUGA",
        "image": "assets/imagens/final_bom.jpg",
        "text": "Você e o verdadeiro criador escapam segundos antes da detonação total. Sua identidade é artificial, mas sua escolha foi genuína.\n\nFINAL BOM.",
        "options": [],
    },
    
    "fim_egoista": {
        "title": "FINAL: O SOBREVIVENTE",
        "image": "assets/imagens/final_ruim.jpg",
        "text": "Você foge sozinho para o mundo exterior. Meses mais tarde, alguém bate à sua porta... É o verdadeiro Mateus cobrando contas.\n\nFINAL RUIM.",
        "options": [],
    },

    "saida_falsa": {
        "title": "FINAL: EXÉRCITO DE CÓPIAS",
        "image": "assets/imagens/final_ruim.jpg",
        "text": "Você emerge na floresta exterior. Mas ao olhar ao redor, centenas de pessoas com o seu rosto te encaram em silêncio absoluto.\n\nFINAL RUIM.",
        "options": [],
    },

    "fim_sacrificio": {
        "title": "FINAL: O SACRIFÍCIO",
        "image": "assets/imagens/final_sacrificio.jpg",
        "text": "O código é aceito. O complexo inteiro é purgado, apagando todas as consciências sintéticas — incluindo a sua. Você salvou o mundo.\n\nFINAL HERÓICO.",
        "options": [],
    },

    "final_memorias": {
        "title": "FINAL SECRETO: CONSCIÊNCIA TOTAL",
        "image": "assets/imagens/final_sacrificio.jpg",
        "text": "Você absorve o eco de todas as cópias que vieram antes. Você lembra de cada morte e desliga o sistema por dentro com sabedoria absoluta.\n\nFINAL SECRETO.",
        "options": [],
    },

    "fim_libertador": {
        "title": "FINAL: O LIBERTADOR",
        "image": "assets/imagens/final_bom.jpg",
        "text": "Você transmite os dados para a internet global. Milhares de cópias despertam simultaneamente. O mundo nunca mais será o mesmo.\n\nFINAL BOM ALTERNATIVO.",
        "options": [],
    },

    "fim_ruim": {
        "title": "GAME OVER",
        "image": "assets/imagens/game_over.jpg",
        "text": "Seu corpo cede aos ferimentos e à exaustão. A escuridão te consome. O Projeto Eclipse reiniciará o ciclo amanhã.",
        "options": [],
    },
}

# ============================================================
# VALIDAÇÃO DINÂMICA DE OPÇÕES (INTELIGÊNCIA DE ESTADO)
# ============================================================

def opcoes_da_cena(nome, cena):
    """Gera as opções de forma dinâmica com base no que já foi pego ou feito."""
    opcoes = []

    if nome == "inicio":
        opcoes = [
            ("Investigar o corredor principal", "corredor"),
            ("Vasculhar o armário de emergência", "armario"),
            ("Forçar a porta restrita à força", "tentar_porta_restrita"),
        ]

    elif nome == "armario":
        # Se ainda não pegou as ferramentas, exibe a opção. Se já pegou, oculta!
        if not state["armario_ferramentas_pego"]:
            opcoes.append(("Pegar a lanterna pesada e a chave", "pegar_ferramentas"))
        
        if not state["armario_suprimentos_pego"]:
            opcoes.append(("Pegar o kit médico e o crachá", "pegar_suprimentos"))
            
        opcoes.append(("Examinar a fotografia antiga", "ver_fotografia"))
        opcoes.append(("Voltar ao laboratório", "inicio"))

    elif nome == "corredor":
        opcoes = [
            ("Ir para a Sala de Controle", "controle"),
            ("Descer para os Laboratórios Inferiores", "descer_escadas"),
            ("Tentar abrir a Porta de Segurança", "tentar_porta_seguranca"),
            ("Voltar à sala inicial", "inicio"),
        ]

    elif nome == "controle":
        opcoes = [
            ("Ler os relatórios do projeto", "ler_arquivos"),
            ("Ouvir o diário de áudio corrompido", "ouvir_gravacao"),
        ]
        # O terminal só pode ser hackeado uma vez
        if not state["computador_hackeado"]:
            opcoes.append(("Hackear o terminal central", "ativar_pc"))
        opcoes.append(("Retornar ao corredor", "corredor"))

    elif nome == "subsolo":
        opcoes = []
        if not state["codigo2_pego"]:
            opcoes.append(("Investigar a Sala 17 (Setor Médico)", "sala17"))
        opcoes.extend([
            ("Avançar para o Laboratório Principal", "laboratorio"),
        ])
        if not state["codigo3_pego"]:
            opcoes.append(("Examinar o Arquivo Subterrâneo", "arquivo"))
        opcoes.append(("Retornar ao andar superior", "corredor"))

    elif nome == "sala17":
        opcoes = [("Guardar código e sair", "pegar_codigo2")]

    elif nome == "arquivo":
        opcoes = [
            ("Acessar o terminal de Memórias Originais", "memorias"),
            ("Pegar código e retornar aos laboratórios", "pegar_codigo3"),
        ]

    # Se a cena já tiver opções fixas cadastradas no dicionário e não tratadas acima, usa elas
    elif "options" in cena:
        opcoes = list(cena["options"])

    return opcoes

# ============================================================
# MOTOR DE EXECUÇÃO
# ============================================================

def el(id_elem):
    return web.page[id_elem]

def configurar_identidade():
    window.document.title = CONFIG["titulo"]
    el("titulo-abertura").innerText = CONFIG["titulo"]
    el("titulo-jogo").innerText = CONFIG["titulo"]
    el("autor-jogo").innerText = f"Autor: {CONFIG['autor']}"
    audio = el("audio-fundo")
    audio.dataset.inicial = CONFIG.get("trilha_inicial", "")

def atualizar_status():
    vida = state["vida"]
    if vida > 0:
        el("vida").innerText = " ".join(["❤️"] * vida)
        el("vida").classList.remove("danger")
    else:
        el("vida").innerText = "💀"
        el("vida").classList.add("danger")

    qtd = len(state["inventario"])
    el("inventario").innerText = f"{qtd} itens" if qtd > 0 else "Vazio"
    
    lista_html = ""
    if qtd > 0:
        for item in state["inventario"]:
            lista_html += f"<li>📦 {item}</li>"
    else:
        lista_html = "<li>Nenhum item coletado ainda.</li>"
    
    web.page["lista-itens"].innerHTML = lista_html
    el("pontos").innerText = str(state["pontos"])

def perder_vida(qtd=1):
    state["vida"] -= qtd
    if state["vida"] < 0: state["vida"] = 0
    atualizar_status()
    return state["vida"] <= 0

def adicionar_item(item, pts=0):
    if item not in state["inventario"]:
        state["inventario"].append(item)
        state["pontos"] += pts
    atualizar_status()

def possui_item(item):
    return item in state["inventario"]

def atualizar_botoes(opcoes):
    for i in range(1, 5):
        botao = el(f"opcao{i}")
        if i <= len(opcoes):
            botao.innerText = opcoes[i - 1][0]
            botao.style.display = "block"
            botao.disabled = False
        else:
            botao.style.display = "none"

def mostrar_cena(nome):
    if nome not in SCENES: return
    state["cena"] = nome
    cena = SCENES[nome]

    el("titulo-cena").innerText = cena.get("title", nome)
    el("texto-cena").innerText = cena.get("text", "")

    video = cena.get("video")
    img = cena.get("image")
    
    if video:
        window.frameworkVideo.play(video, cena.get("video_autoplay", False))
    elif img:
        window.frameworkVideo.stop()
        window.frameworkImage.show(img)
    else:
        window.frameworkVideo.stop()
        window.frameworkImage.hide()

    if "audio" in cena:
        if cena["audio"]: window.frameworkAudio.play(cena["audio"])
        else: window.frameworkAudio.stop()
    elif cena.get("stop_audio"):
        window.frameworkAudio.stop()

    # Puxa as opções validadas dinamicamente
    atualizar_botoes(opcoes_da_cena(nome, cena))
    atualizar_status()

def executar_acao(acao):
    if acao == "pegar_ferramentas":
        if not state["armario_ferramentas_pego"]:
            adicionar_item("Lanterna pesada")
            adicionar_item("Chave enferrujada")
            state["armario_ferramentas_pego"] = True
        mostrar_cena("armario_ferramentas")

    elif acao == "pegar_suprimentos":
        if not state["armario_suprimentos_pego"]:
            adicionar_item("Kit médico")
            adicionar_item("Crachá do Dr. Mateus")
            state["armario_suprimentos_pego"] = True
        mostrar_cena("armario_suprimentos")

    elif acao == "ver_fotografia":
        mostrar_cena("armario_foto")

    elif acao == "tentar_porta_restrita":
        if possui_item("Crachá do Dr. Mateus"):
            mostrar_cena("laboratorio")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque")

    elif acao == "tentar_porta_seguranca":
        if possui_item("Chave enferrujada"):
            mostrar_cena("arquivo")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque")

    elif acao == "descer_escadas":
        if possui_item("Lanterna pesada"):
            mostrar_cena("subsolo")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("queda_escada")

    elif acao == "ativar_pc":
        if not state["computador_hackeado"]:
            adicionar_item("Código de Acesso #1", 10)
            state["computador_hackeado"] = True
        mostrar_cena("ativar_pc")

    elif acao == "pegar_codigo2":
        if not state["codigo2_pego"]:
            adicionar_item("Código de Acesso #2", 10)
            state["codigo2_pego"] = True
        mostrar_cena("subsolo")

    elif acao == "pegar_codigo3":
        if not state["codigo3_pego"]:
            adicionar_item("Código de Acesso #3", 10)
            state["codigo3_pego"] = True
        mostrar_cena("subsolo")

    elif acao == "ligar_gerador":
        mostrar_cena("alarme")

    elif acao == "lutar_criatura":
        morreu = perder_vida(2)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("dano_criatura")

    elif acao == "tentar_desligar":
        if possui_item("Código de Acesso #1") and possui_item("Código de Acesso #2") and possui_item("Código de Acesso #3"):
            state["pontos"] += 50
            mostrar_cena("fim_sacrificio")
        else:
            mostrar_cena("nucleo")

    elif acao in SCENES:
        mostrar_cena(acao)

def escolher_opcao(num):
    opcoes = opcoes_da_cena(state["cena"], SCENES[state["cena"]])
    if (num - 1) < len(opcoes):
        executar_acao(opcoes[num - 1][1])

@when("click", "#opcao1")
def c1(e): escolher_opcao(1)
@when("click", "#opcao2")
def c2(e): escolher_opcao(2)
@when("click", "#opcao3")
def c3(e): escolher_opcao(3)
@when("click", "#opcao4")
def c4(e): escolher_opcao(4)

@when("click", "#reiniciar")
def reiniciar(e):
    state["vida"] = CONFIG["vida_inicial"]
    state["inventario"] = []
    state["pontos"] = CONFIG["pontos_iniciais"]
    state["armario_ferramentas_pego"] = False
    state["armario_suprimentos_pego"] = False
    state["computador_hackeado"] = False
    state["codigo2_pego"] = False
    state["codigo3_pego"] = False
    trilha = CONFIG.get("trilha_inicial")
    if trilha: window.frameworkAudio.play(trilha)
    mostrar_cena(CONFIG["cena_inicial"])

configurar_identidade()
mostrar_cena(CONFIG["cena_inicial"])
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
