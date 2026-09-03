# ============================================================
# PROJETO ECLIPSE - ENGINE NARRATIVA TOTALMENTE REATIVA
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
    # Histórico de coleta
    "lanterna_pega": False,
    "chave_pega": False,
    "kit_medico_pego": False,
    "cracha_pego": False,
    "foto_vista": False,
    # Histórico de portas e acessos
    "tomou_choque_restrita": False,
    "tomou_choque_seguranca": False,
    "porta_restrita_aberta": False,
    "porta_seguranca_aberta": False,
    "escada_desceu_com_luz": False,
    # Progresso técnico da trama
    "arquivos_lidos": False,
    "audio_ouvido": False,
    "computador_hackeado": False,
    "codigo2_pego": False,
    "codigo3_pego": False,
    "gerador_ligado": False,
    "monstro_derrotado": False,
}

# ============================================================
# MAPA DE CENAS E CONTEXTOS REATIVOS
# ============================================================

SCENES = {
    "inicio": {
        "title": "O Despertar",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você acorda no chão frio com sangue nas mãos e sem memórias.\n\n"
            'O alarme avisa: "COLAPSO EM 47 MINUTOS." Na porta blindada ao lado está gravado: '
            '"NÃO CONFIE NAQUELE QUE TEM O SEU ROSTO."\n\n'
            "O que você decide fazer?"
        ),
    },
    "inicio_retorno": {
        "title": "Laboratório de Despertar",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você está de volta à câmara onde despertou. O chão manchado de sangue continua o mesmo, "
            "mas agora você compreende melhor o perigo do local.\n\n"
            "Qual o seu próximo passo?"
        ),
    },

    # --- ARMÁRIO E REAÇÕES DE BUSCA ---
    "armario": {
        "title": "Armário de Emergência",
        "image": "assets/imagens/capa.jfif",
        "text": "O armário de metal oxidado está aberto. Há gavetas emperradas e prateleiras com ferramentas.",
    },
    "pegou_lanterna": {
        "title": "Lanterna Tática em Mãos",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você retira a pesada lanterna de metal e aciona o feixe (+10 pts).\n\n"
            "A luz corta a penumbra da sala. Agora as descidas escuras e os cantos escuros podem ser explorados sem perigo de tropeço.\n\n"
            "O que fará com seu novo equipamento?"
        ),
    },
    "pegou_chave": {
        "title": "Chave Mestra de Segurança",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você retira a chave de ferro fundido (+10 pts). Ela possui dentes pesados, "
            "típicos das portas mecânicas de segurança do complexo.\n\n"
            "Qual o seu destino com a chave?"
        ),
    },
    "pegou_kit": {
        "title": "Kit Médico Coletado",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você guarda o estojo de primeiros socorros biológico (+10 pts).\n\n"
            "Ele poderá ser injetado para fechar ferimentos caso sofra queimaduras ou ataques graves.\n\n"
            "Para onde deseja ir agora?"
        ),
    },
    "pegou_cracha": {
        "title": "Credencial do Dr. Mateus",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você recolhe o crachá magnético de autorização máxima (+15 pts). O homem na foto é uma cópia idêntica de você.\n\n"
            "O sensor da porta blindada agora aceitará a aproximação deste cartão.\n\n"
            "Qual a sua próxima escolha?"
        ),
    },
    "armario_foto": {
        "title": "A Fotografia Reveladora",
        "image": "assets/imagens/capa.jfif",
        "text": (
            'A fotografia mostra uma equipe brindando em 2038. No verso: "Dr. Mateus Almeida - Matriz Original".\n\n'
            "Sua cabeça arde com pontadas ao perceber que você pode não ser o humano original dessa história.\n\n"
            "Como deseja agir?"
        ),
    },

    # --- CORREDOR E PORTAS COM REAÇÃO ---
    "corredor": {
        "title": "Corredor Principal",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Lâmpadas estalam soltando faíscas. À sua esquerda fica a Sala de Controle; "
            "ao centro uma escada íngreme em direção aos laboratórios inferiores; e à direita a Porta de Segurança reforçada."
        ),
    },
    "porta_choque_restrita": {
        "title": "Descarga Violenta!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você tenta forçar os fechos da porta blindada desprotegido!\n\n"
            "Um arco elétrico salta do sensor, queimando suas mãos e arremessando você no chão (-1 Vida). "
            "Fica óbvio que ela exige um crachá de identificação oficial para abrir.\n\n"
            "Com as mãos ainda trêmulas, qual sua atitude?"
        ),
    },
    "porta_choque_seguranca": {
        "title": "Choque no Ferrolho!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Ao puxar a maçaneta da Porta de Segurança trancada, o sistema de alarme periférico dispara uma corrente elétrica (-1 Vida)!\n\n"
            "Essa porta requer uma chave física mecânica para contornar o trincador energizado.\n\n"
            "Recuando tossindo poeira, o que decide fazer?"
        ),
    },
    "queda_escada": {
        "title": "Queda no Abismo Escuro",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você tenta descer a escadaria sem enxergar onde pisa.\n\n"
            "Seu calçado desliza em uma mancha de óleo sintético; você tomba e rola 15 degraus de metal abaixo no breu total (-1 Vida).\n\n"
            "Você se levanta arranhado. Sem uma lanterna para iluminar o trajeto, descer aqui é suicídio.\n\n"
            "Como vai proceder?"
        ),
    },

    # --- SALA DE CONTROLE ---
    "controle": {
        "title": "Sala de Controle Central",
        "image": "assets/imagens/capa.jfif",
        "text": "Fileiras de monitores estáticos. No centro da sala fria, apenas um terminal central permanece pulsando em verde.",
    },
    "ler_arquivos": {
        "title": "Registros Secretos de Clonagem",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você lê os relatórios ultrassecretos:\n\n"
            "- As réplicas entram em histeria violenta ao saberem de sua condição artificial.\n"
            "- O reator entrará em fusão para purgar tudo, a menos que os 3 Códigos de Acesso sejam reunidos.\n\n"
            "O que decide fazer com esse conhecimento?"
        ),
    },
    "ouvir_gravacao": {
        "title": "Gravação de Áudio #07",
        "image": "assets/imagens/capa.jfif",
        "text": (
            'Uma voz igual à sua sussurra no interfone:\n\n'
            '"Se esta mensagem toca, meu projeto virou um pesadelo. Criei clones para me sucederem após minha morte, '
            'mas se eles escaparem para o exterior, ninguém distinguirá o criador do monstro..."\n\n'
            "O que você investigará a seguir?"
        ),
    },
    "pc_hackeado_sucesso": {
        "title": "Terminal Invadido: Código #1 Obtido",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você digita o código biográfico e rompe a proteção!\n\n"
            "O leitor grava no seu inventário a [1ª PARTE DO CÓDIGO DE DESLIGAMENTO] (+20 pts).\n\n"
            "Para onde vai com a primeira chave mestra?"
        ),
    },

    # --- SUBSOLO E SETOR MÉDICO ---
    "subsolo": {
        "title": "Laboratórios Inferiores",
        "image": "assets/imagens/capa.jfif",
        "text": "O ar aqui cheira a ozônio queimado. Trilhas de sangue fresco levam à Sala 17 e ao Laboratório Principal.",
    },
    "sala17": {
        "title": "Sala 17 - Isolamento",
        "image": "assets/imagens/capa.jfif",
        "text": "Uma maca arrebentada sob lâmpadas azuis. No chão, perto de vidros quebrados, repousa um módulo com a 2ª parte do código.",
    },
    "pegou_codigo2": {
        "title": "Código #2 Extraído",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você pega o módulo cirúrgico: [2ª PARTE DO CÓDIGO DE DESLIGAMENTO] (+20 pts).\n\n"
            "Ao guardar a peça, você ouve passos pesados marchando nos túneis próximos.\n\n"
            "O que fará imediatamente?"
        ),
    },

    # --- LABORATÓRIO E GERADOR ---
    "laboratorio": {
        "title": "Laboratório de Clonagem",
        "image": "assets/imagens/capa.jfif",
        "text": "Dezenas de tanques com corpos idênticos a você suspensos em líquido verde. Os caminhos levam ao Gerador e aos Dutos de ar.",
    },
    "gerador": {
        "title": "Sala do Gerador Auxiliar",
        "image": "assets/imagens/capa.jfif",
        "text": "A turbina está desativada. Uma alavanca de emergência aguarda para restabelecer energia e forçar os sistemas de contenção.",
    },
    "alarme": {
        "title": "Sirene de Emergência!",
        "image": "assets/imagens/capa.jfif",
        "audio": "assets/audios/alarme.mp3",
        "text": (
            "Ao acionar o gerador, os alarmes gritam no teto!\n\n"
            "Uma porta de contenção arrebenta e uma réplica deformada com seu rosto avança segurando uma barra de ferro em fúria cega!\n\n"
            "Como você reage?"
        ),
    },
    "combate_vitoria": {
        "title": "Fuga com Sucesso!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você usa a lanterna pesada como porrete e atinge o clone na têmpora! "
            "Ele tomba no chão desorientado, abrindo passagem limpa (+25 pts).\n\n"
            "Qual rota de escape você toma?"
        ),
    },
    "dano_criatura": {
        "title": "Confronto Brutal",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você luta com as mãos desprotegidas contra a criatura. Ela o atira contra as ferragens cortantes (-2 Vidas) "
            "antes de você conseguir se esgueirar pelo duto de exaustão!\n\n"
            "Ferido gravemente dentro da tubulação estreita, o que fará?"
        ),
    },

    # --- ARQUIVO E MEMÓRIAS ---
    "arquivo": {
        "title": "Arquivo Morto",
        "image": "assets/imagens/capa.jfif",
        "text": "Gaveteiros com fichas de voluntários e réplicas. Nos fundos da sala há uma cápsula com a 3ª parte do código e uma câmara criogênica.",
    },
    "pegou_codigo3": {
        "title": "Código #3 Recuperado",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você recolhe o disco com a [3ª PARTE DO CÓDIGO DE DESLIGAMENTO] (+20 pts)!\n\n"
            "Agora você possui todos os fragmentos necessários para desativar o reator no Núcleo.\n\n"
            "Qual o seu próximo movimento?"
        ),
    },
    "memorias": {
        "title": "A Revelação de Mateus",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Na cápsula repousa o verdadeiro Dr. Mateus, quase sem pulso. Ele abre os olhos: "
            "'Você é minha criação mais perfeita... se salvar o complexo, o que fará de mim?'\n\n"
            "Que decisão você toma diante do seu criador?"
        ),
    },

    # --- VENTILAÇÃO E ROTAS FINAIS ---
    "tunel": {
        "title": "Duto de Ventilação",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "O vento zune alto na tubulação. O túnel se divide em 3 ramais:\n"
            "- Duto Azul (exaustão para a mata exterior)\n"
            "- Duto Vermelho (descida direta para o Núcleo do Reator)\n"
            "- Duto Preto (ramificação sem identificação no mapa)"
        ),
    },
    "sala_secreta": {
        "title": "Câmara Clandestina",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Uma cadeira de interface neural diante de um espelho. Seu reflexo sorri sem que você sorria: "
            "'Quer as memórias originais de volta e o domínio sobre todas as cópias?'\n\n"
            "O que decide fazer?"
        ),
    },
    "nucleo": {
        "title": "Núcleo do Reator",
        "image": "assets/imagens/capa.jfif",
        "text": "O coração energético está superaquecido em pulsos vermelhos. O console de desligamento exige a senha trifásica completa.",
    },
    "nucleo_incompleto": {
        "title": "Acesso Negado!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "O console rejeita o comando: 'CÓDIGO INCOMPLETO'.\n\n"
            "Você não reuniu os 3 códigos espalhados pelo complexo para desativar o reator manualmente.\n\n"
            "O que tenta fazer no desespero?"
        ),
    },
    "nucleo_perigoso": {
        "title": "Descarga de Plasma!",
        "image": "assets/imagens/capa.jfif",
        "text": (
            "Você arranca os cabos à força! Uma onda de fogo queima seus braços (-2 Vidas) e as paredes estilhaçam ao redor.\n\n"
            "O tempo acabou. O que tenta fazer antes do desmoronamento?"
        ),
    },

    # --- FINAIS ---
    "fuga_dupla": {
        "title": "FINAL: A VERDADEIRA FUGA",
        "image": "assets/imagens/capa.jfif",
        "text": "Você ampara o criador e ambos usam a cápsula de emergência antes da detonação. Você provou ter mais humanidade que seus algozes.\n\n[FINAL BOM]",
        "options": [],
    },
    "fim_egoista": {
        "title": "FINAL: O SOBREVIVENTE",
        "image": "assets/imagens/capa.jfif",
        "text": "Você escapa sozinho pelas matas. Seis meses depois, alguém bate na sua janela: uma cópia com seu mesmo rosto veio cobrar a conta.\n\n[FINAL RUIM]",
        "options": [],
    },
    "saida_falsa": {
        "title": "FINAL: EXÉRCITO DE RÉPLICAS",
        "image": "assets/imagens/capa.jfif",
        "text": "Você sai na clareira sentindo o vento noturno. Na borda da floresta, centenas de homens idênticos a você o observam em silêncio.\n\n[FINAL RUIM]",
        "options": [],
    },
    "fim_sacrificio": {
        "title": "FINAL: O SACRIFÍCIO HERÓICO",
        "image": "assets/imagens/capa.jfif",
        "text": "Com os 3 fragmentos alinhados, a purga final dissolve as câmaras e seu próprio corpo sintético. O mundo lá fora foi protegido por você.\n\n[FINAL HERÓICO]",
        "options": [],
    },
    "final_memorias": {
        "title": "FINAL SECRETO: CONSCIÊNCIA TOTAL",
        "image": "assets/imagens/capa.jfif",
        "text": "Ao conectar os eletrodos, a mente de todas as cópias se funde em você. Dotado de superinteligência, você assume o Projeto Eclipse.\n\n[FINAL SECRETO]",
        "options": [],
    },
    "fim_libertador": {
        "title": "FINAL: O LIBERTADOR",
        "image": "assets/imagens/capa.jfif",
        "text": "Você conecta o reator à antena externa e transmite todo o projeto para a internet global. Ninguém mais poderá esconder a verdade.\n\n[FINAL BOM ALTERNATIVO]",
        "options": [],
    },
    "fim_ruim": {
        "title": "GAME OVER",
        "image": "assets/imagens/capa.jfif",
        "text": "Seu corpo não aguenta mais os ferimentos. Você tomba sem vida enquanto a contagem regressiva chega a zero.",
        "options": [],
    },
}

