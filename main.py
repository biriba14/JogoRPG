# ============================================================
# PROJETO ECLIPSE
# Aplicação da história ao Projeto Eclipse
# ============================================================

from pyscript import web, when, window

# ============================================================
# CONFIGURAÇÃO GERAL
# ============================================================

CONFIG = {
    "titulo": "PROJETO ECLIPSE",
    "subtitulo": "Uma aventura de terror sci-fi",
    "autor": "Anna Beatriz",
    "icone": "🌑",
    "capa": None,
    "trilha_inicial": "assets/audios/tema_principal.mp3",
    "volume_inicial": 0.5,
    "vida_inicial": 5,
    "pontos_iniciais": 0,
    "cena_inicial": "inicio",
}


# ============================================================
# ESTADO DO JOGO
# ============================================================

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],
}


# ============================================================
# CENAS / NÓS NARRATIVOS (HISTÓRIA DA ANNA BEATRIZ)
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
            '"NÃO CONFIE NAQUELE QUE TEM O SEU ROSTO."'
        ),
        "options": [
            ("Investigar o corredor", "corredor"),
            ("Abrir o armário de emergência", "armario"),
            ("Examinar a porta restrita", "tentar_porta_restrita"),
        ],
    },

    "armario": {
        "title": "Armário de Emergência",
        "image": "assets/imagens/armario.jpg",
        "text": (
            "Você abre o armário. Dentro existem suprimentos que podem salvar sua vida, além de uma fotografia antiga."
        ),
        "options": [
            ("Pegar lanterna e chave", "pegar_ferramentas"),
            ("Pegar kit médico e crachá", "pegar_suprimentos"),
            ("Examinar fotografia", "ver_fotografia"),
            ("Voltar", "inicio"),
        ],
    },

    "armario_ferramentas": {
        "title": "Ferramentas Obtidas",
        "text": "Você pegou uma lanterna pesada e uma chave enferrujada.",
        "options": [("Voltar", "armario")],
    },

    "armario_suprimentos": {
        "title": "Suprimentos Obtidos",
        "text": "Você pegou um kit médico e um crachá parcialmente queimado em nome do Dr. Mateus Almeida.",
        "options": [("Voltar", "armario")],
    },

    "armario_foto": {
        "title": "A Fotografia",
        "text": (
            'Você pega a fotografia. Ela mostra um grupo de cientistas. No centro, está um homem com o seu rosto.\n\n'
            'No verso está escrito: "Equipe Eclipse - Ano 2038. Dr. Mateus Almeida, Diretor do projeto."\n\n'
            'Você sente uma forte dor de cabeça.'
        ),
        "options": [("Voltar", "armario")],
    },

    "corredor": {
        "title": "Corredor Principal",
        "image": "assets/imagens/corredor.jpg",
        "text": (
            "As luzes piscam. Há três caminhos: Sala de Controle, Laboratórios Inferiores e Porta de Segurança.\n\n"
            "Você escuta algo vindo do andar inferior... TOC. TOC. TOC. Como se alguma coisa batesse numa porta."
        ),
        "options": [
            ("Ir para Sala de Controle", "controle"),
            ("Descer para os Laboratórios", "descer_escadas"),
            ("Tentar abrir Porta de Segurança", "tentar_porta_seguranca"),
            ("Voltar ao início", "inicio"),
        ],
    },

    "porta_choque": {
        "title": "Acesso Negado",
        "image": "assets/imagens/porta_trancada.jpg",
        "text": (
            "Você tenta forçar o painel da porta sem a credencial ou chave correta.\n\n"
            "Uma descarga elétrica violenta atravessa seu braço! Você perdeu 1 vida."
        ),
        "options": [("Recuar", "corredor")],
    },

    "queda_escada": {
        "title": "Escuridão Perigosa",
        "text": (
            "Está escuro demais nos laboratórios inferiores. Sem uma lanterna, você tenta descer e escorrega!\n\n"
            "Você rola pelos degraus e se machuca. Você perdeu 1 vida."
        ),
        "options": [("Levantar e voltar", "corredor")],
    },

    "controle": {
        "title": "Sala de Controle",
        "image": "assets/imagens/sala_controle.jpg",
        "text": (
            "Dezenas de monitores desligados. Apenas um exibe: PROJETO ECLIPSE - STATUS CRÍTICO.\n\n"
            "Você encontra arquivos e um terminal central."
        ),
        "options": [
            ("Ler Relatório e Protocolo", "ler_arquivos"),
            ("Ouvir Arquivo Pessoal", "ouvir_gravacao"),
            ("Ativar Computador Central", "ativar_pc"),
            ("Voltar ao corredor", "corredor"),
        ],
    },

    "ler_arquivos": {
        "title": "Arquivos do Projeto",
        "text": (
            "RELATÓRIO: O Projeto Eclipse estuda transferência de consciência. O problema surgiu quando as cópias começaram a acreditar que eram as originais.\n\n"
            "PROTOCOLO DE EVACUAÇÃO: Para fugir, encontre as 3 partes do código de segurança (Setor Médico, Laboratório e Arquivo) e insira no Núcleo."
        ),
        "options": [("Voltar", "controle")],
    },

    "ouvir_gravacao": {
        "title": "Gravação Pessoal",
        "text": (
            '"Se está ouvindo isso, eu falhei. O Eclipse cria cópias. Se meu experimento funcionar, uma cópia acordará sem memórias acreditando ser o Mateus. Mas o verdadeiro Mateus estará morto."\n\n'
            "Você olha para as suas mãos em choque."
        ),
        "options": [("Voltar", "controle")],
    },

    "ativar_pc": {
        "title": "Computador Central",
        "text": (
            "CÓDIGO ADMINISTRADOR NECESSÁRIO.\n\n"
            "Instintivamente você digita 071984. Acesso concedido!\n"
            "Você localizou a PRIMEIRA PARTE do código de evacuação!"
        ),
        "options": [("Voltar", "controle")],
    },

    "subsolo": {
        "title": "Laboratórios Inferiores",
        "image": "assets/imagens/subsolo.jpg",
        "text": (
            "O ar é gélido. As paredes estão cobertas de arranhões feitos por unhas.\n\n"
            "Sua lanterna ilumina uma placa: 'SETOR MÉDICO - SALA 17' e outra 'LABORATÓRIO PRINCIPAL'."
        ),
        "options": [
            ("Entrar na Sala 17", "sala17"),
            ("Entrar no Laboratório Principal", "laboratorio"),
            ("Seguir para o Arquivo", "arquivo"),
            ("Subir", "corredor"),
        ],
    },

    "sala17": {
        "title": "Sala 17",
        "text": (
            "Há uma maca e um monitor ligado: PACIENTE 07. MEMÓRIA: INCOMPLETA. IDENTIDADE: MATEUS ALMEIDA.\n\n"
            "Debaixo da maca, você encontra um cartão com a SEGUNDA PARTE do Código de Evacuação!"
        ),
        "options": [
            ("Pegar código e sair", "pegar_codigo2"),
        ],
    },

    "laboratorio": {
        "title": "Laboratório Principal",
        "image": "assets/imagens/laboratorio_principal.jpg",
        "text": (
            "Uma máquina gigantesca exibe: 'ENERGIA 23%'.\n"
            "Ao tocar nela, centenas de rostos iguais ao seu aparecem na tela. O laboratório produziu várias cópias de você.\n\n"
            "Vasculhando o local, você acha um mapa que revela uma passagem secreta."
        ),
        "options": [
            ("Ir para Passagem Secreta", "arquivo"),
            ("Ir para o Gerador", "gerador"),
            ("Sair", "subsolo"),
        ],
    },

    "gerador": {
        "title": "Sala do Gerador",
        "text": "O enorme motor está desligado. Uma alavanca indica: REINICIALIZAÇÃO MANUAL.",
        "options": [
            ("Ligar o gerador", "ligar_gerador"),
            ("Voltar", "laboratorio"),
        ],
    },

    "alarme": {
        "title": "Alarme Disparado!",
        "image": "assets/imagens/alarme.jpg",
        "audio": "assets/audios/alarme.mp3",
        "text": (
            "As luzes acendem, mas as portas bloqueiam! Uma voz anuncia: CONTENÇÃO DE PACIENTE 07.\n\n"
            "Passos rápidos ecoam. Uma criatura com o SEU ROSTO aparece no corredor!"
        ),
        "options": [
            ("Correr para o Túnel de Manutenção", "tunel"),
            ("Enfrentar a criatura", "lutar_criatura"),
        ],
    },

    "dano_criatura": {
        "title": "Luta Brutal",
        "text": (
            "Você tenta lutar com as próprias mãos contra a cópia monstruosa.\n"
            "Ela é mais forte. Você é arremessado contra a parede e perde 2 vidas, mas consegue fugir rastejando para o túnel."
        ),
        "options": [("Rastejar para o túnel", "tunel")],
    },

    "arquivo": {
        "title": "Arquivo Subterrâneo",
        "text": (
            "Centenas de caixas. Várias possuem o nome 'Mateus Almeida'.\n\n"
            "Você revira algumas caixas e encontra a TERCEIRA PARTE do Código!\n\n"
            "No fundo da sala, há uma porta escrita: MEMÓRIAS ORIGINAIS."
        ),
        "options": [
            ("Entrar em Memórias Originais", "memorias"),
            ("Pegar código e sair", "pegar_codigo3"),
        ],
    },

    "memorias": {
        "title": "Memórias Originais",
        "text": (
            "Dezenas de cápsulas. Uma delas diz: MATEUS ALMEIDA - ORIGINAL - STATUS: VIVO.\n\n"
            "O homem dentro da cápsula abre os olhos. Ele é o verdadeiro. Ele diz: 'Eu sou Mateus. Você é só uma cópia minha.'"
        ),
        "options": [
            ("Ajudar o verdadeiro Mateus", "fuga_dupla"),
            ("Abandoná-lo", "fim_egoista"),
            ("Ir para o Núcleo destruir tudo", "nucleo"),
        ],
    },

    "tunel": {
        "title": "Túnel de Manutenção",
        "text": "É apertado e escuro. Você encontra três portas.",
        "options": [
            ("Porta Azul (Superfície)", "saida_falsa"),
            ("Porta Vermelha (Núcleo)", "nucleo"),
            ("Porta Preta (Secreta)", "sala_secreta"),
        ],
    },

    "sala_secreta": {
        "title": "Sala Secreta",
        "text": (
            "Você encontra uma cadeira conectada a cabos. Um espelho reflete seu rosto. O reflexo sorri (você não).\n"
            "'Deseja ter todas as suas memórias de volta?'"
        ),
        "options": [
            ("Aceitar a conexão", "final_memorias"),
            ("Quebrar o espelho e fugir", "saida_falsa"),
        ],
    },

    "nucleo": {
        "title": "Núcleo Eclipse",
        "image": "assets/imagens/nucleo.jpg",
        "text": (
            "Um enorme reator pulsa. O monitor exibe: 847 CONSCIÊNCIAS CONECTADAS.\n"
            "O sistema exige as 3 partes do código de evacuação para desativação segura."
        ),
        "options": [
            ("Inserir o código de evacuação", "tentar_desligar"),
            ("Desligar puxando os cabos à força", "nucleo_perigoso"),
            ("Libertar todas as consciências", "fim_libertador"),
        ],
    },

    "nucleo_perigoso": {
        "title": "Sobrecarga!",
        "text": (
            "Você puxa os cabos ignorando o sistema. O núcleo sobrecarrega!\n"
            "O laboratório treme violentamente e você é atingido por destroços. Você perde 2 vidas."
        ),
        "options": [("Tentar fugir da explosão", "tunel")],
    },

    # ========================== FINAIS ==========================
    "fuga_dupla": {
        "title": "FINAL: A VERDADEIRA FUGA",
        "image": "assets/imagens/final_bom.jpg",
        "text": (
            "Você ajuda o verdadeiro Mateus a fugir. O laboratório explode atrás de vocês.\n"
            "Sua origem como cópia não determina quem você é. Suas escolhas sim.\n\n"
            "FINAL BOM."
        ),
        "options": [],
    },
    
    "fim_egoista": {
        "title": "FINAL: O SOBREVIVENTE",
        "text": (
            "Você foge sozinho e reconstrói sua vida. Meses depois, alguém bate na sua porta. É o verdadeiro Mateus, e ele não está feliz.\n\n"
            "FINAL RUIM."
        ),
        "options": [],
    },

    "saida_falsa": {
        "title": "FINAL: O EXÉRCITO DE CÓPIAS",
        "text": (
            "Você sai na floresta. Acha que conseguiu, mas dezenas de pessoas estão lá fora. Todas com o seu rosto.\n"
            "'Bem-vindo de volta, Paciente 07'. O laboratório não acabou... Ele apenas começou.\n\n"
            "FINAL RUIM."
        ),
        "options": [],
    },

    "fim_sacrificio": {
        "title": "FINAL: O SACRIFÍCIO",
        "text": (
            "O código funciona. As 847 consciências são apagadas, incluindo a sua. Você morre, mas liberta o mundo dessa maldição.\n\n"
            "FINAL HERÓICO."
        ),
        "options": [],
    },

    "final_memorias": {
        "title": "FINAL SECRETO: TODAS AS MEMÓRIAS",
        "text": (
            "Você absorve as memórias de todas as cópias mortas antes de você. Você lembra de morrer 12 vezes. Você aceita seu destino e desliga a máquina por dentro.\n\n"
            "FINAL SECRETO."
        ),
        "options": [],
    },

    "fim_libertador": {
        "title": "FINAL: O LIBERTADOR",
        "text": (
            "Você sobrecarrega o sistema enviando os dados para a rede. Centenas de cópias acordam pelo mundo.\n"
            "Você não sabe se é humano, mas sabe que está vivo.\n\n"
            "FINAL BOM ALTERNATIVO."
        ),
        "options": [],
    },

    "fim_ruim": {
        "title": "GAME OVER",
        "image": "assets/imagens/game_over.jpg",
        "text": "Seu corpo não resiste aos ferimentos. A escuridão toma conta. O Projeto Eclipse fará uma nova cópia amanhã.",
        "options": [],
    },
}


