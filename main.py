# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================
CONFIG = {
    "titulo": "PROJETO ECLIPSE",
    "subtitulo": "Uma aventura de terror sci-fi",
    "autor": "Anna Beatriz",
    "icone": "🌑",
    "capa": None, # Pode colocar "assets/imagens/capa.jpg" depois
    "trilha_inicial": "assets/audios/tema_principal.mp3", 
    "volume_inicial": 0.5,
    "vida_inicial": 5,
    "pontos_iniciais": 0,
    "cena_inicial": "inicio",
}

# ============================================================
# CENAS DO JOGO
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
            "Você tenta forçar o painel da porta restrita sem o crachá.\n\n"
            "Uma descarga elétrica violenta atravessa seu braço! Você perdeu 1 vida."
        ),
        "options": [("Recuar", "inicio")],
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
            "Você localizou a primeira parte do código de evacuação!"
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
            "Debaixo da maca, você encontra um cartão com a Segunda Parte do Código de Evacuação!"
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
            "Você revira algumas caixas e encontra a Terceira Parte do Código!\n\n"
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
# REGRAS E AÇÕES ESPECIAIS
# ============================================================
def executar_acao(acao):
    
    # ITENS DO ARMÁRIO
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

    # PORTAS
    elif acao == "tentar_porta_restrita":
        if possui_item("crachá"):
            mostrar_cena("laboratorio")
        else:
            morreu = perder_vida(1)
            if not morreu:
                mostrar_cena("porta_choque")

    elif acao == "tentar_porta_seguranca":
        if possui_item("chave"):
            mostrar_cena("arquivo")
        else:
            morreu = perder_vida(1)
            if not morreu:
                mostrar_cena("porta_choque")

    # DESCER ESCADAS (Verifica Lanterna)
    elif acao == "descer_escadas":
        if possui_item("lanterna"):
            mostrar_cena("subsolo")
        else:
            morreu = perder_vida(1)
            if not morreu:
                mostrar_cena("queda_escada")

    # CÓDIGOS
    elif acao == "ativar_pc":
        adicionar_item("codigo1")
        mostrar_cena("ativar_pc")
        
    elif acao == "pegar_codigo2":
        adicionar_item("codigo2")
        mostrar_cena("subsolo")
        
    elif acao == "pegar_codigo3":
        adicionar_item("codigo3")
        mostrar_cena("subsolo")

    # EVENTOS CRÍTICOS
    elif acao == "ligar_gerador":
        mostrar_cena("alarme")

    elif acao == "lutar_criatura":
        morreu = perder_vida(2)
        if not morreu:
            mostrar_cena("dano_criatura")

    elif acao == "tentar_desligar":
        if possui_item("codigo1") and possui_item("codigo2") and possui_item("codigo3"):
            ganhar_pontos(100)
            mostrar_cena("fim_sacrificio")
        else:
            mostrar_cena("nucleo") # Fica preso no núcleo se não tiver as 3 senhas