# ============================================================
# GERADOR DE OPÇÕES TOTALMENTE BASEADO EM ESTADO
# ============================================================

def opcoes_da_cena(nome, cena):
    opcoes = []

    # Condição contextual de cura com kit médico
    pode_curar = (
        "Kit médico" in state["inventario"]
        and state["vida"] < CONFIG["vida_maxima"]
        and not nome.startswith("fim")
    )

    if nome in ["inicio", "inicio_retorno"]:
        opcoes.append(("Entrar no Corredor Principal", "ir_corredor"))
        
        # Opções do armário mudam de acordo com o que já foi retirado
        itens_restantes = not (state["lanterna_pega"] and state["chave_pega"] and state["kit_medico_pego"] and state["cracha_pego"])
        if itens_restantes:
            opcoes.append(("Vasculhar o Armário de Emergência", "ir_armario"))
        else:
            opcoes.append(("Olhar o Armário (Já Vazio)", "ir_armario_vazio"))

        # Interação com a porta blindada inicial
        if state["porta_restrita_aberta"]:
            opcoes.append(("Passar pela Porta Blindada (Aberta)", "entrar_laboratorio"))
        elif "Crachá do Dr. Mateus" in state["inventario"]:
            opcoes.append(("Usar Crachá no Leitor da Porta Blindada", "abrir_porta_restrita_cracha"))
        elif state["tomou_choque_restrita"]:
            opcoes.append(("Examinar a fiação queimada da Porta", "examinar_painel_queimado"))
        else:
            opcoes.append(("Forçar o painel da Porta Blindada", "forcar_porta_restrita"))

    elif nome in ["armario", "ir_armario_vazio"]:
        if not state["lanterna_pega"]:
            opcoes.append(("Pegar a Lanterna de Metal", "pegar_lanterna"))
        if not state["chave_pega"]:
            opcoes.append(("Pegar a Chave Mestra", "pegar_chave"))
        if not state["kit_medico_pego"]:
            opcoes.append(("Pegar o Kit Médico", "pegar_kit"))
        if not state["cracha_pego"]:
            opcoes.append(("Pegar o Crachá do Dr. Mateus", "pegar_cracha"))
        if not state["foto_vista"]:
            opcoes.append(("Examinar a fotografia antiga no fundo", "ver_foto"))
        
        opcoes.append(("Sair do armário e voltar ao laboratório", "inicio_retorno"))

    elif nome in ["pegou_lanterna", "pegou_chave", "pegou_kit", "pegou_cracha", "armario_foto"]:
        opcoes.append(("Continuar revirando o armário", "armario"))
        opcoes.append(("Avançar para o Corredor Principal", "ir_corredor"))
        if "Crachá do Dr. Mateus" in state["inventario"] and not state["porta_restrita_aberta"]:
            opcoes.append(("Usar o crachá na porta blindada da sala", "abrir_porta_restrita_cracha"))

    elif nome == "corredor":
        opcoes.append(("Entrar na Sala de Controle", "ir_controle"))
        
        # Opções de descida da escada mudam se você já tem luz
        if state["escada_desceu_com_luz"] or "Lanterna pesada" in state["inventario"]:
            opcoes.append(("Descer para o Subsolo (Com a Lanterna)", "descer_escadas_sucesso"))
        else:
            opcoes.append(("Tentar descer a escadaria escura às cegas", "descer_escadas_escuro"))

        # Opção da Porta de Segurança
        if state["porta_seguranca_aberta"]:
            opcoes.append(("Entrar no Arquivo Morto (Porta Destrancada)", "ir_arquivo"))
        elif "Chave enferrujada" in state["inventario"]:
            opcoes.append(("Usar Chave Mestra na Porta de Segurança", "abrir_seguranca_chave"))
        else:
            opcoes.append(("Tentar forçar a Porta de Segurança", "forcar_porta_seguranca"))

        opcoes.append(("Voltar à sala onde você acordou", "inicio_retorno"))

    elif nome == "controle":
        if not state["arquivos_lidos"]:
            opcoes.append(("Ler os arquivos confidenciais", "acao_ler_arquivos"))
        if not state["audio_ouvido"]:
            opcoes.append(("Ouvir fita de áudio gravada", "acao_ouvir_audio"))
        if not state["computador_hackeado"]:
            opcoes.append(("Hackear terminal e extrair Código #1", "acao_hackear_pc"))
        
        opcoes.append(("Sair da Sala de Controle para o Corredor", "ir_corredor"))

    elif nome in ["ler_arquivos", "ouvir_gravacao", "pc_hackeado_sucesso"]:
        if not state["computador_hackeado"]:
            opcoes.append(("Hackear o terminal central", "acao_hackear_pc"))
        opcoes.append(("Voltar para o Corredor Principal", "ir_corredor"))
        if not state["arquivos_lidos"]:
            opcoes.append(("Ler os registros técnicos", "acao_ler_arquivos"))

    elif nome == "subsolo":
        if not state["codigo2_pego"]:
            opcoes.append(("Investigar a Sala 17 (Isolamento Médico)", "ir_sala17"))
        opcoes.append(("Avançar para os Tanques de Clonagem", "ir_laboratorio"))
        opcoes.append(("Subir de volta pela escada ao Corredor", "ir_corredor"))

    elif nome == "sala17":
        if not state["codigo2_pego"]:
            opcoes.append(("Recolher o módulo do Código #2", "acao_pegar_codigo2"))
        opcoes.append(("Sair da Sala 17 e voltar ao Subsolo", "subsolo"))

    elif nome == "pegou_codigo2":
        opcoes.append(("Correr para o Laboratório de Clonagem", "ir_laboratorio"))
        opcoes.append(("Voltar para a escada do subsolo", "subsolo"))

    elif nome == "laboratorio":
        if not state["gerador_ligado"]:
            opcoes.append(("Entrar na Sala do Gerador", "ir_gerador"))
        opcoes.append(("Entrar na tubulação de ventilação", "ir_tunel"))
        if state["porta_seguranca_aberta"]:
            opcoes.append(("Passar para o Arquivo Morto", "ir_arquivo"))
        opcoes.append(("Voltar para o corredor do Subsolo", "subsolo"))

    elif nome == "gerador":
        if not state["gerador_ligado"]:
            opcoes.append(("Puxar a alavanca do gerador", "acao_ligar_gerador"))
        opcoes.append(("Recuar para os tanques do Laboratório", "ir_laboratorio"))

    elif nome == "alarme":
        if "Lanterna pesada" in state["inventario"]:
            opcoes.append(("Golpear o clone com a lanterna de metal", "acao_luta_lanterna"))
        opcoes.append(("Enfrentar o clone de mãos vazias", "acao_luta_desarmado"))
        opcoes.append(("Tentar fugir às cegas pelo duto", "acao_fugir_duto"))

    elif nome == "combate_vitoria":
        opcoes.append(("Mergulhar seguro no duto de ventilação", "ir_tunel"))
        opcoes.append(("Acessar a porta do Arquivo Morto", "ir_arquivo"))

    elif nome == "arquivo":
        if not state["codigo3_pego"]:
            opcoes.append(("Pegar o pendrive com o Código #3", "acao_pegar_codigo3"))
        opcoes.append(("Acessar a Câmara de Memórias (Dr. Mateus)", "ir_memorias"))
        opcoes.append(("Seguir pelos dutos de ventilação", "ir_tunel"))

    elif nome == "pegou_codigo3":
        opcoes.append(("Inspecionar a cápsula do Dr. Mateus", "ir_memorias"))
        opcoes.append(("Entrar na tubulação de ar direto ao Núcleo", "ir_tunel"))

    elif nome == "memorias":
        opcoes.append(("Salvar o Dr. Mateus e fugir juntos", "fuga_dupla"))
        opcoes.append(("Desligar o suporte de vida dele e fugir só", "fim_egoista"))
        opcoes.append(("Ignorá-lo e correr para desarmar o Núcleo", "ir_nucleo"))

    elif nome == "tunel":
        opcoes.append(("Duto Azul: Saída para a superfície", "saida_falsa"))
        opcoes.append(("Duto Vermelho: Descida direta ao Núcleo", "ir_nucleo"))
        opcoes.append(("Duto Preto: Tubulação secreta não mapeada", "ir_sala_secreta"))

    elif nome == "sala_secreta":
        opcoes.append(("Conectar-se à máquina de memórias neurais", "final_memorias"))
        opcoes.append(("Quebrar o painel e buscar a mata", "saida_falsa"))
        opcoes.append(("Voltar ao duto e ir para o Núcleo", "ir_nucleo"))

    elif nome in ["nucleo", "nucleo_incompleto"]:
        tem_3_codigos = (
            "Código de Acesso #1" in state["inventario"]
            and "Código de Acesso #2" in state["inventario"]
            and "Código de Acesso #3" in state["inventario"]
        )
        if tem_3_codigos:
            opcoes.append(("Inserir os 3 Códigos de Segurança Mestre", "fim_sacrificio"))
        else:
            opcoes.append(("Tentar digitar os códigos parciais", "acao_tentar_desligar_falha"))

        opcoes.append(("Arrancar os cabos do núcleo à força", "acao_arrancar_cabos"))
        opcoes.append(("Transmitir os dados para o mundo inteiro", "fim_libertador"))

    elif "options" in cena:
        opcoes = list(cena["options"])

    # Se estiver ferido, inclui a opção de cura dinâmica sem sobrescrever escolhas críticas
    if pode_curar:
        if len(opcoes) >= 4:
            opcoes[3] = ("Usar Kit Médico (+2 Vidas)", "usar_kit_medico")
        else:
            opcoes.append(("Usar Kit Médico (+2 Vidas)", "usar_kit_medico"))

    return opcoes[:4]

