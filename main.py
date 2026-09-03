# ============================================================
# PROJETO ECLIPSE - ENGINE NARRATIVA DINÂMICA
# ============================================================

from pyscript import web, when, window

CONFIG = {
    "titulo": "PROJETO ECLIPSE",
    "subtitulo": "Uma aventura de terror sci-fi",
    "autor": "Anna Beatriz",
    "icone": "🌑",
    "capa": "assets/imagens/capa.jfif",
    "trilha_inicial": "assets/audios/tema_principal.mpeg",
    "volume_inicial": 0.5,
    "vida_maxima": 5,
    "vida_inicial": 5,
    "pontos_iniciais": 0,
    "cena_inicial": "inicio",
}

state = {
    "vida": CONFIG["vida_inicial"],
    "inventario": [],
    "pontos": CONFIG["pontos_iniciais"],
    "cena": CONFIG["cena_inicial"],
    # Coleta de itens individuais do armário
    "lanterna_pega": False,
    "chave_pega": False,
    "kit_medico_pego": False,
    "cracha_pego": False,
    # Portas destrancadas
    "porta_restrita_aberta": False,
    "porta_seguranca_aberta": False,
    # Eventos e itens únicos da trama
    "computador_hackeado": False,
    "codigo2_pego": False,
    "codigo3_pego": False,
    "gerador_ligado": False,
    "escada_iluminada": False,
}

# ============================================================
# MAPA DE CENAS NARRATIVAS
# ============================================================

