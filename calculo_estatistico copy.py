import glob

# codigo que le todos os angulos de todas as variaveis (tanto pra MMMSS como pra COLUNA) nos arquivos
# e salva todos esses valores em listas contendo o nome das variaveis
# posteriormente usa essas listas para fazer o calculo estatistico


# função que calcula a correlação entre dados que estão presentes em duas listas
def correlacao(lista_ouro, lista_video):
    
    soma_x = 0.0
    soma_y = 0.0
    soma_quadrado_x = 0.0
    soma_quadrado_y = 0.0
    soma_x_y = 0.0

    # i eh o numero de pares ordenados. as listas devem possuir o mesmo tamanho!!

    # usando a menor lista como referencia, para não dar erro de acesso indevido na lista menor
    if(len(lista_ouro) > len(lista_video)):
        
        for i in range(len(lista_video)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_video)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)

        # calculados os termos necessarios, agr eh so aplicar esses numeros na expressao matematica que calcula a correlaçao

        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
    
    else:

        for i in range(len(lista_ouro)):
            soma_x += lista_ouro[i]
            soma_y += lista_video[i]
            soma_quadrado_x += lista_ouro[i] ** 2
            soma_quadrado_y += lista_video[i] ** 2
            soma_x_y += lista_ouro[i] * lista_video[i]


        n = len(lista_ouro)    
        aux_1 = ((n * soma_quadrado_x - soma_x**2)**0.5)
        aux_2 = ((n * soma_quadrado_y - soma_y**2 )**0.5)
        
        correlacao = ((n * soma_x_y) - soma_x * soma_y ) / (aux_1 * aux_2)

        return correlacao
   



# função que recebe duas listas e calcula o erro medio absoluto entre os dados
# essas listas devem possuir o mesmo tamanho
# uma lista contém os ângulos calculados a partir dos videos
# a outra lista contém os ângulos calculados a partir dos tsv
def erro_medio_absoluto(lista_ouro, lista_video):
    
    # lista que vai guardar cada um dos erros absoluto entre os ângulos
    #erro_medio = []

    if(len(lista_ouro) > len(lista_video)):
        soma = 0

        for i in range(len(lista_video)):
            soma += abs(lista_ouro[i] - lista_video[i])


        return soma / len(lista_video)    

    else:
        soma = 0

        for i in range(len(lista_ouro)):
            soma += abs(lista_ouro[i] - lista_video[i])

        return soma / len(lista_ouro)
 

    

# DECLARANDO AS LISTAS PARA REPRESENTAR TODAS AS VARIAVEIS
# MMSS
## OBSERVAÇÃO: FRONTAL = 30 FRAMES  // LATERAL = 60 FRAMES 
abd_ombro_direito_ouro = []
abd_ombro_direito_video_frontal = []
abd_ombro_direito_video_lateral = []

abd_ombro_esquerdo_ouro = []
abd_ombro_esquerdo_video_frontal = []
abd_ombro_esquerdo_video_lateral = []


flexao_cotov_direito_ouro = []
flexao_cotov_direito_video_frontal = []
flexao_cotov_direito_video_lateral = []

flexao_cotov_esquerdo_ouro = []
flexao_cotov_esquerdo_video_frontal = []
flexao_cotov_esquerdo_video_lateral = []


flexao_ombro_direito_ouro = []
flexao_ombro_direito_video_frontal = []
flexao_ombro_direito_video_lateral = []

flexao_ombro_esquerdo_ouro = []
flexao_ombro_esquerdo_video_frontal = []
flexao_ombro_esquerdo_video_lateral = []

# COLUNA
# OBSERVACAO: FRONTAL = 60 FRAMES   // LATERAL = 30 FRAMES
flexao_cabeca_ouro = []
flexao_cabeca_video_frontal = []
flexao_cabeca_video_lateral = []

flexao_tronco_ouro = []
flexao_tronco_video_frontal = []
flexao_tronco_video_lateral = []


rotacao_tronco_ouro = []
rotacao_tronco_video_frontal = []
rotacao_tronco_video_lateral = []


