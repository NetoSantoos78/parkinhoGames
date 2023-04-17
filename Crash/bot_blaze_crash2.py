import datetime
import requests
import telebot
import time
import json
import csv

class WebScraper:
    
    def __init__(self):
        
        # EDIT!
        self.game = '[Blaze](www.blaze.com/r/Y6EKRG/)'
        self.token = '6095796945:AAEZV4qx4ri4PAkkZe_YJrNlxV146cJGNKM'
        self.chat_id = '-1001932441640'
        self.url_API = 'http://127.0.0.1:5000/resultados'
        self.gales = 2
        self.link = '[Instagram!](www.instagram.com/parkinho78/)'
        
        
        # MAYBE EDIT!
        self.win_results = 0
        self.loss_results = 0
        self.max_hate = 0
        self.win_hate = 0
        self.quantos_sg = 0
        self.quantos_g1 = 0
        self.quantos_gr = 0
        self.quantos_g2 = 0

        # NO EDIT!
        self.count = 0
        self.analisar = True
        self.alvo = 0
        self.message_delete = False
        self.bot = telebot.TeleBot(token=self.token, parse_mode='MARKDOWN')
        self.date_now = str(datetime.datetime.now().strftime("%d/%m/%Y"))
        self.check_date = self.date_now

    def restart(self):
        if self.date_now != self.check_date:           
            print('Reiniciando bot!')
            self.check_date = self.date_now
            
            self.bot.send_sticker(
                self.chat_id, sticker='CAACAgEAAxkBAAEBbJJjXNcB92-_4vp2v0B3Plp9FONrDwACvgEAAsFWwUVjxQN4wmmSBCoE')
            self.results()

            #ZERA OS RESULTADOS
            self.win_results = 0
            self.loss_results = 0
            self.max_hate = 0
            self.win_hate = 0
            self.quantos_sg = 0
            self.quantos_gr = 0
            self.quantos_g1 = 0
            self.quantos_g2 = 0
            time.sleep(10)

            self.bot.send_sticker(
                self.chat_id, sticker='CAACAgEAAxkBAAEBPQZi-ziImRgbjqbDkPduogMKzv0zFgACbAQAAl4ByUUIjW-sdJsr6CkE')
            self.results()
            return True
        else:
            return False
    
    
    
        

    #contador = Contador("algum_valor", "https://exemplo.com/api")
    def results(self):
        time.sleep(1.5)
        if self.win_results + self.loss_results != 0:
            a = 100 / (self.win_results + self.loss_results) * self.win_results 
        else:
            a = 0
        self.win_hate = (f'{a:,.2f}%')


        return
       
    def alert_sinal(self):
        message_id = self.bot.send_message(
            self.chat_id, text='''
⚠️ ANALISANDO, FIQUE ATENTO!!!
''').message_id
        self.message_ids = message_id
        self.message_delete = True
        return
    
    def alert_gale(self):
        self.quantos_gr += 1
        self.message_ids = self.bot.send_message(self.chat_id, text=f'''⚠️ Vamos para o {self.count}ª GALE''').message_id
        self.message_delete = True
        
        return

    def delete(self):
        if self.message_delete == True:
            self.bot.delete_message(chat_id=self.chat_id,
                                    message_id=self.message_ids)
            self.message_delete = False
      
    def send_sinal(self, finalnum):
        self.analisar = False
        self.bot.send_message(chat_id=self.chat_id, text=(f'''
⚠️ Entrada Confirmada ⚠️
Aposta após o {finalnum}x
Saida em {self.alvo}x 
Auto Retirada👉 1.5x (Prevenção banca baixa)
Máximo {self.gales} gales
🎲 Blaze - *{self.game}*
🎲 Segue nosso - '''f'{self.link}''''
📈 Assertividade = '''f'{self.win_hate}''''
 
𝗣𝗮𝗿𝗸𝗶𝗻𝗵𝗼 𝗖𝗿𝗮𝘀𝗵 =   '''f'{self.win_results}'''' ✅ |  '''f'{self.loss_results}'''' 🚫
SG: '''f'{self.quantos_sg}'''' | G1: '''f'{self.quantos_g1}'''' | G2: '''f'{self.quantos_g2}''''

    '''))
        return
    
    def send_possivelsinal(self, finalnum):
        self.analisar = False
        self.bot.send_message(chat_id=self.chat_id, text=(f'''
⚠️ Possivel Entrada ⚠️
Aposta após o {finalnum}x
Auto Retirada👉 1.5x (Prevenção banca baixa)
Máximo {self.gales} gales
🎲 Blaze - *{self.game}*
🎲 Segue nosso - '''f'{self.link}''''
📈 Assertividade = '''f'{self.win_hate}''''
 
𝗣𝗮𝗿𝗸𝗶𝗻𝗵𝗼 𝗖𝗿𝗮𝘀𝗵 =   '''f'{self.win_results}'''' ✅ |  '''f'{self.loss_results}'''' 🚫
SG: '''f'{self.quantos_sg}'''' | G1: '''f'{self.quantos_g1}'''' | G2: '''f'{self.quantos_g2}''''

    '''))
        return
            
            
    def martingale(self, result):
        
        if result == "WIN":
            print(f"WIN")
            self.win_results += 1
            self.max_hate += 1
            if self.quantos_gr == 0:
                # Adiciona 1 gale ao sg
                self.quantos_sg += 1
                
                #self.bot.send_message(chat_id=self.chat_id, text=(f''' Subiu até x '''))
                
                # FIGURINHA SEM GALE
                self.bot.send_sticker(self.chat_id, sticker='CAACAgEAAx0Ccy64KAACCt9kPCUxnm4jSfkLRqwtxfRwcL1uEQACnwIAAkbMGUQ8uIXdYDPE9i8E')
                
                ## Resetar Gale
                self.quantos_gr -= self.quantos_gr
                
            elif self.quantos_gr == 1:
                # Adiciona 1 gale ao g1
                self.quantos_g1 += 1
                
                #self.bot.send_message(chat_id=self.chat_id, text=(f''' Subiu até x '''))
                
                # FIGURINHA 1º GALE
                self.bot.send_sticker(self.chat_id, sticker='CAACAgEAAx0Ccy64KAACEaVkPUG5BO9ITDx_LZNPZY_3SQhMZAAC0wMAAlIMGUQqzkz1uALjuC8E')
                
                ## Resetar Gale
                self.quantos_gr -= self.quantos_gr
                
            elif self.quantos_gr == 2:
                # Adiciona 1 gale ao g2
                self.quantos_g1 += 1
                
                #self.bot.send_message(chat_id=self.chat_id, text=(f''' Subiu até x '''))
                
                # FIGURINHA 2º GALE 
                self.bot.send_sticker(self.chat_id, sticker='CAACAgEAAx0Ccy64KAACEapkPUHMak3gyb1eN6Xb-sOE6OXMKAACAQIAAmj1IUTy1vn0zRv2pC8E')
                
                ## Resetar Gale
                self.quantos_gr -= self.quantos_gr
                
            #self.bot.send_sticker(self.chat_id, sticker='CAACAgEAAx0Ccy64KAACCt9kPCUxnm4jSfkLRqwtxfRwcL1uEQACnwIAAkbMGUQ8uIXdYDPE9i8E')
            # self.bot.send_message(chat_id=self.chat_id, text=(f'''✅ GREEN!!!'''))
        
        elif result == "LOSS":
            self.count += 1
            
            if self.count > self.gales:
                print(f"LOSS")
                self.loss_results += 1
                self.max_hate = 0
                self.quantos_gr = 0
                #self.bot.send_message(chat_id=self.chat_id, text=(f''' Subiu até x '''))
                self.bot.send_sticker(self.chat_id, sticker='CAACAgEAAx0Ccy64KAACCuFkPCXji9wnfuI4UcUokwNdX2fr_wACfAMAAtSZGUSH_9AQ1paacC8E')
                #self.bot.send_message(chat_id=self.chat_id, text=(f'''🚫🚫🚫 LOSS 🚫🚫🚫'''))

            else:
                print(f"Vamos para o {self.count}ª gale!")
                #self.quantos_gr += 1
                self.alert_gale()
            ####
            #    self.quantos_gr == 1:
            #        self.quantos_g1 += 1
            #    elif self.quantos_gr == 2:
            #        self.quantos_g2 += 1
            ####
                return

        self.count = 0
        self.quantos_foram = 0
        self.analisar = True
        self.results()
        self.restart()
        return
    

    def check_results(self, results):

        if results >= self.alvo:
            self.martingale('WIN')
            
            return
        
        elif results < self.alvo:
            self.martingale('LOSS')
            return

    def start(self):
        check = []
        while True:
            try:
                self.date_now = str(datetime.datetime.now().strftime("%d/%m/%Y"))

                results = []
                time.sleep(1)

                response = requests.get(self.url_API)
                json_data = json.loads(response.text)
                for i in json_data['results']:
                    results.append(float(i))

                if check != results:
                    check = results
                    self.delete()
                    self.estrategy(results)
                
            except:
                print("ERROR - 404!")
                continue

    def estrategy(self, results):
        print(results[0:10])

        if self.analisar == False:
            self.check_results(results[0])
            return

        # EDITAR ESTRATÉGIAS
        elif self.analisar == True:  

            #ESTRATÉGIAS COM BASE NO CSV SEM ALERTAS
            with open('estrategy.csv', newline='') as f:
                reader = csv.reader(f)

                ESTRATEGIAS = []

                for row in reader:
                    string = str(row[0])

                    split_saida = string.split('=')
                    split_string = split_saida[0].split('-')

                    listx = []
                    for i in split_string:
                        listx.append(float(i))

                    values = listx
                    values.reverse()
                    dictionary = {'PADRAO': values, 'SAIDA': float(split_saida[1])}
                    ESTRATEGIAS.append(dictionary)


                for i in ESTRATEGIAS:
                    lista = results[0:len(i['PADRAO'])]
                    self.alvo = i['SAIDA']
                    count = 0
                    sinal = False

                    for i in i['PADRAO']:
                        try:
                            if i >= lista[count]:
                                sinal = True
                                count += 1
                            else:
                                sinal = False
                                break
                        except:
                            sinal = False
                            print("Resultados incompletos")
                            break
                   
                    if sinal:
                        print("SINAL ENCONTRADO.")
                        self.send_sinal(results[0])
                        return


            #ESTRATÉGIAS COM MANUAIS
            # Estrategia 3 loss 
            if results[0] <= 2.0 and results[1] <= 2.0 and results[2] <= 2.0:
                print("SINAL ENCONTRADO!")
                self.alvo = 1.5
                self.send_sinal(results[0])
                return
            # Estrategia 3 loss, 1 green, 1 loss
            if results[0] <= 2.0 and results[1] <= 2.0 and results[2] <= 2.0 and results[3] >= 2.0 and results[4] <= 2.0:
                print("SINAL ENCONTRADO!")
                self.alvo = 1.5
                self.send_sinal(results[0])
                return
            # Estrategia 7 loss seguidos
            if results[0] <= 2.0 and results[1] <= 2.0 and results[2] <= 2.0 and results[3] <= 2.0 and results[4] <= 2.0 and results[5] <= 2.0 and results[6] <= 2.0 and results[7] <= 2.0:
                print("SINAL ENCONTRADO!")
                self.alvo = 1.5
                self.send_possivelsinal(results[0])
                return
            # Estrategia 3 green
            if results[0] >= 2.0 and results[1] >= 2.0 and results[2] >= 2.0:
                print("POSSIVEL SINAL ENCONTRADO APOS 3 GREEN!")
                self.alvo = 1.5
                self.send_possivelsinal(results[0])
                return
            # Estrategia 4 green
            if results[0] >= 2.0 and results[1] >= 2.0 and results[2] >= 2.0 and results[3] >= 2.0:
                print("POSSIVEL QUINTA ENTRADA ENCONTRADA!")
                self.alvo = 1.5
                self.send_possivelsinal(results[0])
                return
            
            #ALERTA DAS MANUAIS
            if results[0] <= 2.0 and results[1] <= 2.0:
                self.alert_sinal()
                return
            

scraper = WebScraper()
scraper.start()