import pyautogui
import time


time.sleep(5)
def enviar_script(script_text):
    lines = [line.strip() for line in script_text.splitlines() if line.strip()]
    
    for line in lines:
        print(f"Enviando: {line}")
        pyautogui.typewrite(line, interval=0.1)
        pyautogui.press("enter")
        time.sleep(1)  # Pequeno delay para evitar problemas

script ="""

De acordo com todas as leis conhecidas da aviação, não há como uma abelha voar. 
Suas asas são muito pequenas para tirar seu corpinho gordo do chão. 
A abelha, é claro, voa de qualquer maneira porque as abelhas não se importam com o que os humanos acham impossível. 
Amarelo, preto. Amarelo, preto. Amarelo, preto. Amarelo, preto. 
Ooh, preto e amarelo! 
Vamos agitar um pouco. 
Barry! O café da manhã está pronto! 
Chegando! 
Espere um segundo. 
Alô? 
Barry? 
Adam? 
Você acredita que isso está acontecendo? 
Eu não acredito. 
Vou buscá-lo. 
Parecendo afiado. 
Use as escadas, Seu pai pagou um bom dinheiro por elas. 
Desculpe. Estou animado. 
Aqui está o formando. 
Estamos muito orgulhosos de você, filho. 
Um boletim perfeito, tudo B's. 
Muito orgulhoso. 
Mãe! Eu tenho uma coisa acontecendo aqui. 
Você tem fiapos no seu pelo. 
Ai! Sou eu! 
Acene para nós! Estaremos na fileira 118.000. 
Tchau! 
Barry, eu disse a você, pare de voar dentro de casa! 
Ei, Adam. 
Ei, Barry. 
Isso é gel de pelos? 
Um pouco. Dia especial, formatura. 
Nunca pensei que conseguiria. 
Três dias de escola primária, três dias de ensino médio. 
Esses foram estranhos. 
Três dias de faculdade. Ainda bem que tirei um dia e peguei carona por The Hive. 
Você voltou diferente. 
Oi, Barry. Artie, deixando o bigode crescer? Parece bom. 
Ouviu sobre Frankie? 
Sim. 
Você vai ao funeral? 
Não, eu não vou. 
Todo mundo sabe, se picar alguém, você morre. 
Não desperdice com um esquilo. 
Que cabeça quente. 
Acho que ele poderia ter saído do caminho. 
Adoro incorporar um parque de diversões ao nosso dia. 
É por isso que não precisamos de férias. 
Rapaz, muita pompa nessas circunstâncias. 
Bem, Adam, hoje somos homens. 
Somos! 
Homens-abelha. 
Amém! 
Aleluia! 
Alunos, professores, abelhas ilustres, 
por favor, deem as boas-vindas ao reitor Buzzwell. Bem- 
vindos, turma de formatura de New Hive City, das 9h15. 
Isso conclui nossas cerimônias E começa sua carreira na Honex Industries! 
Vamos escolher nosso trabalho hoje? 
Ouvi dizer que é só orientação. 
Atenção! Aqui vamos nós. 
Mantenha suas mãos e antenas dentro do bonde o tempo todo. 
Quer saber como será? 
Um pouco assustador. 
Bem-vindo à Honex, uma divisão da Honesco e parte do Hexagon Group. 
É isso! 
Uau.
Sabemos que você, como abelha, trabalhou a vida inteira para chegar ao ponto em que pode trabalhar a vida inteira. 
O mel começa quando nossos valentes Pollen Jocks trazem o néctar para The Hive. 
Nossa fórmula ultrassecreta é automaticamente corrigida em cores, ajustada em aromas e contornada por bolhas neste xarope doce e calmante com seu brilho dourado característico que você conhece como... Mel! 
Aquela garota era gostosa. 
Ela é minha prima! 
Ela é? 
Sim, somos todos primos. 
Certo. Você está certo. 
Na Honex, nos esforçamos constantemente para melhorar todos os aspectos da existência das abelhas. 
Essas abelhas estão testando uma nova tecnologia de capacete. 
O que você acha que ele faz? 
Não o suficiente. 
Aqui temos nosso mais recente avanço, o Krelman. 
O que ele faz? 
Captura aquele pequeno fio de mel que fica pendurado depois que você o despeja. 
Economiza milhões para nós. 
Alguém pode trabalhar no Krelman? 
Claro. A maioria dos trabalhos das abelhas são pequenos. 
Mas as abelhas sabem que cada pequeno trabalho, se bem feito, significa muito. 
Mas escolha com cuidado porque você vai ficar no emprego que escolheu pelo resto da vida. 
O mesmo emprego pelo resto da vida? Eu não sabia disso. 
Qual é a diferença? 
Você ficará feliz em saber que as abelhas, como espécie, não tiveram um dia de folga em 27 milhões de anos. 
Então você vai nos fazer trabalhar até a morte? 
Nós certamente tentaremos. 
Uau! Isso me surpreendeu! 
"Qual é a diferença?" 
Como você pode dizer isso? 
Um emprego para sempre? 
Essa é uma escolha insana de se fazer. 
Estou aliviado. Agora só temos que tomar uma decisão na vida. 
Mas, Adam, como eles nunca nos disseram isso? 
Por que você questionaria alguma coisa? Nós somos abelhas. 
Somos a sociedade mais perfeitamente funcional da Terra. 
Você já pensou que talvez as coisas funcionem um pouco bem demais aqui? 
Tipo o quê? Dê-me um exemplo. om todas as leis conhecidas
Eu não sei. Mas você sabe do que estou falando. 
Por favor, limpe o portão. Royal Nectar Force se aproximando. 
Espere um segundo. Confira. 
Ei, esses são os Pollen Jocks! 
Uau. 
Nunca os vi tão de perto. 
Eles sabem como é fora da Colmeia. 
Sim, mas alguns não voltam. 
Ei, Jocks! 
Oi, Jocks! 
Vocês foram ótimos! 
Vocês são monstros! 
Vocês são aberrações do céu! Eu amei! Eu amei! 
Eu me pergunto onde eles estavam. 
Eu não sei. 
O dia deles não é planejado. 
Fora da Colmeia, voando sabe-se lá para onde, fazendo sabe-se lá o quê. 
Você não pode simplesmente decidir ser um Pollen Jock. Você tem que ser criado para isso.
Olha. Isso é mais pólen do que você e eu veremos em uma vida inteira. 
É só um símbolo de status. 
As abelhas fazem muito disso. 
Talvez. A menos que você esteja usando e as mulheres vejam você usando. 
Essas mulheres? 
Elas não são nossas primas também? 
Distante. Distante. 
Olhe para esses dois. 
Um casal de Hive Harrys. 
Vamos nos divertir com eles. 
Deve ser perigoso ser um Pollen Jock. 
Sim. Uma vez um urso me prendeu contra um cogumelo! 
Ele tinha uma pata na minha garganta e, com a outra, estava me dando um tapa! 
Oh, meu Deus! 
Nunca pensei que o nocautearia. 
O que você estava fazendo durante isso? 
Tentando alertar as autoridades. 
Posso autografar isso. 
Um pouco tempestuoso lá fora hoje, não é, camaradas? 
Sim. Tempestuoso. 
Vamos atingir um canteiro de girassóis a seis milhas daqui amanhã. 
Seis milhas, hein? 
Barry! 
Um salto de poça para nós, mas talvez você não esteja a fim. 
Talvez eu esteja. 
Você não está! 
Vamos às 09:00 no J-Gate. 
O que você acha, buzzy-boy? 
Você é abelha o suficiente? 
Talvez eu seja. Tudo depende do que 09:00 significa. 
Ei, Honex! 
Pai, você me surpreendeu. 
Você decide no que está interessado? 
Bem, há muitas escolhas. 
Mas você só tem uma. 
Você já ficou entediado fazendo o mesmo trabalho todos os dias? 
Filho, deixe-me falar sobre mexer. 
Você pega aquele palito, e simplesmente o move, e mexe. 
Você entra em um ritmo. 
É uma coisa linda. 
Sabe, pai, quanto mais penso sobre isso, 
talvez o campo de mel não seja o certo para mim. 
Você estava pensando em quê, fazer animais de balão? 
Esse é um trabalho ruim para um cara com um ferrão. 
Janet, seu filho não tem certeza se quer entrar no ramo do mel! 
Barry, você é tão engraçado às vezes. 
Eu não estou tentando ser engraçado. 
Você não é engraçado! Você está entrando no ramo do mel. Nosso filho, o mexedor! 
Você vai ser um agitador? 
Ninguém está me ouvindo! 
Espere até ver os gravetos que eu tenho. 
Eu poderia dizer qualquer coisa agora. 
Vou fazer uma tatuagem de formiga! 
Vamos abrir um pouco de mel e comemorar! 
Talvez eu fure meu tórax. Raspe minhas antenas. Morar com um gafanhoto. Ganhe um dente de ouro e chame todo mundo de "cara"! 
Estou tão orgulhoso. 
Estamos começando a trabalhar hoje! 
Hoje é o dia. 
Vamos! Todos os bons empregos vão acabar. 
Sim, certo. 
Contagem de pólen, abelha dublê, despejar, agitador, recepção, remoção de pelos...
Ainda está disponível?
Espere. Restam dois! 
Um deles é seu! Parabéns! 
Afaste-se. 
O que você conseguiu? 
Tirando sujeira. Estelar! 
Uau! 
Dois novatos? 
Sim, senhor! Nosso primeiro dia! Estamos prontos! 
Faça sua escolha. 
Você quer ir primeiro? 
Não, você vai. 
Oh, meu Deus. O que está disponível? 
O atendente do banheiro está aberto, não pelo motivo que você pensa. 
Alguma chance de pegar o Krelman? 
Claro, você está dentro. 
Desculpe, o Krelman acabou de fechar. 
O macaco de cera está sempre aberto. 
O Krelman abriu novamente. 
O que aconteceu? 
Uma abelha morreu. Abre uma abertura. Viu? Ele está morto. Outro morto. 
Morto. Morto. Mais dois mortos. 
Morto do pescoço para cima. Morto do pescoço para baixo. É a vida! 
Oh, isso é tão difícil! 
Aquecimento, resfriamento, abelha dublê, despejador, agitador, zumbido, inspetor número sete, coordenador de fiapos, supervisor de listras, domador de ácaros. 
Barry, o que você acha que eu deveria... Barry? 
Barry! 
Tudo bem, temos o canteiro de girassóis no quadrante nove... 
O que aconteceu com você? 
Onde você está? 
Vou sair. 
Sair? Sair para onde? 
Lá fora. 
Ah, não! 
Tenho que sair, antes de ir trabalhar pelo resto da minha vida. 
Você vai morrer! Você é louco! Alô? 
Outra ligação chegando. 
Se alguém estiver se sentindo corajoso, tem uma delicatessen coreana na 83rd que recebe suas rosas hoje. 
Ei, pessoal. 
Olhem isso. 
Não é o garoto que vimos ontem? 
Calma, filho, o convés de voo está restrito. 
Tudo bem, Lou. Vamos levá-lo para cima. 
Sério? Está se sentindo com sorte, não é? 
Assine aqui, aqui. Apenas coloque suas iniciais. 
Obrigado. 
OK. 
Você tem um aviso de chuva hoje e, como todos sabem, abelhas não voam na chuva. 
Então, tomem cuidado. Como sempre, tomem cuidado com suas vassouras, tacos de hóquei, cães, pássaros, ursos e morcegos. 
Também recebi alguns relatos de root beer sendo despejados em nós. 
Murphy está em um asilo por causa disso, balbuciando como uma cigarra! 
Isso é horrível. 
E um lembrete para vocês, novatos, lei das abelhas número um, absolutamente nada de falar com humanos! 
 Tudo bem, posições de lançamento! 
Zumbido, zumbido, zumbido! Zumbido, zumbido, zumbido, zumbido! Zumbido, zumbido, zumbido, zumbido! 
Preto e amarelo! 
Olá! 
Você está pronto para isso, figurão? 
Sim. Sim, vamos lá. 
Vento, certo. 
Antenas, certo. 
Pacote de néctar, certo. 
Asas, certo. 
Ferrão, certo. 
Assustado até a morte, certo. 
OK, moças, 
vamos lá!
Bata nessas petúnias, seus sugadores de caule listrados! 
Todos vocês, drenem essas flores! 
Uau! Estou fora! 
Não acredito que estou fora! 
Tão azul. 
Sinto-me tão rápido e livre! 
Pipa-caixa! 
Uau! 
Flores! 
Este é o Líder Azul, Temos um visual de rosas. 
Traga-o em torno de 30 graus e segure. 
Rosas! 
30 graus, entendido. Trazendo-o ao redor. 
Fique de lado, garoto. 
Tem um pouco de um chute. 
Esse é um coletor de néctar! 
Já viu a polinização de perto? 
Não, senhor. 
Pego um pouco de pólen aqui, espalho aqui. Talvez uma pitada ali, uma pitada naquele. 
Viu isso? É um pouco de mágica. 
Isso é incrível. Por que fazemos isso? 
Esse é o poder do pólen. Mais pólen, mais flores, mais néctar, mais mel para nós. 
Legal. 
Estou pegando muito amarelo brilhante, Podem ser margaridas, Não precisamos delas? 
Copie esse visual. 
Espere. Uma dessas flores parece estar se movendo. 
Diga de novo? Você está relatando uma flor se movendo? 
Afirmativo. 
Isso estava na linha! 
Isso é o mais legal. O que é? 
Eu não sei, mas estou amando essa cor. 
Tem um cheiro bom. 
Não como uma flor, mas eu gosto. 
Sim, felpudo. 
Químico. 
Cuidado, rapazes. É um pouco pegajoso. 
Meu doce senhor das abelhas! 
Cérebro de doce, saia daí! 
Problema! 
Rapazes! 
Isso pode ser ruim. 
Afirmativo. 
Muito perto. 
Vai doer. 
O garotinho da mamãe. 
Você está muito fora de posição, novato! 
Vindo em sua direção como um míssil! 
Me ajude! 
Eu não acho que essas são flores. 
Devemos contar a ele? 
Acho que ele sabe. 
O que é isso?! 
Ponto de partida! 
Você pode começar a fazer as malas, querida, porque você está prestes a comê-lo! 
Uau! 
Nojento. 
Tem uma abelha no carro! 
Faça alguma coisa! 
Estou dirigindo! 
Oi, abelha. 
Ele está aqui de volta! 
Ele vai me picar! 
Ninguém se mexe. Se você não se mexer, ele não vai picar você. Parado! 
Ele piscou! 
Borrife nele, vovó! 
O que você está fazendo?! 
Uau... o nível de tensão aqui fora é inacreditável. 
Tenho que ir para casa. 
Não posso voar na chuva. Não posso voar na chuva. Não posso voar na chuva. 
Mayday! Mayday! Abelha caindo! 
Ken, você pode fechar a janela, por favor? 
Ken, você pode fechar a janela, por favor? 
Ah, não. Mais humanos. Eu não preciso disso. 
O que foi isso?
Talvez dessa vez. Dessa vez. Dessa vez! Dessa vez! Dessa vez! Isso... Cortinas! 
Isso é diabólico. 
É fantástico. Tem todas as minhas habilidades especiais, até meus dez filmes favoritos. 
Qual é o número um? Star Wars? 
Não, eu não curto esse tipo de coisa. 
Não é de se espantar que não devamos falar com eles. Eles estão loucos. 
Quando saio de uma entrevista de emprego, eles ficam espantados, não conseguem acreditar no que eu digo. 
Tem o sol. Talvez seja uma saída. 
Não me lembro do sol ter um grande 75 graus. 
Eu previ o aquecimento global. Eu podia sentir que estava ficando mais quente. No começo, pensei que era só eu. 
Espere! Pare! Abelha! 
Afaste-se. Essas são botas de inverno. 
Espere! 
Não o mate! 
Você sabe que sou alérgico a elas! Essa coisa pode me matar! 
Por que a vida dele tem menos valor que a sua? 
Por que a vida dele tem menos valor que a minha? Essa é sua afirmação? 
Só estou dizendo que toda vida tem valor. Você não sabe o que ele é capaz de sentir. 
Meu folheto! 
Aí está, rapazinho. 
Não tenho medo dele. É uma coisa alérgica. 
 Coloque isso no seu folheto de currículo. 
Meu rosto inteiro pode inchar. 
Faça disso uma de suas habilidades especiais. 
Nocautear alguém também é uma habilidade especial. 
Certo. Tchau, Vanessa. Obrigada. 
Vanessa, semana que vem? Noite de iogurte? 
Claro, Ken. Você sabe, tanto faz. 
Você poderia colocar chips de alfarroba aí. 
Tchau. 
Supostamente tem menos calorias. 
Tchau. 
Tenho que dizer algo. Ela salvou minha vida. Tenho que dizer algo. 
Tudo bem, aqui vai. 
Não. 
O que eu diria? 
Eu poderia realmente ter problemas. É uma lei das abelhas. Você não deve falar com um humano. 
Não acredito que estou fazendo isso. Tenho que fazer. 
Ah, não consigo. Vamos lá! 
Não. Sim. Não. Faça. Não consigo. 
Como devo começar? "Você gosta de jazz?" Não, isso não é bom. 
Lá vem ela! Fala, seu idiota! 
Oi! 
Desculpa. Você está falando. 
Sim, eu sei. 
Você está falando! 
Desculpa mesmo. 
Não, está tudo bem. Está tudo bem. 
Sei que estou sonhando. Mas não me lembro de ter ido dormir. 
Bem, tenho certeza de que isso é muito desconcertante. 
É uma surpresa para mim. Quer dizer, você é uma abelha! 
Eu sou. E eu não deveria estar fazendo isso, mas todos estavam tentando me matar. 
E se não fosse por você... Eu tinha que te agradecer. É assim que fui criado. 
Isso foi um pouco estranho. Estou falando com uma abelha.
Estou falando com uma abelha. E a abelha está falando comigo! 
Vou embora agora.
Espera! Como você aprendeu a fazer isso? 
O quê? 
A coisa de falar. 
Do mesmo jeito que você fez, eu acho. "Mamãe, papai, querida." Você pega. 
Isso é muito engraçado. 
Sim. 
Abelhas são engraçadas. Se não ríssemos, choraríamos com o que temos que lidar. 
De qualquer forma... Posso... te dar alguma coisa? 
Tipo o quê? 
Não sei. Quer dizer... não sei. Café? 
Não quero te incomodar. 
Não é problema. Leva dois minutos. 
É só café. 
Odeio me impor. 
Não seja ridícula! 
Na verdade, eu adoraria uma xícara. 
Ei, você quer bolo de rum? 
Eu não deveria. 
Tome um pouco. 
Não, não posso. 
Vamos! 
Estou tentando perder alguns microgramas. 
Onde? 
Essas listras não ajudam. 
Você está ótima! 
Não sei se você entende de moda. 
Você está bem? 
Não. 
Ele está fazendo a gravata no táxi enquanto voam para Madison. 
Ele finalmente chega lá. 
Ele sobe correndo os degraus da igreja. 
O casamento está acontecendo. 
E ele diz: "Melancia? 
Achei que você tivesse dito guatemalteca. 
Por que eu me casaria com uma melancia?" 
Isso é uma piada de abelha? 
Esse é o tipo de coisa que fazemos. 
Sim, diferente. 
Então, o que você vai fazer, Barry? 
Sobre o trabalho? Não sei. 
Quero fazer a minha parte pela Colmeia, mas não posso fazer do jeito que eles querem. 
Sei como você se sente. 
Sabe? 
Claro. 
Meus pais queriam que eu fosse advogada ou médica, mas eu queria ser florista. 
Sério? 
Meu único interesse são flores. 
Nossa nova rainha foi eleita com o mesmo slogan de campanha. 
De qualquer forma, se você olhar... Aí está minha colmeia. Vê? 
Você está em Sheep Meadow! 
Sim! Estou bem perto do Turtle Pond! 
De jeito nenhum! Conheço essa área. Perdi um anel de dedo lá uma vez. 
Por que as meninas colocam anéis nos dedos dos pés? 
Por que não? 
É como colocar um chapéu no seu joelho. 
Talvez eu tente isso. 
Você está bem, senhora? 
Ah, sim. Ótimo. 
Só tomando duas xícaras de café! 
De qualquer forma, isso foi ótimo. 
Obrigado pelo café. 
Sim, não é problema. 
Desculpe por não ter conseguido terminar. Se eu conseguisse, ficaria acordado o resto da minha vida. 
Você está...? 
Posso levar um pedaço disso comigo? 
Claro! Aqui, pegue uma migalha. 
Obrigado! 
Sim. 
Tudo bem. Bem, então... Acho que te vejo por aí. Ou não. 
Bem, não é nada, mas... De qualquer forma...
Isso não pode funcionar.
Ele está pronto para ir. 
Podemos muito bem tentar. 
OK, Dave, puxe o paraquedas. 
Parece incrível. 
Foi incrível! 
Foi o momento mais assustador e feliz da minha vida. 
Humanos! Não acredito que você estava com humanos! 
Humanos gigantes e assustadores! 
Como eles eram? 
Enormes e loucos. Eles falam loucamente. 
Eles comem coisas gigantes e loucas. 
Eles dirigem loucamente. 
Eles tentam te matar, como na TV? 
Alguns deles. Mas alguns deles não. 
Como você voltou? 
Poodle. 
Você fez isso, e estou feliz. Você viu o que queria ver. 
Você teve sua "experiência". Agora você pode escolher seu trabalho e ser normal. 
Bem... 
Bem? 
Bem, eu conheci alguém. 
Você conheceu? Ela era do tipo Bee-ish? 
Uma vespa?! Seus pais vão te matar! 
Não, não, não, não é uma vespa. 
Aranha? 
Eu não sou atraído por aranhas. 
Eu sei que é a coisa mais quente, com as oito pernas e tudo. Eu não consigo passar por essa cara. 
Então, quem é ela? 
Ela é... humana. 
Não, não. Essa é uma lei das abelhas. Você não quebraria uma lei das abelhas. O 
nome dela é Vanessa. 
Nossa. 
Ela é tão legal. E ela é florista! 
Ah, não! Você está namorando uma florista humana! 
Nós não estamos namorando. 
Você está voando para fora da Colmeia, falando com humanos que atacam nossas casas com lavadoras de alta pressão e M-80s! Um oitavo de uma barra de dinamite! 
Ela salvou minha vida! E ela me entende. 
Isso acabou! 
Coma isso. 
Isso não acabou! O que foi isso? 
Eles chamam de migalha. 
Era tão listrado e picante! 
E não é isso que eles comem. 
É isso que cai do que eles comem! 
Você sabe o que é um Cinnabon? 
Não. 
É pão, canela e cobertura. Eles esquentam... 
Sente-se! 
...muito quente! 
Escute-me! 
Nós não somos eles! Nós somos nós. 
Há nós e há eles! 
Sim, mas quem pode negar o coração que anseia? 
Não há anseio. Pare de ansiar. Escute-me! 
Você tem que começar a pensar abelha, meu amigo. Abelha pensante! 
Abelha pensante. 
Abelha pensante. 
Abelha pensante! Abelha pensante! Abelha pensante! Abelha pensante! 
Lá está ele. Ele está na piscina. 
Você sabe qual é o seu problema, Barry? 
Eu tenho que começar a pensar abelha? 
Quanto tempo mais isso vai durar? 
Já faz três dias! Por que você não está trabalhando? 
Que vida? Você não tem vida! 
Mataria você fazer um pouco de mel? 
Barry, saia. Seu pai está falando com você.
Martin, você falaria com ele?
Barry, estou falando com você! 
Você vem? 
Tem tudo? 
Tudo pronto! 
Vá em frente. Eu alcanço você. 
Não demore muito. 
Assista isso! 
Vanessa! 
Ainda estamos aqui. 
Eu disse para você não gritar com ele. 
Ele não responde a gritos! 
Então por que gritar comigo? 
Porque você não escuta! 
Eu não estou ouvindo isso. 
Desculpe, eu tenho que ir. 
Aonde você está indo? 
Estou me encontrando com uma amiga. 
Uma garota? É por isso que você não consegue decidir? 
Tchau. 
Só espero que ela seja do tipo Bee. 
Eles têm um grande desfile de flores todo ano em Pasadena? 
Estar no Torneio das Rosas, esse é o sonho de todo florista! 
Em um carro alegórico, cercado por flores, multidões torcendo. 
Um torneio. As rosas competem em eventos esportivos? 
Não. Tudo bem, eu tenho um. 
Por que você não voa para todos os lugares? 
É exaustivo. Por que você não corre para todos os lugares? É mais rápido. 
Sim, OK, entendi, entendi. 
Tudo bem, sua vez. 
TiVo. Você pode congelar a TV ao vivo? Isso é loucura! 
Você não tem isso? 
Temos Hivo, mas é uma doença. É uma doença horrível, horrível. 
Oh, meu Deus. 
Abelhas idiotas! 
Você deve querer picar todos esses idiotas. 
Tentamos não picar. Geralmente é fatal para nós. 
Então você tem que controlar seu temperamento. 
Com muito cuidado. 
Você chuta uma parede, sai para dar uma volta, escreve uma carta raivosa e joga fora. Trabalhe com isso como qualquer emoção: Raiva, ciúme, luxúria. 
Oh, meu Deus! Você está bem? 
Sim. 
O que há de errado com você?! 
É um bug. 
Ele não está incomodando ninguém. 
Sai daqui, seu nojento! 
O que foi isso? Um circular Pic 'N' Save? 
Sim, foi. Como você sabia? 
Parecia umas 10 páginas. Setenta e cinco é praticamente o nosso limite. 
Você realmente entendeu isso como uma ciência. 
Perdi um primo para a Vogue italiana. 
Aposto. 
O que em nome do Poderoso Hércules é isso? 
Como isso chegou aqui? Cute Bee, Golden Blossom, Ray Liotta Private Select? 
Ele é aquele ator? 
Nunca ouvi falar dele. 
Por que isso está aqui? 
Para as pessoas. Nós comemos. 
Você não tem comida suficiente? 
Bem, sim. 
Como você consegue? 
As abelhas fazem isso. 
Eu sei quem faz isso! E é difícil fazer isso! 
Há aquecimento, resfriamento, agitação. Você precisa de uma coisa Krelman inteira! 
É orgânico. 
É nosso-orgânico! 
É só mel, Barry. 
Só o quê?!
As abelhas não sabem disso! Isso é roubo! Muito roubo! 
Vocês tomaram nossas casas, escolas, hospitais! Isso é tudo que temos! 
E está em promoção?! Estou chegando ao fundo disso. 
Estou chegando ao fundo de tudo isso! 
Ei, Hector. Você está quase terminando? 
Quase. 
Ele está aqui. Eu sinto isso. 
Bem, acho que vou para casa agora e vou deixar esse mel gostoso lá fora, sem ninguém por perto. 
Você está ferrado, garoto da caixa! 
Eu sabia que tinha ouvido alguma coisa. 
Então você pode falar! 
Eu posso falar. E agora você vai começar a falar! 
De onde você tira o doce? Quem é seu fornecedor? 
Não entendo. 
Pensei que fôssemos amigos. 
A última coisa que queremos é chatear as abelhas! 
Você chegou tarde demais! Agora é nosso! 
Você, senhor, cruzou a espada errada! 
Você, senhor, vai ser o almoço da minha iguana, Ignacio! 
De onde vem o mel? Diga-me de onde! 
Fazendas de mel! Vem de Honey Farms! 
Louco! 
Que coisa horrível aconteceu aqui? 
Esses rostos, eles nunca souberam o que os atingiu. E agora 
estão na estrada para lugar nenhum! 
Apenas fique parado. 
O quê? Você não está morto? 
Eu pareço morto? Eles vão limpar qualquer coisa que se mova. Para onde você foi? 
Para Honey Farms. Estou em algo enorme aqui. 
Estou indo para o Alasca. Sangue de alce, coisa louca. Explode sua cabeça! 
Estou indo para Tacoma. 
E você? 
Ele realmente está morto. 
Tudo bem. 
Uh-oh! 
O que é isso?! 
Oh, não! 
Um limpador! Lâmina tripla! 
Lâmina tripla? 
Pule! É sua única chance, abelha! 
Por que tudo tem que 
ser tão limpo?! 
O quanto vocês precisam ver?! 
Abram os olhos! 
Coloquem a cabeça para fora da janela! 
Da NPR News em Washington, 
sou Carl Kasell. 
Mas não matem mais insetos! 
Abelha! 
Cara do sangue de alce!! 
Você ouviu alguma coisa? 
Tipo o quê? 
Tipo um gritinho. 
Desligue o rádio. 
E aí, garoto abelha? 
Ei, Blood. 
Só uma fileira de potes de mel, até onde a vista alcança. 
Uau! 
Imagino que seja para onde esse caminhão for que eles vão buscá-lo. Quer dizer, esse mel é nosso. 
As abelhas ficam firmes. Estamos todos amontoados. 
É uma comunidade unida. 
Não nós, cara. Estamos sozinhos. Cada mosquito por si. 
E se você tiver problemas? 
Garotas mosquito tentam negociar, ficam com uma mariposa, libélula. Garotas mosquito não querem mosquitos. 
Você só pode estar brincando comigo!
Mooseblood está prestes a sair do prédio! Até mais, abelha! 
Ei, pessoal! 
Mooseblood! 
Eu sabia que pegaria vocês aqui. 
Você trouxe seu canudo maluco? 
Nós o jogamos em potes, colocamos um rótulo nele e é praticamente lucro puro. 
Que lugar é esse? 
Uma abelha tem um cérebro do tamanho de uma cabeça de alfinete. 
Elas são cabeças de alfinete! 
Cabeça de alfinete. 
Dê uma olhada no novo fumante. 
Oh, legal. É esse que você quer. O Thomas 3000! 
Fumante? 
Noventa tragadas por minuto, semiautomático. O dobro de nicotina, todo o alcatrão. Algumas baforadas disso os derrubam. 
Eles fazem o mel e nós fazemos o dinheiro. 
"Eles fazem o mel e nós fazemos o dinheiro"? 
Oh, meu Deus! 
O que está acontecendo? Você está bem? 
Sim. Não dura muito tempo. 
Você sabia que está em uma colmeia falsa com paredes falsas? 
Nossa rainha foi movida para cá. Não tivemos escolha. 
Esta é sua rainha? É um homem com roupas de mulher! É uma drag queen! 
O que é isso? 
Ah, não! 
São centenas delas! 
Mel de abelha. 
Nosso mel está sendo descaradamente roubado em grande escala! 
Isso é pior do que qualquer coisa que os ursos já fizeram! Pretendo fazer alguma coisa. 
Ah, Barry, pare. 
Quem te disse que os humanos estão roubando nosso mel? Isso é um boato. 
Isso parece boato? 
Isso é uma teoria da conspiração. Essas são fotos obviamente adulteradas. Como você se meteu nisso? 
Ele está falando com humanos. 
O quê? Falando com humanos?! 
Ele tem uma namorada humana. E eles se pegam! 
Se pegam? Barry! 
Nós não. 
Você queria poder. 
De que lado você está? 
Das abelhas! 
Eu namorei um grilo uma vez em San Antonio. Essas pernas malucas me mantiveram acordado a noite toda. 
Barry, é isso que você quer fazer da sua vida? 
Eu quero fazer isso por todas as nossas vidas. Ninguém trabalha mais duro do que as abelhas! 
Pai, eu lembro de você chegando em casa tão sobrecarregado que 
suas mãos ainda estavam se mexendo. Você não conseguia parar. 
Eu lembro disso. 
Que direito eles têm sobre o nosso mel? 
Nós vivemos com duas xícaras por ano. Eles colocam no protetor labial sem motivo algum! 
Mesmo que seja verdade, o que uma abelha pode fazer? 
Picá-las onde realmente dói. 
No rosto! No olho! 
Isso doeria. 
Não. 
No nariz? Isso é mortal. 
Só há um lugar onde você pode picar os humanos, um lugar onde isso importa. 
Hive at Five, a única fonte de notícias de ação de hora em hora do The Hive. 
Chega de barbas de abelha!
Com Bob Bumble na mesa do âncora. Clima com Storm Stinger. Esportes com Buzz Larvi. E Jeanette Chung. 
Boa noite. Eu sou Bob Bumble. 
E eu sou Jeanette Ohung. 
Uma abelha de três condados, Barry Benson, pretende processar a raça humana por roubar nosso mel, embalá-lo e lucrar com ele ilegalmente! 
Amanhã à noite no Bee Larry King, teremos três ex-rainhas aqui em nosso estúdio, discutindo seu novo livro, Classy Ladies, lançado esta semana na Hexagon. 
Hoje à noite, estamos falando com Barry Benson. 
Você já pensou: "Sou uma criança do The Hive. Não posso fazer isso"? 
As abelhas nunca tiveram medo de mudar o mundo. 
E quanto a Bee Oolumbus? Bee Gandhi? Jesus? 
De onde eu sou, nunca processaríamos humanos. 
Estávamos pensando em lojas de stickball ou doces. 
Quantos anos você tem? 
A comunidade de abelhas está apoiando você neste caso, que será o julgamento do século das abelhas. 
Sabe, eles têm um Larry King no mundo humano também. 
É um nome comum. Semana que vem... 
Ele se parece com você e tem um show e suspensórios e bolinhas coloridas... 
Semana que vem... 
Óculos, citações na parte de baixo do convidado, mesmo que você tenha acabado de ouvir. 
Semana do Urso na semana que vem! Eles são assustadores, peludos e estão aqui ao vivo. 
Sempre se inclina para frente, ombros pontudos, olhos semicerrados, muito judeus. 
No tênis, você ataca no ponto fraco! 
Era minha avó, Ken. Ela tem 81 anos. 
Querida, o backhand dela é uma piada! 
Eu não vou tirar vantagem disso? 
Silêncio, por favor. 
Trabalho de verdade acontecendo aqui. 
É a mesma abelha? 
Sim, é! 
Estou ajudando-o a processar a raça humana. 
Olá. 
Olá, abelha. 
Este é o Ken. 
Sim, eu lembro de você. Timberland, tamanho dez e meio. Sola Vibram, eu acho. 
Por que ele fala de novo? 
Escute, é melhor você ir porque estamos muito ocupados trabalhando. 
Mas é a nossa noite de iogurte! 
Tchau. 
Por que a noite do iogurte é tão difícil?! 
Coitadinha. Vocês dois estão nisso há horas! 
Sim, e o Adam aqui tem sido uma grande ajuda. 
Cobertura... 
Quantos açúcares? 
Só um. Eu tento não usar a competição. 
Então por que você está me ajudando? 
As abelhas têm boas qualidades. E isso tira minha mente da loja. Em vez de flores, as pessoas estão dando buquês de balões agora. 
Eles são ótimos, se você tem três anos. 
E flores artificiais. 
Ah, essas me deixam psicótica! 
Sim, eu também. 
Ferrões tortos, polinização inútil. 
As abelhas devem odiar essas coisas falsas! 
Nada pior do que um narciso que foi consertado.
Talvez isso possa compensar um pouco. 
Esse processo é um grande negócio. 
Eu acho. 
Tem certeza de que quer prosseguir com isso? 
Tenho certeza? Quando eu terminar com os humanos, eles não poderão dizer "Querida, estou em casa" sem pagar royalties! 
É uma cena incrível aqui no centro de Manhattan, onde o mundo espera ansiosamente, porque pela primeira vez na história, ouviremos por nós mesmos se uma abelha pode realmente falar. 
No que nos metemos aqui, Barry? 
É muito grande, não é? 
Não acredito em quantos humanos não trabalham durante o dia. 
Você acha que empresas multinacionais de alimentos de bilhões de dólares têm bons advogados? 
Todo mundo precisa ficar atrás da barricada. 
Qual é o problema? 
Não sei, só fiquei com um resfriado. 
Bem, se não é a equipe das abelhas. 
Vocês, rapazes, trabalham nisso? 
Todos de pé! O Honorável Juiz Bumbleton presidindo. 
Tudo bem. O caso número 4475, 
Tribunal Superior de Nova York, 
Barry Bee Benson v. the Honey Industry está em sessão. 
Sr. Montgomery, você está representando as cinco empresas alimentícias coletivamente? 
Um privilégio. 
Sr. Benson... você está representando todas as abelhas do mundo? 
Brincadeira. Sim, Meritíssimo, estamos prontos para prosseguir. 
Sr. Montgomery, sua declaração de abertura, por favor. 
Senhoras e senhores do júri, minha avó era uma mulher simples. Nascida em uma fazenda, ela acreditava que era direito divino do homem se beneficiar da generosidade da natureza que Deus colocou diante de nós. 
Se vivêssemos no mundo de pernas para o ar que o Sr. Benson imagina, pense no que isso significaria. 
Eu teria que negociar com o bicho-da-seda pelo elástico das minhas calças! 
Abelha falante! 
Como sabemos que isso não é algum tipo de magia de Hollywood de captura de filme holográfico? 
Eles podem estar usando raios laser! Robótica! Ventriloquia! Clonagem! Pelo que sabemos, ele pode estar usando esteroides! 
Sr. Benson? 
Senhoras e senhores, não há truques aqui. Eu sou apenas uma abelha comum. O mel é muito importante para mim. É importante para todas as abelhas. Nós o inventamos! Nós o fazemos. E o protegemos com nossas vidas. 
Infelizmente, há algumas pessoas nesta sala que acham que podem tirá-lo de nós porque somos os pequenos! 
Espero que, depois que tudo isso acabar, vocês vejam como, ao tirar nosso mel, vocês não só tiram tudo o que temos, mas tudo o que somos! Gostaria que 
ele se vestisse assim o tempo todo. Que legal! 
Chame sua primeira testemunha. 
Então, Sr. Klauss Vanderhayden da Honey Farms, grande empresa que vocês têm. 
Acho que sim. 
Vejo que você também é dono da Honeyburton e da Honron!
Sim, eles fornecem apicultores para nossas fazendas.
Apicultor. Acho que esse é um termo muito perturbador. 
Não imagino que você empregue algum libertador de abelhas, certo? 
Não. 
Não consegui ouvir. 
Não. 
Não. Porque você não liberta abelhas. Você cria abelhas. Não só isso, parece que você pensou que um urso seria uma imagem apropriada para um pote de mel. 
Eles são criaturas muito adoráveis. Urso Yogi, Urso Fozzie, Urso de Construção. 
Você quer dizer assim? 
Ursos matam abelhas! 
Como você gostaria que a cabeça dele batesse na sua sala de estar?! Mordendo seu sofá! Cuspindo suas almofadas! OK, já chega. Leve-o embora. 
Então, Sr. Sting, obrigado por estar aqui. Seu nome me intriga. Onde eu já o ouvi antes? 
Eu estava com uma banda chamada The Police. 
Mas você nunca foi policial, foi? 
Não, eu não fui. 
Não, você não foi. E aqui temos mais um exemplo de cultura de abelhas casualmente roubada por um humano por nada mais do que um nome artístico de brincadeira. 
Ah, por favor. 
Você já foi picado, Sr. Sting? Porque estou me sentindo um pouco picado, Sting. Ou devo dizer... Sr. Gordon M. Sumner! 
Esse não é o nome verdadeiro dele?! Seus idiotas! 
Sr. Liotta, primeiro, parabéns atrasados ​​pela sua vitória no Emmy por uma participação especial em ER em 2005. 
Obrigado. Obrigado. 
Vejo pelo seu currículo que você é diabolicamente bonito com uma turbulência interna agitada que está pronta para explodir. 
Eu gosto do que faço. Isso é crime? 
Ainda não é. Mas é isso que aconteceu com você? Explorar abelhas minúsculas e indefesas para não ter que ensaiar sua parte e aprender suas falas, senhor? 
Cuidado, Benson! Eu poderia explodir agora mesmo! 
Este não é um bom sujeito. 
Este é um mau sujeito! 
Por que alguém não pisa nesse canalha e todos nós podemos ir para casa?! 
Ordem neste tribunal! 
Vocês todos estão pensando nisso! 
Ordem! Ordem, eu digo! 
Diga! 
Sr. Liotta, por favor, sente-se! 
Acho que foi muito legal da parte daquele urso ajudar assim. Acho que o júri está do nosso lado. 
Estamos fazendo tudo certo, legalmente? 
Sou florista. 
Certo. Bem, aqui vai para uma ótima equipe. 
Para uma ótima equipe! 
Bem, olá. 
Ken! 
Olá. 
Não pensei que você viria. 
Não, eu estava atrasado. Tentei ligar, mas... a bateria. 
Não queria desperdiçar tudo isso, 
então liguei para Barry. Por sorte, ele estava livre. 
Ah, que sorte. 
Sobrou um pouco. Eu poderia esquentar. 
Sim, esquentar, claro, tanto faz. 
É onde eu geralmente sento. Certo... ali.
Ken, Barry estava olhando seu currículo e concordou comigo que comer com hashis não é realmente uma habilidade especial. 
Você acha que eu não vejo o que você está fazendo? 
Eu sei como é difícil encontrar o emprego certo. Temos isso em comum. 
Temos? 
As abelhas têm 100% de emprego, mas fazemos trabalhos como tirar a sujeira. 
Era exatamente isso que eu estava pensando em fazer. 
Ken, emprestei sua navalha para Barry para a penugem dele. Espero que esteja tudo bem. 
Vou drenar o velho ferrão. 
Sim, faça isso. 
Olhe para isso. 
Sabe, eu já estou farto dos seus pequenos jogos mentais. 
O que é isso? 
Vogue italiana. 
Mamma mia, são muitas páginas. 
Muitos anúncios. 
Lembra do que Van disse, por que sua vida é mais valiosa que a minha? 
Engraçado, eu simplesmente não consigo me lembrar disso! Acho que tem algo fedorento aqui! 
Adoro o cheiro de flores. 
Como você gosta do cheiro de chamas?! 
Nem tanto. 
Inseto aquático! Não tomo partido! 
Ken, estou usando um chapéu Chapstick! 
Isso é patético! 
Tenho problemas! 
Bem, bem, bem, um royal flush! 
Você está blefando. 
Estou? 
O surfe está bom, cara! 
Água de cocô! 
Essa tigela é horrível. Exceto por aqueles anéis amarelos sujos! 
Kenneth! O que você está fazendo?! 
Sabe, eu nem gosto de mel! Eu não como! 
Precisamos conversar! Ele é só uma abelhinha! 
E ele é a abelhinha mais legal que conheci em muito tempo! 
Muito tempo? Do que você está falando?! Existem outros insetos na sua vida? 
 Não, mas há outras coisas me incomodando na vida. E você é uma delas! 
Tudo bem! Abelhas falantes, noite sem iogurte... 
Meus nervos estão fritos de andar nessa montanha-russa emocional! 
Adeus, Ken. 
E para sua informação, eu prefiro adoçantes artificiais sem açúcar feitos pelo homem! 
Sinto muito por tudo isso. 
Eu sei que tem um gosto residual! Eu gosto! 
Sempre senti que havia algum tipo de barreira entre Ken e eu. Não conseguia superá-la. 
Ah, bem. 
Você está bem para o julgamento? 
Acredito que o Sr. Montgomery está sem ideias. 
Gostaríamos de chamar o Sr. Barry Benson Bee para o banco das testemunhas. 
Não se preocupe. A única coisa que tenho que fazer para mudar o júri é lembrá-los do que eles não gostam nas abelhas. 
Você tem a pinça? 
Você é alérgico? 
Só a perder, filho. Só a perder. 
Sr. Benson Bee, vou perguntar o que acho que todos nós gostaríamos de saber. 
Qual é exatamente o seu relacionamento com aquela mulher? 
Abelhas não fumam!
Mas algumas abelhas estão fumando. 
É isso! Esse é o nosso caso! 
É? Não acabou? 
Vista-se. Tenho que ir a algum lugar. 
Volte para o tribunal e protele. Proteja-se de qualquer maneira que puder. 
E supondo que você tenha feito o passo corretamente, você está pronto para a banheira. 
Sr. Flayman. 
Bem, Meritíssimo, é interessante. As abelhas são treinadas para voar aleatoriamente e, como resultado, não fazemos muito tempo. 
Na verdade, ouvi uma história engraçada sobre... 
Meritíssimo, esses insetos ridículos não tomaram tempo suficiente deste tribunal? Por quanto tempo mais permitiremos que essas travessuras absurdas continuem? 
Eles não apresentaram nenhuma evidência convincente para apoiar suas acusações contra meus clientes, que administram negócios legítimos. 
Eu movo para uma rejeição completa de todo este caso! 
Sr. Flayman, temo que terei que considerar a moção do Sr. Montgomery. 
Mas você não pode! Temos um caso fantástico. 
Onde estão suas provas? 
Onde estão as evidências? 
Mostre-me a arma fumegante! 
Segure-a, Meritíssimo! 
Você quer uma arma fumegante? Aqui está sua arma fumegante. 
O que é isso? 
É um defumador de abelhas! 
O que, isso? Esta engenhoca inofensiva? Isso não machucaria uma mosca, muito menos uma abelha. 
Veja o que aconteceu com as abelhas que nunca foram questionadas: "Fumar ou não?" É isso que a natureza pretendia para nós? Sermos viciados à força em máquinas de fumaça e campos de trabalho de ripas de madeira feitos pelo homem? 
Viver nossas vidas como escravos do mel para o homem branco? 
O que vamos fazer? 
Ele está jogando a carta da espécie. 
Senhoras e senhores, por favor, libertem essas abelhas! 
Libertem as abelhas! Libertem as abelhas! Libertem as abelhas! Libertem as abelhas! Libertem as abelhas! 
O tribunal decide a favor das abelhas! 
Vanessa, nós vencemos! 
Eu sabia que você conseguiria! Toca aqui! 
Desculpe. 
Estou bem! Você sabe o que isso significa? 
Todo o mel finalmente pertencerá às abelhas. 
Agora não teremos que trabalhar tanto o tempo todo. 
Esta é uma perversão profana do equilíbrio da natureza, Benson. 
Você vai se arrepender. 
Barry, quanto mel tem aí? 
Tudo bem. Um de cada vez. 
Barry, quem você está vestindo? 
Meu suéter é Ralph Lauren, e eu não tenho calças. 
E se Montgomery estiver certo? 
O que você quer dizer? 
Nós vivemos do jeito das abelhas há muito tempo, 27 milhões de anos. 
Parabéns pela sua vitória. O que você vai exigir como acordo? 
Primeiro, exigiremos o fechamento completo de todos os campos de trabalho das abelhas. 
Exigimos o fim da glorificação do urso como algo mais do que uma máquina imunda, fedorenta e com mau hálito.
Estamos todos cientes do que eles fazem na floresta. 
Espere meu sinal. Leve-o para fora. 
Ele ficará enjoado por algumas horas, depois ficará bem. 
E não toleraremos mais apelidos negativos para abelhas... 
Mas é apenas um nome artístico de brincadeira! 
...inclusão desnecessária de mel em produtos de saúde falsos e guarnições de lanches humanos para a hora do chá. 
Não consigo respirar. 
Tragam, rapazes! 
Segurem bem aí! Ótimo. 
Toquem. 
Sr. Buzzwell, acabamos de passar três xícaras e há galões a mais chegando! 
Acho que precisamos desligar! 
Desligar? Nunca desligamos. 
Desligar a produção de mel! 
Pare de fazer mel! 
Gire sua chave, senhor! 
O que fazemos agora? 
Bala de canhão! 
Estamos desligando a produção de mel! 
Abortar a missão. 
Abortar a polinização e os detalhes do néctar. 
Retornando à base. 
Adam, você não acreditaria em quanto mel havia lá fora. 
Ah, é? 
O que está acontecendo? Onde estão todos? 
Estão comemorando? 
Estão em casa. 
Não sabem o que fazer. Deitados, dormindo até tarde. 
Ouvi dizer que seu tio Carl estava a caminho de San Antonio com um grilo. 
Pelo menos recuperamos nosso mel. 
Às vezes penso, e daí se os humanos gostam do nosso mel? Quem não gostaria? 
É a melhor coisa do mundo! Fiquei animado por fazer parte da criação dele. 
Esta era minha nova mesa. Este era meu novo trabalho. Queria fazê-lo muito bem. E agora... 
Agora não consigo. 
Não entendo por que não estão felizes. 
Pensei que suas vidas seriam melhores! 
Não estão fazendo nada. É incrível. 
O mel realmente muda as pessoas. 
Você não tem ideia do que está acontecendo, tem? 
O que queria me mostrar? 
Isto. 
O que aconteceu aqui? 
Não é nem a metade. 
Oh, não. Oh, meu Deus. 
Estão todos murchando. 
Não parece muito bom, não é? 
Não. 
E de quem você acha que é a culpa? 
Sabe, vou adivinhar as abelhas. 
Abelhas? 
Especificamente, eu. 
Não pensei que abelhas não precisando fazer mel afetariam todas essas coisas. 
Não são só flores. Frutas, vegetais, todos eles precisam de abelhas. 
Esse é o nosso teste SAT inteiro ali. 
Tire os produtos, isso afeta todo o reino animal. 
E então, é claro... 
A espécie humana? 
Sei que isso também é parcialmente minha culpa. 
Que tal um pacto de suicídio? 
Como fazemos isso? 
Eu vou picar você, você pisa em mim.
Isso te mata duas vezes. 
Certo, certo.
Escute, Barry... desculpe, mas eu tenho que ir. 
Eu tive que abrir minha boca e falar. 
Eles mudaram para este fim de semana porque todas as flores estão morrendo. 
É a última chance que eu terei de ver isso. 
Vanessa, eu só quero dizer que sinto muito. 
Eu nunca quis que acabasse assim. 
Eu sei. Eu também não. 
Torneio das Rosas. 
Rosas não podem praticar esportes. 
Espere um minuto. Rosas. Rosas? 
Rosas! 
Vanessa! 
Rosas?! 
Barry? 
Rosas são flores! 
Sim, elas são. 
Flores, abelhas, pólen! 
Eu sei. 
É por isso que este é o último desfile. 
Talvez não. 
Você poderia pedir para ele ir mais devagar? 
Você poderia ir mais devagar? 
Barry! 
OK, eu cometi um grande erro. 
Isto é um desastre total, tudo culpa minha. 
Sim, é meio que isso. 
Eu arruinei o planeta. Eu queria te ajudar com a floricultura. Eu piorei. 
Na verdade, ela está completamente fechada. 
Eu pensei que talvez você estivesse reformando. 
Mas eu tenho outra ideia, e é melhor do que minhas ideias anteriores combinadas. 
Eu não quero ouvir! 
Tudo bem, eles têm as rosas, as rosas têm o pólen. 
Eu conheço cada abelha, planta e botão de flor neste parque. 
Tudo o que temos que fazer é trazer o que eles têm de volta aqui com o que temos. 
Abelhas. 
Parque. 
Pólen! 
Flores. 
Repolinização! 
Por todo o país! 
Torneio das Rosas, Pasadena, Califórnia. 
Eles não têm nada além de flores, carros alegóricos e algodão doce. 
A segurança será rigorosa. 
Eu tenho uma ideia. 
Vanessa Bloome, FTD. 
Negócio floral oficial. É real. 
Desculpe, senhora. Belo broche. 
Obrigada. Foi um presente. 
Uma vez lá dentro, nós apenas escolhemos o carro alegórico certo. 
Que tal A Princesa e a Ervilha? 
Eu poderia ser a princesa, e você poderia ser a ervilha! 
Sim, eu entendi. 
Onde devo sentar? 
O que você é? 
Eu acredito que eu sou a ervilha. 
A ervilha? 
Ela vai para baixo dos colchões. 
Não neste conto de fadas, querida. 
Vou chamar o delegado. 
Faça isso! Esse desfile todo é um fiasco! 
Vamos ver o que esse bebê vai fazer. 
Ei, o que você está fazendo?! 
Então tudo o que fazemos é nos misturar ao trânsito... sem levantar suspeitas. 
Uma vez no aeroporto, não há como nos parar. 
Pare! Segurança. 
Você e seu inseto embalam seu carro alegórico? 
Sim. 
Ele estava em sua posse o tempo todo? 
Você tiraria seus sapatos?
Remova seu ferrão. 
É parte de mim. 
Eu sei. Só estou me divertindo. 
Mas ele não é sua única esperança? 
As asas deles são muito pequenas... Já não ouvimos isso um milhão de vezes? 
"A área da superfície das asas e a massa corporal não fazem sentido." 
Coloque isso no ar! 
Entendi. Aguarde 
. 
Estamos entrando no ar. 
A maneira como trabalhamos pode ser um mistério para você. Fazer mel exige muitas abelhas fazendo muitos trabalhos pequenos. 
Mas deixe-me falar sobre um trabalho pequeno. Se você fizer bem, faz uma grande diferença. 
Mais do que imaginávamos. Para nós, para todos. 
É por isso que quero que as abelhas voltem a trabalhar juntas. Esse é o jeito das abelhas! Não somos feitos de gelatina. 
Ficamos atrás de um sujeito. 
Preto e amarelo! 
Alô! 
Esquerda, direita, baixo, pairar. 
Pairar? 
Esqueça pairar. 
Isso não é tão difícil. 
Bip-bip! Bip-bip! 
Barry, o que aconteceu?! 
Espere, acho que estávamos no piloto automático o tempo todo. 
Isso pode ter me ajudado. 
E agora não estamos mais! 
Então acontece que eu não sei pilotar um avião. 
Todos vocês, vamos ficar atrás desse sujeito! Saiam! 
Saiam! 
Nossa única chance é se eu fizer o que eu faria, vocês me copiarem com as asas do avião! 
Não precisa gritar. 
Eu não estou gritando! Estamos com muitos problemas. 
É muito difícil se concentrar com esse tom de pânico na voz! 
Não é um tom. Estou em pânico! 
Não consigo fazer isso! 
Vanessa, se recomponha. Você tem que sair dessa! 
Sai dessa. 
Sai 
dessa. Sai dessa! Sai dessa ! 
Sai dessa! Sai dessa! Sai dessa! 
Sai 
dessa! 
Sai dessa! Sai dessa! Sai 
dessa! Espera aí! Por 
quê 
? Vamos, é a minha vez. 
Como está o avião voando? 
Não sei. 
Alô? 
Benson, tem flores para uma ocasião feliz aí? 
Os Pollen Jocks! 
Eles ficam atrás de um sujeito. 
Preto e amarelo. 
Olá. 
Tudo bem, vamos jogar esta lata no asfalto. 
Onde? Não consigo ver nada. Você consegue? 
Não, nada. Está tudo nublado. 
Vamos lá. Você tem que pensar abelha, Barry. 
Abelha pensante. 
Abelha pensante. 
Abelha pensante! 
Abelha pensante! Abelha pensante! 
Espere um minuto. Acho que estou sentindo alguma coisa. 
O quê? 
Não sei. É forte, me puxando. 
Como um instinto de 27 milhões de anos. 
Abaixe o nariz. 
Abelha pensante!
Abelha pensante! Abelha pensante!
O que diabos está na pista? 
Acenda algumas luzes! 
Abelha pensante! 
Vanessa, mire na flor. 
OK. 
Desligue os motores. Estamos entrando no poder das abelhas. Prontos, rapazes? 
Afirmativo! 
Ótimo. Ótimo. Calma, agora. É isso. 
Pouse naquela flor! 
Pronto? Reverso total! 
Gire! 
Não aquela flor! A outra! 
Qual? 
Aquela flor. 
Estou mirando na flor! 
É um cara gordo com uma camisa florida. 
Quero dizer, a flor gigante pulsante feita de milhões de abelhas! 
Puxe para frente. Nariz para baixo. Cauda para cima. 
Gire em torno dela. 
Isso é loucura, Barry! 
Esta é a única maneira que sei voar. 
Estou fazendo koo-koo-kachoo, ou este avião está voando em um padrão de inseto? 
Coloque seu nariz lá. Não tenha medo. Sinta o cheiro. Reverso total! 
Apenas solte. Seja parte disso. 
Mire no centro! 
Agora solte! Solte, mulher! 
Vamos, já. 
Barry, nós conseguimos! Você me ensinou a voar! 
Sim. Sem high-five! 
Certo. 
Barry, funcionou! 
Você viu a flor gigante? 
Que flor gigante? Onde? Claro que 
eu vi a flor! Isso foi genial! 
Obrigado. 
Mas ainda não terminamos. 
Ouçam, pessoal! 
Esta pista está coberta com o último pólen das últimas flores disponíveis em qualquer lugar da Terra. 
Isso significa que esta é a nossa Última Chance. Somos os únicos que fazem mel, polinizam flores e se vestem assim. 
Se vamos sobreviver como espécie, este é o nosso momento! O que você diz? 
Vamos ser abelhas ou apenas chaveiros do Museu de História Natural? 
Somos abelhas! 
Chaveiro! 
Então me siga! Exceto o chaveiro. 
Espere, Barry. Aqui. Você mereceu isso. 
Sim! 
Eu sou um Pollen Jock! E é um ajuste perfeito. Tudo o que tenho que fazer são as mangas. 
Ah, sim. 
Esse é o nosso Barry. 
Mãe! As abelhas estão de volta! 
Se alguém precisar fazer uma ligação, agora é a hora. Tenho a sensação de que trabalharemos até tarde hoje à noite! 
Aqui está seu troco. Tenha uma ótima tarde! Posso ajudar quem é o próximo? 
Você gostaria de um pouco de mel com isso? 
É aprovado pelas abelhas. Não se esqueça disso. 
Leite, creme, queijo, sou tudo eu. E eu não vejo um centavo! 
Às vezes me sinto como um pedaço de carne! 
Eu não tinha ideia. 
Barry, me desculpe. 
Você tem um momento? 
Você me daria licença? 
Meu associado mosquito vai te ajudar. 
Desculpe pelo atraso. 
Ele também é advogado?
Eu já era um parasita sugador de sangue. Tudo o que eu precisava era de uma maleta. 
Tenha uma ótima tarde! 
Barry, acabei de receber um pedido enorme de tulipas e não consigo levá-las a lugar nenhum. 
Sem problemas, Vannie. Deixe comigo. 
Você é um salva-vidas, Barry. Posso ajudar quem é o próximo? 
Tudo bem, corram, atletas! É hora de voar. 
Obrigado, Barry! 
Essa abelha está vivendo minha vida! 
Deixe para lá, Kenny. 
Quando esse pesadelo vai acabar?! 
Deixe tudo para lá. 
Lindo dia para voar. 
Claro que sim. 
Entre você e eu, 
eu estava morrendo de vontade de sair daquele escritório. 
Você tem que começar a pensar em abelha, meu amigo. 
Pensando em abelha! 
Eu? 
Espere. Vamos parar por um segundo. Espere. 
Sinto muito. Sinto muito, pessoal. Podemos parar aqui? 
Não vou tomar uma decisão importante na vida durante um número de produção! 
Tudo bem. Tire dez, pessoal. Concluam, rapazes. 
Eu praticamente não tive ensaio para isso.
"""
enviar_script(script)