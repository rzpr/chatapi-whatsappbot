import json
import requests as r, re
from googletrans import Translator

class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl = 'https://api.chat-api.com/instance294052/'
        self.token = 'axxoikrq0moarmmj'
        print(self.dict_messages)
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = r.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

 
    def apa(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            par = text[8:]
            req = r.get('https://api.zeks.xyz/api/wiki?apikey=mx7GKG2UZgIiwZ9FI8FzQEXTOpu&q='+par)
            data = {
               "body": req.json()['result'],
               "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def lirik(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            query = text[5:]
            from lirik import search
            cari = search(query)
            data = {"body" : cari.result(),"chatId" : chatID}
            answer = self.send_requests('sendMessage', data)
            return answer

    def Nama(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            query = text[10:]
            import requests as r
            req = r.get(f'https://lolhuman.herokuapp.com/api/artinama?apikey=e3982397c0f037686dbcaf17&nama={query}')
            data = {
            "body": req.json()['result'],
            "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer

    def niat(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            query = text[11:]
            import requests as r
            req = r.get(f'https://lolhuman.herokuapp.com/api/niatsholat/{query}?apikey=e3982397c0f037686dbcaf17'),
            js = req.json()['result']
            data = {
            "body": f"*{js['name']}*\n\n Arab : {js['ar']}\n\n latin : {js['latin']}\n\n id : {js['id']}",
            "chatId": chatID
            }
            answer = self.send_requests('sendMessage', data)
            return answer
    def start(self, chatID):
        data = {
            "body": "🤖 _Halo Saya Adalah Recsec Bot, Ada Yang Bisa Saya Bantu?_\n\n*Admin :*\n\n📞 : 088299423038\n📱 : _fb.me/rezzapriatna12_ \n\n🚀 *Fitur* \n\n✅ _Youtube Downloader_ \n✅ _Facebook Downloader_ \n✅ _Instagram Downloader_ \n✅ _Google Search_ \n✅ _Text To Speech_ \n✅ _Stalking Profil Instagram_ \n✅ _Translate_ \n\n\n _Untuk Menampilkan Command Ketik_ *Menu*",
            "chatId": chatID
        }
        answer = self.send_requests('sendMessage', data)
        return answer

    def menu(self, chatID):
        data = {
              "body": '*List Of Command* :\n\n🔖 *tulis* _text_ ( Membuat Tulisan Dibuku )\n🔖 *ig* _url_ ( Unduh Video Instagram )\n🔖 *fb* _url_ ( Unduh Video Facebook )\n🔖 *ig-profil* _username_ ( Melihat Profil Instagram )\n🔖 *arti-nama* _text_ ( Mencari arti nama kamu )\n🔖 *lirik* _judul+artis_ ( Mencari Lirik Lagu )\n🔖 *tts* _text_ ( text to speech )\n🔖 *yt* url ( Yt To Mp3 )',
              "chatId": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

    def er(self, chatID):
        p = "Yah Maaf:( Aku Gangerti Apa Yang Kakak Maksud, Kakak Bisa Ketik Start Atau Menu Untuk Menampilkn Apa Saja Yang Aku Bisa:)"
        data = {
              "body": p,
              "phones": chatID
              }
        answer = self.send_requests('sendMessage', data)
        return answer

    def tts(self, chatID):
        for message in self.dict_messages:
            text = message['body'] 
            par = text[4:]
            data = {
                'chatId': chatID,
                'body': 'https://api.zeks.xyz/api/tts?apikey=mx7GKG2UZgIiwZ9FI8FzQEXTOpu&code=id&text='+par,
                'filename': 'hahah',
                'caption': 'example'
            }
            answer = self.send_requests('sendFile', data)
            return answer
    
    def fb(self, chatID):
        for message in self.dict_messages:
            text = message['body'] 
            par = text[3:]
            html = r.get(par)
            video = re.search('sd_src:"(.+?)"', html.text).group(1)
            data = {
                'chatId': chatID,
                'body': video,
                'filename': 'hahah',
                'caption': '✅ *Video Berhasil Didownload*'
            }
            answer = self.send_requests('sendFile', data)
            return answer

    def igg(self, chatID):
        import requests as r
        import re
        for message in self.dict_messages:
            text = message['body'] 
            req = r.get(f'https://lolhuman.herokuapp.com/api/instagram?apikey=e3982397c0f037686dbcaf17&url={text[3:]}')
            data = {
                'chatId': chatID,
                'body': req.json()['result'],
                'filename': 'hahah',
                'caption': '✅ *Video Berhasil Didownload*'
            }
            answer = self.send_requests('sendFile', data)
            return answer


    def ig(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            tex = message['senderName']
            import requests as r
            import json
            par = text[10:]
            req= r.get(f'https://lolhuman.herokuapp.com/api/stalkig/{par}?apikey=e3982397c0f037686dbcaf17')
            js = req.json()['result']
            data = {
                  "chatId": chatID,
                  "body": js['photo_profile'],
                  "filename": 'png',
                  "caption" : '🔎 *Hasil Pencarian Instagram* \n\n*Username* : '+par+'\n*Nama* : '+str(js['fullname'])+'\n*Bio* : '+str(js['bio'])+'\n*Followers* : '+str(js['followers'])+'\n*Following* :'+str(js['following'])
                  
                  
                  }
            answer = self.send_requests('sendFile', data)
            return answer  

    def yt(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            tex = message['senderName']
            import requests as r
            import json
            par = text[2:]
            req= r.get(f'https://api.zeks.xyz/api/ytplaymp4/2?apikey=mx7GKG2UZgIiwZ9FI8FzQEXTOpu&q={par}')
            js = req.json()['result']
            data = {
                  "chatId": chatID,
                  "body": js['thumb'],
                  "filename": 'png',
                  "caption" : f"🔎 *{js['title']}*\n\n*Ukuran* : {js['size']}\n*Durasi* :{js['duration']}\n*Link Download* : {js['link']}"
                  
                  
                  }
            answer = self.send_requests('sendFile', data)
            return answer 

    def tulis(self, chatID):
        for message in self.dict_messages:
            text = message['body']
            tex = message['senderName']
            import requests as r
            import json
            from nulis import tulis
            import base64
            par = text[5:]
            tulis=tulis(par)
            for i in tulis.tulis():
                i.save('gambar.jpg')
                image = open('gambar.jpg', 'rb')
                image_read = image.read()
                image_64_encode = base64.encodebytes(image_read)
                api = 'b76b9a5f05dafad41987044532b9e400'
                url = 'https://api.imgbb.com/1/upload'
                par = {
                 'key':api,
                 'image':image_64_encode,
                 'name':'nulis',
                 'expiration': 60
                }
                headers = {
                  'Accept': 'application/json'
                }
                req = r.post(url,data=par, headers=headers)
                p = req.json()['data']['display_url']
                data = {
                     "chatId": chatID,
                     "body": p,
                     "filename": 'png',
                     "caption" : '*Nih Ka Hasil Nya Maaf Kalo Jelek*'
                    }
                answer = self.send_requests('sendFile', data)
                return answer  

    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                text = message['body'].split()
                if not message['fromMe']:
                    id  = message['chatId']
                    if text[0].lower() == 'niat-sholat':
                        return self.niat(id)
                    elif text[0].lower() == 'lirik':
                        return self.lirik(id)
                    elif text[0].lower() == 'ig-profil':
                        return self.ig(id)
                    elif text[0].lower() == 'ig':
                        return self.igg(id)
                    elif text[0].lower() == 'start':
                        return self.start(id)
                    elif text[0].lower() == 'fb':
                        return self.fb(id)
                    elif text[0].lower() == 'arti-nama':
                        return self.Nama(id)
                    elif text[0].lower() == 'tulis':
                        return self.tulis(id)
                    elif text[0].lower() == 'menu':
                        return self.menu(id)
                    elif text[0].lower() == 'tts':
                        return self.tts(id)
                    elif text[0].lower() == 'yt':
                        return self.yt(id)
                    elif text[0].lower() == 'apa-itu':
                        return self.apa(id)
                    else:
                        return self.er(id)
                else: return 'NoCommand'

            



        
        