SCENES = {
    "inicio": {
        "title": "O Despertar",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você acorda deitado no chão frio de um laboratório. Sua cabeça dói. Uma luz vermelha pisca no teto.\n\n"
            "Você não sabe onde está e não consegue lembrar seu próprio nome. Há sangue nas suas mãos.\n\n"
            'Um som metálico ecoa: "PROTOCOLO DE CONTENÇÃO ATIVO. TEMPO ESTIMADO PARA COLAPSO: 47 MINUTOS."\n\n'
            'Uma porta blindada à sua frente possui uma mensagem escrita com tinta vermelha:\n'
            '"NÃO CONFIE NAQUELE QUE TENHA O SEU ROSTO."'
        ),
    },

    "armario": {
        "title": "Armário de Emergência",
        "image": "assets/imagens/capa.jfif",
        "text": "O armário metálico range ao abrir. Prateleiras oxidadas guardam resquícios de equipamentos abandonados da equipe científica.",
    },

    "armario_foto": {
        "title": "A Fotografia Antiga",
        "image": "assets/imagens/capa.jfif",
        "text": (
            'Você observa a foto empoeirada. Um grupo de pesquisadores sorri. No centro, o homem é idêntico a você.\n\n'
            'No verso: "Equipe Eclipse - Ano 2038. Dr. Mateus Almeida."\n'
            'Sua cabeça lateja com uma lembrança que não parece sua.'
        ),
        "options": [("Voltar ao armário", "armario")],
    },

    "corredor": {
        "title": "Corredor Principal",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "As lâmpadas de emergência estalam no teto úmido.\n"
            "À sua esquerda está a Sala de Controle, à frente uma escadaria que desce para o breu total dos Laboratórios Inferiores, e ao fundo a pesada Porta de Segurança reforçada."
        ),
    },

    "porta_choque": {
        "title": "Descarga Elétrica!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você tenta forçar o painel com as mãos desprotegidas!\n\n"
            "Uma descarga azulada explode sobre o seu braço, jogando você para trás no chão. Você perdeu 1 vida."
        ),
        "options": [("Recuar atordoado", "voltar_de_choque")],
    },

    "queda_escada": {
        "title": "Queda no Escuro",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você tenta descer a escadaria tateando as paredes frias no breu absoluto.\n\n"
            "O chão está escorregadio de óleo sintético; seu pé falseia e você rola vários degraus abaixo batendo o ombro com força. Você perdeu 1 vida."
        ),
        "options": [("Levantar-se com dor", "corredor")],
    },

    "controle": {
        "title": "Sala de Controle",
        "image": "assets/imagens/capa.jfif",
        "text": "Fileiras de monitores apagados cercam a sala fria. Apenas um terminal central permanece energizado, emitindo um zumbido contínuo e estático.",
    },

    "ler_arquivos": {
        "title": "Arquivos Confidenciais",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "RELATÓRIO DE TRANSFERÊNCIA MENTAL:\n\n"
            "- A replicação de consciência biológica produz cópias idênticas e funcionais.\n"
            "- Se uma réplica descobrir a verdade sobre sua origem, entra em colapso psicótico ou rebelião violenta.\n"
            "- PROTOCOLO FINAL: A única forma de impedir a detonação é reunir os 3 Códigos de Segurança no Núcleo."
        ),
        "options": [("Fechar registros", "controle")],
    },

    "ouvir_gravacao": {
        "title": "Registro de Áudio #07",
        "image": "assets/imagens/capa.jfif",
        "text": (
            '"Se esta gravação ainda existe... o protocolo falhou. Eu não pude morrer com minha doença, então criei minha própria continuação.\n'
            'Mas eles acordaram sem alma. Se as cópias alcançarem os túneis de superfície, o mundo lá fora não saberá a diferença..."'
        ),
        "options": [("Desligar reprodução", "controle")],
    },

    "subsolo": {
        "title": "Laboratórios Inferiores",
        "image": "assets/imagens/capa.jfif",
        "text": "O ar aqui embaixo cheira a ozônio e queimado. Há arranhões profundos nas paredes de liga metálica e marcas de sapatos manchados.",
    },

    "sala17": {
        "title": "Sala 17 - Setor de Isolamento",
        "image": "assets/imagens/capa.jfif",
        "text": "Uma maca cirúrgica destruída domina o centro. No monitor de sinais vitais pisca continuamente: [PACIENTE 07 - PROTÓTIPO ATIVO].",
    },

    "laboratorio": {
        "title": "Laboratório Principal",
        "image": "assets/imagens/capa.jfif",
        "text": "Cilindros de clonagem preenchidos de líquido turvo e vidro quebrado. Rostos exatamente iguais ao seu repousam sem vida nas câmaras auxiliares.",
    },

    "gerador": {
        "title": "Sala do Gerador Auxiliar",
        "image": "assets/imagens/capa.jfif",
        "text": "Turbinas paradas sob vapor espesso. O painel de emergência aguarda para ser acionado manualmente para restabelecer energia aos setores críticos.",
    },

    "alarme": {
        "title": "Alarme Geral Disparado!",
        "image": "assets/imagens/capa.jfif",
        "audio": "assets/audios/alarme.mp3",
        "text": (
            "Sirenes ensurdecedoras soam e luzes giratórias banham a câmara em sangue luminoso!\n\n"
            "Uma porta de contenção cede... Uma figura deformada com o seu próprio rosto avança em sua direção empunhando uma barra de aço!"
        ),
    },

    "combate_vitoria": {
        "title": "Fuga Rápida!",
        "image": "assets/imagens/capa.jfif",
        "text": "Você acerta a criatura em cheio na têmpora com a lanterna de metal pesado! O clone cambaleia atordoado, dando tempo para você mergulhar no duto de ventilação sem ferimentos.",
        "options": [("Avançar pelo túnel", "tunel")],
    },

    "dano_criatura": {
        "title": "Confronto Desesperado",
        "image": "assets/imagens/capa.jfif",
        "text": "Você tenta conter seu clone com os braços livres, mas a força dele é desumana! Você é lançado violentamente contra as ferragens e sofre ferimentos graves antes de conseguir escapar para o duto (-2 Vidas).",
        "options": [("Arrastar-se pelo túnel", "tunel")],
    },

    "arquivo": {
        "title": "Arquivo Morto",
        "image": "assets/imagens/capa.jfif",
        "text": "Gaveteiros metálicos com fichas de todos os voluntários e réplicas produzidas pelo Projeto Eclipse ao longo de duas décadas.",
    },

    "memorias": {
        "title": "Câmara de Memórias",
        "image": "assets/imagens/capa.jfif",
        "text": "Em uma cápsula criogênica no centro da sala, repousa o verdadeiro Dr. Mateus Almeida, debilitado. Os olhos dele se abrem vagarosamente ao notar sua presença: 'Então você despertou... minha última réplica.'",
        "options": [
            ("Libertar e ajudar o verdadeiro criador", "fuga_dupla"),
            ("Desconectar a cápsula e fugir sozinho", "fim_egoista"),
            ("Ignorar a cápsula e correr para o Núcleo", "nucleo"),
        ],
    },

    "tunel": {
        "title": "Túnel de Ventilação",
        "image": "assets/imagens/capa.jfif",
        "text": "Um duto estreito e escuro. Mais à frente, o fluxo de ar se divide em três ramificações industriais com marcações na tubulação.",
        "options": [
            ("Seguir o duto azul (Exaustão para a Superfície)", "saida_falsa"),
            ("Descer pelo duto vermelho (Acesso Direto ao Núcleo)", "nucleo"),
            ("Rastrear o duto preto (Setor Não Mapeado)", "sala_secreta"),
        ],
    },

    "sala_secreta": {
        "title": "Laboratório Clandestino",
        "image": "assets/imagens/capa.jfif",
        "text": "Uma cadeira neural com cabos ópticos voltada para um espelho de observação. Seu reflexo não pisca quando você pisca, estendendo a mão pelo vidro: 'Deseja ter todas as memórias reais que lhe roubaram?'",
        "options": [
            ("Conectar-se à cadeira neural", "final_memorias"),
            ("Quebrar o painel e buscar a saída da floresta", "saida_falsa"),
        ],
    },

    "nucleo": {
        "title": "Núcleo do Reator",
        "image": "assets/imagens/capa.jfif",
        "text": "O coração energético da instalação ruge com pulsos de radiação pura. O painel central exige o alinhamento das 3 partes do código mestre para desligamento seguro.",
    },

    "nucleo_incompleto": {
        "title": "Acesso Negado!",
        "image": "assets/imagens/capa.jfif",
        "text": "O console emite um aviso estridente: CÓDIGO INCOMPLETO. Você não reuniu todas as 3 partes necessárias da chave mestre para desativar o reator com segurança.",
        "options": [("Voltar e explorar outras rotas", "tunel")],
    },

    "nucleo_perigoso": {
        "title": "Fusão Nuclear Incontrolável!",
        "image": "assets/imagens/capa.jfif",
        "text": "Você arranca os cabos do console sem autorização! Uma onda de calor abrasador irrompe do reator, queimando suas mãos e estilhaçando as paredes ao redor (-2 Vidas).",
        "options": [("Escapar ferido pelos escombros", "tunel")],
    },

    # ================= FINAIS =================
    "fuga_dupla": {
        "title": "FINAL: A VERDADEIRA FUGA",
        "image": "assets/imagens/capa.jfif",
        "text": "Você ampara o enfraquecido criador e ambos usam a cápsula de emergência antes do colapso da instalação. Você pode ser uma cópia biológica, mas a humanidade demonstrada nesta escolha foi inteiramente sua.\n\n[FINAL BOM]",
        "options": [],
    },

    "fim_egoista": {
        "title": "FINAL: O SOBREVIVENTE",
        "image": "assets/imagens/capa.jfif",
        "text": "Você escapa sozinho pelas matas circundantes, deixando o complexo queimar. Seis meses depois, vivendo com uma identidade comprada, você ouve passos na sua varanda: alguém com o seu mesmo rosto veio cobrar a conta.\n\n[FINAL RUIM]",
        "options": [],
    },

    "saida_falsa": {
        "title": "FINAL: EXÉRCITO DE RÉPLICAS",
        "image": "assets/imagens/capa.jfif",
        "text": "Você emerge na clareira nos arredores do laboratório sentindo a brisa da noite. Mas ao olhar para a floresta, dezenas de homens iguaizinhos a você encaram sua chegada em silêncio absoluto. Você nunca foi o único a escapar.\n\n[FINAL RUIM]",
        "options": [],
    },

    "fim_sacrificio": {
        "title": "FINAL: O SACRIFÍCIO HERÓICO",
        "image": "assets/imagens/capa.jfif",
        "text": "Com os 3 fragmentos alinhados, a sequência de purga final é acionada. O gerador congela as câmaras de clonagem e dissolve toda a base de dados neurais. Conforme sua própria mente sintética se apaga, você sabe que o mundo exterior foi protegido.\n\n[FINAL HERÓICO]",
        "options": [],
    },

    "final_memorias": {
        "title": "FINAL SECRETO: CONSCIÊNCIA TOTAL",
        "image": "assets/imagens/capa.jfif",
        "text": "Ao ligar os eletrodos, a consciência de cada réplica que pereceu antes de você se funde em sua mente. Com a inteligência combinada de dezenas de vidas, você assume o controle dos sistemas centrais e remodela o Projeto Eclipse por dentro.\n\n[FINAL SECRETO]",
        "options": [],
    },

    "fim_libertador": {
        "title": "FINAL: O LIBERTADOR",
        "image": "assets/imagens/capa.jfif",
        "text": "Você conecta o reator à antena de alta potência do complexo e transmite os arquivos do projeto e as consciências gravadas para servidores espalhados por todo o planeta. A verdade não pode mais ser contida.\n\n[FINAL BOM ALTERNATIVO]",
        "options": [],
    },

    "fim_ruim": {
        "title": "GAME OVER",
        "image": "assets/imagens/capa.jfif",
        "text": "Suas forças se esvaem no chão de concreto gelado. Seus batimentos cessam enquanto o alarme continua a contar os minutos restantes. Amanhã, uma nova câmara será despertada.",
        "options": [],
    },
}

