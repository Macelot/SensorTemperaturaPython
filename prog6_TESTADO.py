#############################################################
#  ########\                                                #
#  ##  _____|                                               #
#  ## |       ######\####\   #######\                       #
#  #####\     ##  _##  _##\ ##  _____|                      #
#  ##  __|    ## / ## / ## |## /                            #
#  ## |       ## | ## | ## |## |                            #
#  ########\  ## | ## | ## |\#######\                       #
#  \________| \__| \__| \__| \_______|                      #
#    Ércio       Marcelo       Cainã                        #
#                                                           #
#  Leitor de Temperatura e Umidade                          #
#  Este progorama recebe informação do pino 25. Tais        #
#  informações são tratadas pela biblioteca para            #
#  identificar a temperatura e umidade.                     #  
#                                                           #
#  Autores: Marcelo Josué Telles,                           #
#           Ércio Luis Dorneles Berna,                      #
#           Cainã Silva da Costa                            #
#                                                           #
#  Data: 03/06/2017                                         #
#############################################################
#Definindo a utilização da biblioteca GPIO e time 
#	em um mesmo import
import RPi.GPIO as GPIO, time
#Definindo a utilização da biblioteca do sensor DHT11 da 
#	empresa Adafruit
import Adafruit_DHT 
#Defindo tipo de sensor, também temos o sensor DHT22
sensor = Adafruit_DHT.DHT11
#Aqui definimos que vamos usar o numero de ordem do pino, e
#	não o numero que refere a porta
#Para usar o numero da porta, é preciso trocar a definição 
#	"GPIO.BOARD (12)" para "GPIO.BCM (18)" 
#Definindo a pinagem real
GPIO.setmode(GPIO.BOARD)
#Definindo o pino a ser utilizado
pino_sensor = 25
#Informacoes iniciais
print ("***Lendo os valores de temperatura e umidade***");
while(1):
   #Efetua a leitura do sensor
   umid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
   #Caso leitura esteja ok, mostra os valores na tela
   if umid is not None and temp is not None:
     print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}\n").format(temp, umid);
     print ("Aguarda 5 segundos para efetuar nova leitura...\n");
     time.sleep(5)
   else:
     # Mensagem de erro de comunicacao com o sensor
     print("Falha ao ler dados do DHT11 !!!")
#Fonte: FILIPEFLOP
#http://blog.filipeflop.com/embarcados/temperatura-umidade-dht11-com-raspberry-pi.html 	 