# ============================================================
# ACESSO AO HTML
# ============================================================

def el(id_elemento):
    return web.page[id_elemento]


# ============================================================
# IDENTIDADE VISUAL
# ============================================================

def configurar_identidade():
    titulo = CONFIG["titulo"]
    autor = CONFIG["autor"]
    subtitulo = CONFIG["subtitulo"]

    window.document.title = titulo
    el("titulo-jogo").innerText = titulo
    el("autor-jogo").innerText = f"Autor: {autor}"
    el("titulo-abertura").innerText = titulo
    el("subtitulo-abertura").innerText = subtitulo
    el("autor-abertura").innerText = f"Criado por {autor}"
    el("icone-abertura").innerText = CONFIG["icone"]

    capa = CONFIG.get("capa")
    if capa:
        el("capa-jogo").src = capa
        el("capa-jogo").style.display = "block"
        el("icone-abertura").style.display = "none"
    else:
        el("capa-jogo").style.display = "none"
        el("icone-abertura").style.display = "block"

    audio = el("audio-fundo")
    trilha = CONFIG.get("trilha_inicial")
    audio.dataset.inicial = trilha if trilha else ""
    audio.dataset.volume = str(CONFIG.get("volume_inicial", 0.5))


# ============================================================
# STATUS E INVENTÁRIO
# ============================================================