# ============================================================
# INTERFACE E FUNÇÕES AUXILIARES
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
    if state["vida"] < 0:
        state["vida"] = 0
    atualizar_status()
    return state["vida"] <= 0

def adicionar_item(item, pts=0):
    if item not in state["inventario"]:
        state["inventario"].append(item)
        state["pontos"] += pts
    atualizar_status()

def remover_item(item):
    if item in state["inventario"]:
        state["inventario"].remove(item)
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

# ============================================================
# LÓGICA DINÂMICA DE OPÇÕES
# ============================================================

def opcoes_da_cena(nome, cena):
    opcoes = []

    # Opção contextual de uso de item: Curar vida com Kit Médico
    pode_curar = possui_item("Kit médico") and state["vida"] < CONFIG["vida_maxima"] and not nome.startswith("fim") and nome != "fim_ruim"

    if nome == "inicio":
        opcoes.append(("Investigar o corredor principal", "corredor"))
        opcoes.append(("Vasculhar o armário de emergência", "armario"))
        if state["porta_restrita_aberta"]:
            opcoes.append(("Entrar no Laboratório Principal (Aberta)", "laboratorio"))
        else:
            opcoes.append(("Tentar abrir a porta com mensagem", "tentar_porta_restrita"))

    elif nome == "armario":
        if not state["lanterna_pega"]:
            opcoes.append(("Pegar a lanterna pesada", "pegar_lanterna"))
        if not state["chave_pega"]:
            opcoes.append(("Pegar a chave enferrujada", "pegar_chave"))
        if not state["kit_medico_pego"]:
            opcoes.append(("Pegar o kit médico", "pegar_kit"))
        if not state["cracha_pego"]:
            opcoes.append(("Pegar o crachá do Dr. Mateus", "pegar_cracha"))

        if len(opcoes) < 3:
            opcoes.append(("Examinar a fotografia antiga", "armario_foto"))
        opcoes.append(("Voltar à sala inicial", "inicio"))

    elif nome == "corredor":
        opcoes.append(("Ir para a Sala de Controle", "controle"))
        opcoes.append(("Descer para os Laboratórios Inferiores", "descer_escadas"))
        if state["porta_seguranca_aberta"]:
            opcoes.append(("Entrar no Arquivo Morto (Destrancado)", "arquivo"))
        else:
            opcoes.append(("Tentar abrir a Porta de Segurança", "tentar_porta_seguranca"))
        opcoes.append(("Voltar à sala inicial", "inicio"))

    elif nome == "controle":
        opcoes.append(("Ler os relatórios do projeto", "ler_arquivos"))
        opcoes.append(("Ouvir gravação corrompida", "ouvir_gravacao"))
        if not state["computador_hackeado"]:
            opcoes.append(("Hackear o terminal central", "ativar_pc"))
        opcoes.append(("Retornar ao corredor", "corredor"))

    elif nome == "subsolo":
        if not state["codigo2_pego"]:
            opcoes.append(("Vasculhar Sala 17 (Setor Médico)", "sala17"))
        opcoes.append(("Avançar para o Laboratório Principal", "laboratorio"))
        opcoes.append(("Subir de volta para o corredor", "corredor"))

    elif nome == "sala17":
        if not state["codigo2_pego"]:
            opcoes.append(("Coletar o Código de Acesso #2", "pegar_codigo2"))
        opcoes.append(("Retornar ao corredor do subsolo", "subsolo"))

    elif nome == "laboratorio":
        if not state["gerador_ligado"]:
            opcoes.append(("Ir para a Sala do Gerador Auxiliar", "gerador"))
        opcoes.append(("Entrar no duto de ventilação", "tunel"))
        opcoes.append(("Ir para o Arquivo Morto", "arquivo"))
        opcoes.append(("Voltar para o subsolo", "subsolo"))

    elif nome == "gerador":
        if not state["gerador_ligado"]:
            opcoes.append(("Puxar a alavanca de ignição", "ligar_gerador"))
        opcoes.append(("Recuar para o Laboratório Principal", "laboratorio"))

    elif nome == "alarme":
        if possui_item("Lanterna pesada"):
            opcoes.append(("Golpear clone com a lanterna", "combater_lanterna"))
        opcoes.append(("Enfrentar o clone de mãos limpas", "lutar_criatura"))
        opcoes.append(("Correr em disparada para a ventilação", "dano_criatura"))

    elif nome == "arquivo":
        if not state["codigo3_pego"]:
            opcoes.append(("Recolher Código de Acesso #3", "pegar_codigo3"))
        opcoes.append(("Acessar Câmara de Memórias", "memorias"))
        opcoes.append(("Voltar ao Laboratório Principal", "laboratorio"))

    elif nome == "nucleo":
        opcoes.append(("Digitar os 3 Códigos de Segurança", "tentar_desligar"))
        opcoes.append(("Desconectar os cabos centrais à força", "nucleo_perigoso"))
        opcoes.append(("Transmitir os dados para a rede global", "fim_libertador"))

    elif "options" in cena:
        opcoes = list(cena["options"])

    # Se estiver ferido e com o kit médico, encaixa o uso do item prioritariamente
    if pode_curar and len(opcoes) >= 4:
        opcoes[3] = ("Usar Kit Médico (+2 Vidas)", "usar_kit_medico")
    elif pode_curar and len(opcoes) < 4:
        opcoes.append(("Usar Kit Médico (+2 Vidas)", "usar_kit_medico"))

    return opcoes[:4]