# busca por todos os arquivos TSV no diretorio especificado
pasta_ouro_MMSS = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/MMSS/padrao_ouro/*.tsv")
pasta_video_frontal_MMSS = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/MMSS/video_mmss/frontal/*.tsv")
pasta_video_lateral_MMSS = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/MMSS/video_mmss/lateral/*.tsv")

pasta_ouro_COLUNA = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/padrao_ouro/*.tsv")
pasta_video_frontal_COLUNA = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/video_coluna/frontal/*.tsv")
pasta_video_lateral_COLUNA = glob.glob("C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/video_coluna/lateral/*.tsv")

#padrao_ouro_MMSS = 'C:/Users/jhona/OneDrive/Desktop/estatistica/MMSS/padrao_ouro/padrao_ouro_Bianca_MMSS.tsv'
#video_MMSS = 'C:/Users/jhona/OneDrive/Desktop/estatistica\MMSS/video_mmss/video_Bianca_MMSS.tsv'

#padrao_ouro_COLUNA = 'C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/padrao_ouro/padra_ouro_Bianca_COLUNA.tsv'
#video_COLUNA = 'C:/Users/jhona/OneDrive/Desktop/estatistica/COLUNA/video_coluna/video_Bianca_COLUNA.tsv'



################################################################################################################
################################################################################################################
#                                   MMSS

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_OURO
# E SALVANDO NAS LISTAS OS ANGULOS
#print(pasta_ouro_MMSS)
for nome_arquivo in pasta_ouro_MMSS:

    with open(nome_arquivo, 'r') as ouro_MMSS:

        for i in ouro_MMSS.readlines():

            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            abd_ombro_direito_ouro.append(float(coluna[2]))


            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_ouro.append(float(coluna[8]))


            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
            flexao_cotov_direito_ouro.append(float(coluna[4]))

            
            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            flexao_cotov_esquerdo_ouro.append(float(coluna[6]))


            ## --------------- FLEXAO OMBRO DIREITO ------------------------ ##
            flexao_ombro_direito_ouro.append(float(coluna[10]))


            ## --------------- FLEXAO OMBRO ESQUERDO ---------------- ##
            flexao_ombro_esquerdo_ouro.append(float(coluna[12]))


##############################################################################################

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_VIDEO_FRONTAL (30 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_frontal_MMSS:

    with open(nome_arquivo, 'r') as video_MMSS:

        
        for i in video_MMSS.readlines():
            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            abd_ombro_direito_video_frontal.append(float(coluna[2]))
            

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_video_frontal.append(float(coluna[4]))

            
            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
            flexao_cotov_direito_video_frontal.append(float(coluna[6]))


            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            flexao_cotov_esquerdo_video_frontal.append(float(coluna[8]))
            

            ## --------------- FLEXAO OMBRO DIREITO ----------------------- ##
            flexao_ombro_direito_video_frontal.append(float(coluna[10]))
       
            ## --------------- FLEXAO OMBRO ESQUERDO ---------------------- ##
            flexao_ombro_esquerdo_video_frontal.append(float(coluna[12]))
        


# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO MMSS_VIDEO_LATERAL (60 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_lateral_MMSS:
    
    with open(nome_arquivo, 'r') as video_MMSS:

        for i in video_MMSS.readlines():
            coluna = i.strip().split('\t')

            ## --------------- ABD OMBRO DIREITO -------------------- ##
            abd_ombro_direito_video_lateral.append(float(coluna[2]))
            

            ## --------------- ABD OMBRO ESQUERDO -------------------- ##
            abd_ombro_esquerdo_video_lateral.append(float(coluna[4]))

        
            ## --------------- FLEXÃO COTOVELO DIREITO -------------------- ##
            flexao_cotov_direito_video_lateral.append(float(coluna[6]))


            ## --------------- FLEXÃO COTOVELO ESQUERDO -------------------- ##
            flexao_cotov_esquerdo_video_lateral.append(float(coluna[8]))


            ## --------------- FLEXAO OMBRO DIREITO ---------------- ##
            flexao_ombro_direito_video_lateral.append(float(coluna[10]))


            ##---------------- FLEXAO OMBRO ESQUERDO ---------------- ##
            flexao_ombro_esquerdo_video_lateral.append(float(coluna[12]))


################################################################################################################
################################################################################################################
#                                   COLUNA

# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_OURO
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_ouro_COLUNA:

    with open(nome_arquivo, 'r') as coluna_ouro:

        for i in coluna_ouro.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            flexao_cabeca_ouro.append(float(coluna[1]))


            ## ----------- FLEXAO TRONCO -------------- ##
            flexao_tronco_ouro.append(float(coluna[3]))

            ## ----------- ROTACAO TRONCO -------------- ##
            rotacao_tronco_ouro.append(float(coluna[5]))



# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_VIDEO FRONTAL (60 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_frontal_COLUNA:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            flexao_cabeca_video_frontal.append(float(coluna[1]))


            ## ----------- FLEXAO TRONCO -------------- ##
            flexao_tronco_video_frontal.append(float(coluna[3]))


            ## ----------- ROTACAO TRONCO -------------- ##
            rotacao_tronco_video_frontal.append(float(coluna[5]))




# PERCORRENDO A PASTA QUE CONTEM OS ARQUIVOS DO COLUNA_VIDEO lateral (30 FRAMES)
# E SALVANDO NAS LISTAS OS ANGULOS
for nome_arquivo in pasta_video_lateral_COLUNA:

    with open(nome_arquivo, 'r') as coluna_video:

        for i in coluna_video.readlines():

            coluna = i.strip().split('\t')

            ## ----------- FLEXAO CABECA -------------- ##
            flexao_cabeca_video_lateral.append(float(coluna[1]))


            ## ----------- FLEXAO TRONCO -------------- ##
            flexao_tronco_video_lateral.append(float(coluna[3]))


            ## ----------- ROTACAO TRONCO -------------- ##
            rotacao_tronco_video_lateral.append(float(coluna[5]))



################ ------- ERRO MEDIO ABSOLUTO ------- ######################

#-------------------------- MMSS ------------------------------------ #
# ABDUÇÃO OMBRO DIREITO

erro_abd_ombro_direito_ouro_frontal = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_frontal)
erro_abd_ombro_direito_ouro_lateral = erro_medio_absoluto(abd_ombro_direito_ouro, abd_ombro_direito_video_lateral)
erro_abd_ombro_direito_frontal_lateral = erro_medio_absoluto(abd_ombro_direito_video_frontal, abd_ombro_direito_video_lateral)


# ABDUÇÃO OMBRO ESQUERDO

erro_abd_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
erro_abd_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
erro_abd_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(abd_ombro_esquerdo_video_frontal, abd_ombro_esquerdo_video_lateral)


# FLEXÃO OMBRO DIREITO

erro_flex_ombro_direito_ouro_frontal = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_frontal)
erro_flex_ombro_direito_ouro_lateral = erro_medio_absoluto(flexao_ombro_direito_ouro, flexao_ombro_direito_video_lateral)
erro_flex_ombro_direito_frontal_lateral = erro_medio_absoluto(flexao_ombro_direito_video_frontal, flexao_ombro_esquerdo_video_lateral)


# FLEXÃO OMBRO ESQUERDO

erro_flex_ombro_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_frontal)
erro_flex_ombro_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_lateral)
erro_flex_ombro_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_ombro_esquerdo_video_frontal, flexao_ombro_esquerdo_video_lateral)

# FLEXÃO COTOVELO DIREITO

erro_flex_cot_direito_ouro_frontal = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_frontal)
erro_flex_cot_direito_ouro_lateral = erro_medio_absoluto(flexao_cotov_direito_ouro, flexao_cotov_direito_video_lateral)
erro_flex_cot_direito_frontal_lateral = erro_medio_absoluto(flexao_cotov_direito_video_frontal, flexao_cotov_direito_video_lateral)

# FLEXÃO COTOVELO ESQUERDO

erro_flex_cot_esquerdo_ouro_frontal = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_frontal)
erro_flex_cot_esquerdo_ouro_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_lateral)
erro_flex_cot_esquerdo_frontal_lateral = erro_medio_absoluto(flexao_cotov_esquerdo_video_frontal, flexao_cotov_esquerdo_video_lateral)


movimento_ouro_MMSS =  [abd_ombro_direito_ouro, abd_ombro_esquerdo_ouro, flexao_ombro_direito_ouro, 
                    flexao_ombro_esquerdo_ouro, flexao_cotov_direito_ouro, flexao_cotov_esquerdo_ouro]

movimento_frontal_MMSS = [abd_ombro_direito_video_frontal, abd_ombro_esquerdo_video_frontal, flexao_ombro_direito_video_frontal, 
                    flexao_ombro_esquerdo_video_frontal, flexao_cotov_direito_video_frontal, flexao_cotov_esquerdo_video_frontal]

movimento_lateral_MMSS = [abd_ombro_direito_video_lateral, abd_ombro_esquerdo_video_lateral, flexao_ombro_direito_video_lateral, 
                    flexao_ombro_esquerdo_video_lateral, flexao_cotov_direito_video_lateral, flexao_cotov_esquerdo_video_lateral]




amplitude_frontal_MMSS = []
amplitude_lateral_MMSS = []
amplitude_ouro_MMSS = []

for i in movimento_ouro_MMSS:
    amplitude_ouro_MMSS.append(max(i) - min(i))

for i in movimento_frontal_MMSS:
    amplitude_frontal_MMSS.append(max(i) - min(i))

for i in movimento_lateral_MMSS:
    amplitude_lateral_MMSS.append(max(i) - min(i))


#------------------------------- COLUNA ---------------------------------------#

# FLEXÃO CABEÇA

erro_flex_cabeca_ouro_frontal = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
erro_flex_cabeca_ouro_lateral = erro_medio_absoluto(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
erro_flex_cabeca_frontal_lateral = erro_medio_absoluto(flexao_cabeca_video_frontal, flexao_cabeca_video_lateral)


# FLEXÃO TRONCO

erro_flex_tronco_ouro_frontal = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_frontal)
erro_flex_tronco_ouro_lateral = erro_medio_absoluto(flexao_tronco_ouro, flexao_tronco_video_lateral)
erro_flex_tronco_frontal_lateral = erro_medio_absoluto(flexao_tronco_video_frontal, flexao_tronco_video_lateral)


# ROTAÇÃO TRONCO

erro_rot_tronco_ouro_frontal = erro_medio_absoluto(rotacao_tronco_ouro, rotacao_tronco_video_frontal)
erro_rot_tronco_ouro_leteral = erro_medio_absoluto(rotacao_tronco_ouro, rotacao_tronco_video_lateral)
erro_rot_tronco_frontal_lateral = erro_medio_absoluto(rotacao_tronco_video_frontal, rotacao_tronco_video_lateral)

movimento_ouro_COLUNA = [flexao_cabeca_ouro, flexao_tronco_ouro, rotacao_tronco_ouro]
movimento_frontal_COLUNA = [flexao_cabeca_video_frontal, flexao_tronco_video_frontal, rotacao_tronco_video_frontal]
movimento_lateral_COLUNA = [flexao_cabeca_video_lateral, flexao_tronco_video_lateral, rotacao_tronco_video_lateral]


amplitude_ouro_COLUNA = []
amplitude_frontal_COLUNA = []
amplitude_lateral_COLUNA = []

for i in movimento_ouro_COLUNA:
    amplitude_ouro_COLUNA.append(max(i) - min(i))

for i in movimento_frontal_COLUNA:
    amplitude_frontal_COLUNA.append(max(i) - min(i))

for i in movimento_lateral_COLUNA:
    amplitude_lateral_COLUNA.append(max(i) - min(i))

#dois primeiros = MMSS; depois COLUNA
erro_medio_geral = []
correlacao_geral = []
compare_ouro_video = [amplitude_lateral_MMSS, amplitude_frontal_MMSS, amplitude_lateral_COLUNA, amplitude_frontal_COLUNA]

count = 0
for i in compare_ouro_video:
    if(count <= 1):
        erro_medio_geral.append(erro_medio_absoluto(amplitude_ouro_MMSS, i))
        correlacao_geral.append(correlacao(amplitude_ouro_MMSS, i))
    else:
        erro_medio_geral.append(erro_medio_absoluto(amplitude_ouro_COLUNA, i))
        correlacao_geral.append(correlacao(amplitude_ouro_COLUNA, i))
    count+= 1

erro_medio_geral.append(erro_medio_absoluto(compare_ouro_video[0], compare_ouro_video[1]))
erro_medio_geral.append(erro_medio_absoluto(compare_ouro_video[2], compare_ouro_video[3]))

correlacao_geral.append(correlacao(compare_ouro_video[0], compare_ouro_video[1]))
correlacao_geral.append(correlacao(compare_ouro_video[2], compare_ouro_video[3]))



############### ------- CORRELAÇÃO -------------- ####################

#------------------ MMSS ------------------------- #

# ABDUÇÃO OMBRO DIREITO

corr_abd_ombro_direito_ouro_frontal = correlacao(abd_ombro_direito_ouro, abd_ombro_direito_video_frontal)
corr_abd_ombro_direito_ouro_lateral = correlacao(abd_ombro_direito_ouro, abd_ombro_direito_video_lateral)
corr_abd_ombro_direito_frontal_lateral = correlacao(abd_ombro_direito_video_frontal, abd_ombro_direito_video_lateral)

# ABDUÇÃO OMBRO ESQUERDO

corr_abd_ombro_esquerdo_ouro_frontal = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_frontal)
corr_abd_ombro_esquerdo_ouro_lateral = correlacao(abd_ombro_esquerdo_ouro, abd_ombro_esquerdo_video_lateral)
corr_abd_ombro_esquerdo_frontal_lateral = correlacao(abd_ombro_esquerdo_video_frontal, abd_ombro_esquerdo_video_lateral)

# FLEXÃO OMBRO DIREITO

corr_flex_ombro_direito_ouro_frontal = correlacao(flexao_ombro_direito_ouro, flexao_ombro_direito_video_frontal)
corr_flex_ombro_direito_ouro_lateral = correlacao(flexao_ombro_direito_ouro, flexao_ombro_direito_video_lateral)
corr_flex_ombro_direiro_frontal_lateral = correlacao(flexao_ombro_direito_video_frontal, flexao_ombro_direito_video_lateral)

# FLEXÃO OMBRO ESQUERDO

corr_flex_ombro_esquerdo_ouro_frontal = correlacao(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_frontal)
corr_flex_ombro_direito_ouro_lateral = correlacao(flexao_ombro_esquerdo_ouro, flexao_ombro_esquerdo_video_lateral)
corr_flex_ombro_direiro_frontal_lateral = correlacao(flexao_ombro_esquerdo_video_frontal, flexao_ombro_esquerdo_video_lateral)

# FLEXAO COTOVELO DIREITO

corr_flex_cot_direito_ouro_frontal = correlacao(flexao_cotov_direito_ouro, flexao_cotov_direito_video_frontal)
corr_flex_cot_direito_ouro_lateral = correlacao(flexao_cotov_direito_ouro, flexao_cotov_direito_video_lateral)
corr_flex_cot_direito_frontal_lateral = correlacao(flexao_cotov_direito_video_frontal, flexao_cotov_direito_video_lateral)


# FLEXAO COTOVELO ESQUERDO

corr_flex_cot_esquerdo_ouro_frontal = correlacao(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_frontal)
corr_flex_cot_esquerdo_ouro_lateral = correlacao(flexao_cotov_esquerdo_ouro, flexao_cotov_esquerdo_video_lateral)
corr_flex_cot_esquerdo_frontal_lateral = correlacao(flexao_cotov_esquerdo_video_frontal, flexao_cotov_esquerdo_video_lateral)


max_ouro_MMSS = []
min_ouro_MMSS = []

max_frontal_MMSS = []
min_frontal_MMSS = []

max_lateral_MMSS = []
min_lateral_MMSS = []

max_ouro_COLUNA = []
min_ouro_COLUNA = []

max_frontal_COLUNA = []
min_frontal_COLUNA = []

max_lateral_COLUNA = []
min_lateral_COLUNA = []



for o_MMSS, f_MMSS, l_MMSS, o_COLUNA, f_COLUNA, l_COLUNA in movimento_ouro_MMSS, movimento_frontal_MMSS, movimento_lateral_MMSS, movimento_ouro_COLUNA, movimento_frontal_COLUNA, movimento_lateral_COLUNA:
    max_ouro_MMSS.append(max(o_MMSS))
    min_ouro_MMSS.append(min(o_MMSS))

    max_frontal_MMSS.append(max(f_MMSS))
    min_frontal_MMSS.append(min(f_MMSS))

    max_lateral_MMSS.append(max(l_MMSS))
    min_frontal_MMSS.append(min(l_MMSS))

    max_ouro_COLUNA.append(max(o_COLUNA))
    min_ouro_COLUNA.append(min(o_COLUNA))

    max_frontal_COLUNA.append(max(f_COLUNA))
    min_frontal_COLUNA.append(min(f_COLUNA))

    max_lateral_COLUNA.append(max(l_COLUNA))
    min_frontal_COLUNA.append(min(l_COLUNA))


# correlacao entre os angulos maximos de todas as variaveis de MMSS
corr_max_ouro_frontal = correlacao(max_ouro_MMSS, max_frontal_MMSS)
corr_min_ouro_frontal = correlacao(min_ouro_MMSS, min_frontal_MMSS)

corr_max_ouro_lateral = correlacao(max_ouro_MMSS, max_lateral_MMSS)
corr_min_ouro_lateral = correlacao(min_ouro_MMSS, min_lateral_MMSS)

corr_max_frontal_lateral = correlacao(max_frontal_MMSS, max_lateral_MMSS)
corr_min_frontal_lateral = correlacao(min_frontal_MMSS, min_lateral_MMSS)

# correlacao entre os angulos maximos de todas as variaveis de COLUNA
corr_max_ouro_frontal = correlacao(max_ouro_COLUNA, max_frontal_COLUNA)
corr_min_ouro_frontal = correlacao(min_ouro_COLUNA, min_frontal_COLUNA)

corr_max_ouro_lateral = correlacao(max_ouro_COLUNA, max_lateral_COLUNA)
corr_min_ouro_lateral = correlacao(min_ouro_COLUNA, min_lateral_COLUNA)

corr_max_frontal_lateral = correlacao(max_frontal_COLUNA, max_lateral_COLUNA)
corr_min_frontal_lateral = correlacao(min_frontal_COLUNA, min_lateral_COLUNA)

#-------------------- COLUNA ------------------------- #

# FLEXAO CABEÇA

corr_flexao_cabeca_ouro_frontal = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_frontal)
corr_flexao_cabeca_ouro_lateral = correlacao(flexao_cabeca_ouro, flexao_cabeca_video_lateral)
corr_flexao_cabeca_frontal_lateral = correlacao(flexao_cabeca_video_frontal, flexao_cabeca_video_lateral)

# FLEXAO TRONCO

corr_flexao_tronco_ouro_frontal = correlacao(flexao_tronco_ouro, flexao_tronco_video_frontal)
corr_flexao_tronco_ouro_lateral = correlacao(flexao_tronco_ouro, flexao_tronco_video_lateral)
corr_flexao_tronco_frontal_lateral = correlacao(flexao_tronco_video_frontal, flexao_tronco_video_lateral)

# ROTAÇÃO TRONCO

corr_rot_tronco_ouro_frontal = correlacao(rotacao_tronco_ouro, rotacao_tronco_video_frontal)
corr_rot_tronco_ouro_lateral = correlacao(rotacao_tronco_ouro, rotacao_tronco_video_lateral)
corr_rot_tronco_frontal_lateral = correlacao(rotacao_tronco_video_frontal, rotacao_tronco_video_lateral)