def atualizar_status():
    vida = state["vida"]
    if vida > 0:
        el("vida").innerText = " ".join(["❤️"] * vida)
        el("vida").classList.remove("danger")
    else:
        el("vida").innerText = "💀"
        el("vida").classList.add("danger")

    if state["inventario"]:
        el("inventario").innerText = ", ".join(state["inventario"])
    else:
        el("inventario").innerText = "Vazio"

    el("pontos").innerText = str(state["pontos"])


def perder_vida(quantidade=1):
    """Retira vida e retorna True se o jogador morreu."""
    state["vida"] -= quantidade
    if state["vida"] < 0:
        state["vida"] = 0
    atualizar_status()
    return state["vida"] <= 0


def adicionar_item(item, pontos=0):
    if item not in state["inventario"]:
        state["inventario"].append(item)
        state["pontos"] += pontos
    atualizar_status()


def possui_item(item):
    return item in state["inventario"]


def ganhar_pontos(quantidade):
    state["pontos"] += quantidade
    atualizar_status()


# ============================================================
# MULTIMÍDIA
# ============================================================

def mostrar_imagem(caminho):
    window.frameworkVideo.stop()
    if not caminho:
        window.frameworkImage.hide()
        return
    window.frameworkImage.show(caminho)

def mostrar_video(caminho, autoplay=False):
    if not caminho:
        window.frameworkVideo.stop()
        return
    window.frameworkVideo.play(caminho, autoplay)

