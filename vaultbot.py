# -*- coding: cp1252 -*-
import telepot
import random
import time
import sys
import base64

s = input('token:')
s2 = base64.b64encode(s)
s3 = 'Mzg2MTQ2MjI3OkFBRjRON1NUVTFHaWFVdzBXdWZBYWZpd040S0Ruc0c0QU93'
if s2 == s3:
    print("nice")
else:
    exit
s4 = base64.b64decode(s3)
token = s4

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    #Todo chat no Telegram tem um ID proprio.
    #Grupos, chats privados, todos eles tem um ID!
    #Voce so adquire este ID ao alguem se comunicar com o Bot.
    #Para se comunicar (via bot) com alguem, vc precisa do ID de chat.
    #Logo, para o bot enviar mensagens, alguem precisa enviar alguma primeiro pra ele.
    chat_id = msg['chat']['id']

    if content_type == "new_chat_member":
         bot.sendMessage(chat_id,'welcome', reply_to_message_id= True)

    #Adquire a mensagem recebida.
    msg_text = msg['text']

    user_id = msg['from']['id']

    
    if msg_text == '/random':
         bot.sendMessage(chat_id,random.randint(1,100))   
    if msg_text == '/C':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKUmhXdnR4cXgzMzQ&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/C++':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKRjUxUzUyNU12ZTg&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/C#':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKQmI3dTU1TkhRbGs&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/python':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKX3BiUEJlOFVsS0k&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/shell script':
        try:bot.sendMessage(user_id,'https://drive.google.com/open?id=0Bwai0kYN-ieKYWJRSkpkcHJ1QzA')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/redes':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKNmh5MUVvcDdRLWM&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/hardware':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKU2w5SjdPUEtmS1k&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/programming':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKMVJvQmtMQ0VJQTA&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/ajuda':
        try:bot.sendMessage(user_id,'Principais comandos do Bot:\n OBS:NAO cliquem nos COMANDOS, copiem e colem , ou olhem e digitem pois caso contrario NÃO IRÁ FUNCIONAR!\n/infhelp - ajuda para os comandos relacionados a T.I e computing em geral \n/mediahelp - ajuda para os comandos de entreterimento.')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/Engsoft':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0Bwai0kYN-ieKRzJzMkNhaURCckE&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/java':
        try:bot.sendMessage(user_id,'https://drive.google.com/folderview?id=0B7DZdGrd5LrRN3pKSHNSWTVTUUk&usp=sharing')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/start':
         bot.sendMessage(user_id,'olá digite /ajuda para ver os comandos')
    if msg_text == '/mediahelp':
        try:bot.sendMessage(user_id,'/corelx8n software para designers\n/filmes - Muitos filmes.\n/007 - Coleção de 23 filmes 007 1962-2012.\n/jogos - Muitos jogos.\n/series - Muitas séries.\n/discografia - Coleção com diversas discografias.\n/documentarios - Coleção com diversos documentários.\n/gospel - Conteúdo Gospel.\n/animes - Coleção de Anime.')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/infhelp':
        try:bot.sendMessage(user_id,' /programming - 300GB de mateiral de lógica de programação. \n/C-material sobre a linguagem C \n/C++ - material sobre C++ \n/C# - material sobre C# \n/python - material sobre python \n/java - material sobre java para iniciantes \n/casadocodigo - Vários livros da Casa do Código.\n/gnu - Um ótimo material sobre GNU/Linux.\n/bancodedados - Um ótimo material sobre Banco de Dados.\n/hardware - Um ótimo material sobre Hardware.\n/redes - Um ótimo material sobre Redes de computadores.\n/engenharia - 300GB de engenharia de software.')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/clavis':
        try:bot.sendMessage(user_id,'https://drive.google.com/open?id=0B7DZdGrd5LrRVW51ZVd1NnpkMVk')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/cathedra':
        try:bot.sendMessage(user_id,'https://drive.google.com/open?id=0B7DZdGrd5LrRdXN3bFRDcVZOaXM')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/linkdosdeuses':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/EAYC/49MrQZkhS')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/filmes':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/3kzc/QTKWxwJCi')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/casadocodigo':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/5AMh/bfL4z7Ccq')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/gnu':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/FLvd/NPdxHxMau')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/bancodedados':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/LpSU/LYMMzZfp1')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/programming':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/ENkW/oNNusHUge')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/hardware':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/4ahJ/Vz3UMVWPL')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/redes':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/47Z4/PqXy26Wry')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/engenharia':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/7nHp/i3GPnyQ6M')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/darknet':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/2X1N/cqjTZPHWG')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/007':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/BWUn/jDF3p8XrA')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/animes':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/DYsu/mRatffRCK')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/documentarios':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/B5Qq/uwt2SAMN7')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/gospel':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/M3jV/BfhNqhPQ6')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/jogos':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/8S4E/EjUKisVDr')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/discografia':
        try:bot.sendMessage(user_id,'https://cloud.mail.ru/public/8zpk/4BKBjamSF')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/series':
        try:bot.sendMessage(user_id,'[Series](https://cloud.mail.ru/public/EpKf/NVLQ1FNhs)', parse_mode = 'Markdown' ,disable_web_page_preview=true)
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/Nmap':
        try:bot.sendDocument(user_id,'BQADAQADHQADvWAMBvn2jZxKCEvMAg') 
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/A-Debian':
        try:bot.sendDocument(user_id,'BQADAQADgg4AAguj7ARnnBkSVTlo7QI')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/Linux-sh':
        try:bot.sendDocument(user_id,'BQADAQADOQADu9p7CmJprITJ96ZmAg') and bot.sendDocument(user_id,'BQADAQADrwAD2oeuBA9kmZVWpzUIAg') and bot.sendDocument(user_id,'BQADAQADrgAD2oeuBD_DO7gCT_9dAg') and bot.sendDocument(user_id,'BQADAQADbAEAAoHXWATF8pNatBBlrgI')  
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/A-Ubuntu':
        try:bot.sendDocument(user_id,'BQADAQADDwADAYOMCSIeF5vbPfzMAg') 
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/A-Html':
        try:bot.sendDocument(user_id,'BQADAQADRgEAAnIEmAfFy-ik47ixTQI')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == '/TutoMega':
        try:bot.sendDocument(user_id,'BQADAQADgg4AAguj7ARnnBkSVTlo7QI')
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
    if msg_text == 'sasas':
        try:bot.sendDocument(user_id,'BQADAQADDwADAYOMCSIeF5vbPfzMAg') 
        except:bot.sendMessage(chat_id, 'Hey, voce ainda nao iniciou uma conversa comigo , dê /start no privado do @deadbotv2_bot')
        

bot = telepot.Bot(token) 

bot.message_loop(handle)

print ('Listening ...')

while 1:
    time.sleep(10)

    
   