# ============================================================
# TRANSIÇÕES E EXECUÇÃO
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
    # Uso de consumível
    if acao == "usar_kit_medico":
        if "Kit médico" in state["inventario"]:
            remover_item("Kit médico")
            state["vida"] = min(CONFIG["vida_maxima"], state["vida"] + 2)
            state["pontos"] += 15
            atualizar_status()
            mostrar_cena(state["cena"])
        return

    # Navegação básica
    if acao == "inicio_retorno":
        mostrar_cena("inicio_retorno")
    elif acao == "ir_armario":
        mostrar_cena("armario")
    elif acao == "ir_armario_vazio":
        mostrar_cena("armario")
    elif acao == "ir_corredor":
        mostrar_cena("corredor")
    elif acao == "ir_controle":
        mostrar_cena("controle")
    elif acao == "ir_laboratorio":
        mostrar_cena("laboratorio")
    elif acao == "ir_gerador":
        mostrar_cena("gerador")
    elif acao == "ir_sala17":
        mostrar_cena("sala17")
    elif acao == "ir_arquivo":
        mostrar_cena("arquivo")
    elif acao == "ir_memorias":
        mostrar_cena("memorias")
    elif acao == "ir_tunel":
        mostrar_cena("tunel")
    elif acao == "ir_sala_secreta":
        mostrar_cena("sala_secreta")
    elif acao == "ir_nucleo":
        mostrar_cena("nucleo")

    # Coletas do Armário
    elif acao == "pegar_lanterna":
        state["lanterna_pega"] = True
        adicionar_item("Lanterna pesada", 10)
        mostrar_cena("pegou_lanterna")
    elif acao == "pegar_chave":
        state["chave_pega"] = True
        adicionar_item("Chave enferrujada", 10)
        mostrar_cena("pegou_chave")
    elif acao == "pegar_kit":
        state["kit_medico_pego"] = True
        adicionar_item("Kit médico", 10)
        mostrar_cena("pegou_kit")
    elif acao == "pegar_cracha":
        state["cracha_pego"] = True
        adicionar_item("Crachá do Dr. Mateus", 15)
        mostrar_cena("pegou_cracha")
    elif acao == "ver_foto":
        state["foto_vista"] = True
        mostrar_cena("armario_foto")

    # Interações com Portas
    elif acao == "forcar_porta_restrita":
        state["tomou_choque_restrita"] = True
        morreu = perder_vida(1)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque_restrita")
    elif acao == "examinar_painel_queimado":
        mostrar_cena("porta_choque_restrita")
    elif acao == "abrir_porta_restrita_cracha":
        state["porta_restrita_aberta"] = True
        state["pontos"] += 20
        mostrar_cena("laboratorio")
    elif acao == "entrar_laboratorio":
        mostrar_cena("laboratorio")

    elif acao == "forcar_porta_seguranca":
        state["tomou_choque_seguranca"] = True
        morreu = perder_vida(1)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("porta_choque_seguranca")
    elif acao == "abrir_seguranca_chave":
        state["porta_seguranca_aberta"] = True
        state["pontos"] += 20
        mostrar_cena("arquivo")

    # Escada
    elif acao == "descer_escadas_escuro":
        morreu = perder_vida(1)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("queda_escada")
    elif acao == "descer_escadas_sucesso":
        state["escada_desceu_com_luz"] = True
        mostrar_cena("subsolo")

    # Sala de Controle
    elif acao == "acao_ler_arquivos":
        state["arquivos_lidos"] = True
        mostrar_cena("ler_arquivos")
    elif acao == "acao_ouvir_audio":
        state["audio_ouvido"] = True
        mostrar_cena("ouvir_gravacao")
    elif acao == "acao_hackear_pc":
        state["computador_hackeado"] = True
        adicionar_item("Código de Acesso #1", 20)
        mostrar_cena("pc_hackeado_sucesso")

    # Subsolo e Códigos
    elif acao == "acao_pegar_codigo2":
        state["codigo2_pego"] = True
        adicionar_item("Código de Acesso #2", 20)
        mostrar_cena("pegou_codigo2")
    elif acao == "acao_pegar_codigo3":
        state["codigo3_pego"] = True
        adicionar_item("Código de Acesso #3", 20)
        mostrar_cena("pegou_codigo3")

    # Gerador e Combate
    elif acao == "acao_ligar_gerador":
        state["gerador_ligado"] = True
        state["pontos"] += 25
        mostrar_cena("alarme")
    elif acao == "acao_luta_lanterna":
        state["monstro_derrotado"] = True
        state["pontos"] += 30
        mostrar_cena("combate_vitoria")
    elif acao in ["acao_luta_desarmado", "acao_fugir_duto"]:
        morreu = perder_vida(2)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("dano_criatura")

    # Núcleo
    elif acao == "acao_tentar_desligar_falha":
        mostrar_cena("nucleo_incompleto")
    elif acao == "acao_arrancar_cabos":
        morreu = perder_vida(2)
        mostrar_cena("fim_ruim") if morreu else mostrar_cena("nucleo_perigoso")

    # Finais diretos
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
    state["foto_vista"] = False
    state["tomou_choque_restrita"] = False
    state["tomou_choque_seguranca"] = False
    state["porta_restrita_aberta"] = False
    state["porta_seguranca_aberta"] = False
    state["escada_desceu_com_luz"] = False
    state["arquivos_lidos"] = False
    state["audio_ouvido"] = False
    state["computador_hackeado"] = False
    state["codigo2_pego"] = False
    state["codigo3_pego"] = False
    state["gerador_ligado"] = False
    state["monstro_derrotado"] = False

    trilha = CONFIG.get("trilha_inicial")
    if trilha:
        window.frameworkAudio.play(trilha)
    mostrar_cena(CONFIG["cena_inicial"])

# Inicialização
configurar_identidade()
mostrar_cena(CONFIG["cena_inicial"])
el("botao-iniciar").disabled = False
el("botao-iniciar").innerText = "▶ INICIAR JOGO"