def trocar_audio(caminho):
    if caminho:
        window.frameworkAudio.play(
            caminho,
            CONFIG.get("volume_inicial", 0.5),
            True,
        )

def parar_audio():
    window.frameworkAudio.stop()


# ============================================================
# BOTÕES E CENAS
# ============================================================

def configurar_botao(numero, texto="", ativo=False):
    botao = el(f"opcao{numero}")
    botao.innerText = texto
    botao.disabled = not ativo
    botao.style.display = "block" if ativo else "none"

def opcoes_da_cena(nome, cena):
    return list(cena.get("options", []))

def atualizar_botoes(opcoes):
    for i in range(1, 5):
        if i <= len(opcoes):
            configurar_botao(i, opcoes[i - 1][0], True)
        else:
            configurar_botao(i, "", False)

def mostrar_cena(nome):
    if nome not in SCENES:
        el("titulo-cena").innerText = "Erro de cena"
        el("texto-cena").innerText = f"A cena '{nome}' não existe em SCENES."
        atualizar_botoes([])
        return

    state["cena"] = nome
    cena = SCENES[nome]

    el("titulo-cena").innerText = cena.get("title", nome)
    el("texto-cena").innerText = cena.get("text", "")

    video = cena.get("video")
    if video:
        mostrar_video(video, cena.get("video_autoplay", False))
    else:
        mostrar_imagem(cena.get("image"))

    if "audio" in cena:
        if cena["audio"]:
            trocar_audio(cena["audio"])
        else:
            parar_audio()

    if cena.get("stop_audio"):
        parar_audio()

    atualizar_botoes(opcoes_da_cena(nome, cena))
    atualizar_status()