# ============================================================
# TRANSIÇÃO E EXECUÇÃO DE AÇÕES
# ============================================================

def mostrar_cena(nome):
    if nome not in SCENES:
        return
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
        if cena["audio"]:
            window.frameworkAudio.play(cena["audio"])
        else:
            window.frameworkAudio.stop()
    elif cena.get("stop_audio"):
        window.frameworkAudio.stop()

    atualizar_botoes(opcoes_da_cena(nome, cena))
    atualizar_status()

def executar_acao(acao):
    if acao == "usar_kit_medico":
        if possui_item("Kit médico"):
            remover_item("Kit médico")
            state["vida"] = min(CONFIG["vida_maxima"], state["vida"] + 2)
            state["pontos"] += 15
            atualizar_status()
            mostrar_cena(state["cena"])
        return

    if acao == "pegar_lanterna":
        state["lanterna_pega"] = True
        adicionar_item("Lanterna pesada", 10)
        mostrar_cena("armario")

    elif acao == "pegar_chave":
        state["chave_pega"] = True
        adicionar_item("Chave enferrujada", 10)
        mostrar_cena("armario")

    elif acao == "pegar_kit":
        state["kit_medico_pego"] = True
        adicionar_item("Kit médico", 10)
        mostrar_cena("armario")

    elif acao == "pegar_cracha":
        state["cracha_pego"] = True
        adicionar_item("Crachá do Dr. Mateus", 15)
        mostrar_cena("armario")

    elif acao == "tentar_porta_restrita":
        if possui_item("Crachá do Dr. Mateus"):
            state["porta_restrita_aberta"] = True
            state["pontos"] += 20
            mostrar_cena("laboratorio")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque")

    elif acao == "voltar_de_choque":
        if state["cena"] == "porta_choque":
            mostrar_cena("corredor")

    elif acao == "tentar_porta_seguranca":
        if possui_item("Chave enferrujada"):
            state["porta_seguranca_aberta"] = True
            state["pontos"] += 20
            mostrar_cena("arquivo")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque")

    elif acao == "descer_escadas":
        if state["escada_iluminada"] or possui_item("Lanterna pesada"):
            state["escada_iluminada"] = True
            mostrar_cena("subsolo")
        else:
            morreu = perder_vida(1)
            mostrar_cena("fim_ruim") if morreu else mostrar_cena("queda_escada")

    elif acao == "ativar_pc":
        if not state["computador_hackeado"]:
            state["computador_hackeado"] = True
            adicionar_item("Código de Acesso #1", 20)
            mostrar_cena("controle")

    elif acao == "pegar_codigo2":
        if not state["codigo2_pego"]:
            state["codigo2_pego"] = True
            adicionar_item("Código de Acesso #2", 20)
            mostrar_cena("sala17")

    elif acao == "pegar_codigo3":
        if not state["codigo3_pego"]:
            state["codigo3_pego"] = True
            adicionar_item("Código de Acesso #3", 20)
            mostrar_cena("arquivo")

    elif acao == "ligar_gerador":
        state["gerador_ligado"] = True
        state["pontos"] += 25
        mostrar_cena("alarme")

    elif acao == "combater_lanterna":
        state["pontos"] += 25
        mostrar_cena("combate_vitoria")

    elif acao == "lutar_criatura":
        morreu = perder_vida(2)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("dano_criatura")

    elif acao == "tentar_desligar":
        tem_codigos = (
            possui_item("Código de Acesso #1")
            and possui_item("Código de Acesso #2")
            and possui_item("Código de Acesso #3")
        )
        if tem_codigos:
            state["pontos"] += 50
            mostrar_cena("fim_sacrificio")
        else:
            mostrar_cena("nucleo_incompleto")

    elif acao in SCENES:
        mostrar_cena(acao)

def escolher_opcao(num):
    opcoes = opcoes_da_cena(state["cena"], SCENES[state["cena"]])
    if (num - 1) < len(opcoes):
        executar_acao(opcoes[num - 1][1])

# ============================================================
# EVENT LISTENERS
# ============================================================

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
    state["lanterna_pega"] = False
    state["chave_pega"] = False
    state["kit_medico_pego"] = False
    state["cracha_pego"] = False
    state["porta_restrita_aberta"] = False
    state["porta_seguranca_aberta"] = False
    state["computador_hackeado"] = False
    state["codigo2_pego"] = False
    state["codigo3_pego"] = False
    state["gerador_ligado"] = False
    state["escada_iluminada"] = False

    trilha = CONFIG.get("trilha_inicial")
    if trilha:
        window.frameworkAudio.play(trilha)
    mostrar_cena(CONFIG["cena_inicial"])

# Inicialização
configurar_identidade()
mostrar_cena(CONFIG["cena_inicial"])
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