# ============================================================
# EXECUTAR AÇÃO (LÓGICA DA ANNA BEATRIZ)
# ============================================================

def executar_acao(acao):
    if acao == "pegar_ferramentas":
        adicionar_item("lanterna")
        adicionar_item("chave")
        mostrar_cena("armario_ferramentas")

    elif acao == "pegar_suprimentos":
        adicionar_item("kit médico")
        adicionar_item("crachá")
        mostrar_cena("armario_suprimentos")

    elif acao == "ver_fotografia":
        mostrar_cena("armario_foto")

    elif acao == "tentar_porta_restrita":
        if possui_item("crachá"):
            mostrar_cena("laboratorio")
        else:
            morreu = perder_vida(1)
            if morreu:
                mostrar_cena("fim_ruim")
            else:
                mostrar_cena("porta_choque")

    elif acao == "tentar_porta_seguranca":
        if possui_item("chave"):
            mostrar_cena("arquivo")
        else:
            morreu = perder_vida(1)
            if morreu:
                mostrar_cena("fim_ruim")
            else:
                mostrar_cena("porta_choque")

    elif acao == "descer_escadas":
        if possui_item("lanterna"):
            mostrar_cena("subsolo")
        else:
            morreu = perder_vida(1)
            if morreu:
                mostrar_cena("fim_ruim")
            else:
                mostrar_cena("queda_escada")

    elif acao == "ativar_pc":
        adicionar_item("codigo1")
        mostrar_cena("ativar_pc")

    elif acao == "pegar_codigo2":
        adicionar_item("codigo2")
        mostrar_cena("subsolo")

    elif acao == "pegar_codigo3":
        adicionar_item("codigo3")
        mostrar_cena("subsolo")

    elif acao == "ligar_gerador":
        mostrar_cena("alarme")

    elif acao == "lutar_criatura":
        morreu = perder_vida(2)
        if morreu:
            mostrar_cena("fim_ruim")
        else:
            mostrar_cena("dano_criatura")

    elif acao == "tentar_desligar":
        if possui_item("codigo1") and possui_item("codigo2") and possui_item("codigo3"):
            ganhar_pontos(100)
            mostrar_cena("fim_sacrificio")
        else:
            mostrar_cena("nucleo")

    elif acao in SCENES:
        mostrar_cena(acao)

    else:
        el("texto-cena").innerText = f"A ação '{acao}' não foi cadastrada."


# ============================================================
# EVENTOS DE CLIQUES E REINÍCIO
# ============================================================

def escolher_opcao(numero):
    nome = state["cena"]
    cena = SCENES[nome]
    opcoes = opcoes_da_cena(nome, cena)
    indice = numero - 1
    if indice < len(opcoes):
        executar_acao(opcoes[indice][1])

@when("click", "#opcao1")
def clicar_opcao1(event):
    escolher_opcao(1)

@when("click", "#opcao2")
def clicar_opcao2(event):
    escolher_opcao(2)

@when("click", "#opcao3")
def clicar_opcao3(event):
    escolher_opcao(3)

@when("click", "#opcao4")
def clicar_opcao4(event):
    escolher_opcao(4)

@when("click", "#reiniciar")
def reiniciar(event):
    state["vida"] = CONFIG["vida_inicial"]
    state["inventario"] = []
    state["pontos"] = CONFIG["pontos_iniciais"]
    state["cena"] = CONFIG["cena_inicial"]

    trilha = CONFIG.get("trilha_inicial")
    if trilha:
        trocar_audio(trilha)

    mostrar_cena(CONFIG["cena_inicial"])


# ============================================================
# INICIALIZAÇÃO
# ============================================================

configurar_identidade()
mostrar_cena(CONFIG["cena_inicial"])
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
