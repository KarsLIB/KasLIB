import serial
import requests
import pyttsx4
from discord import SyncWebhook
def idk(text):
    print('done!', text)
class microkast():
    def read(serialid, buatrate):
        read = serial.Serial(serialid, buatrate)
        received_data = read.readline().decode('utf-8').strip()
        return received_data
    def write(serialid, buatrate, Inputdata):
        write = serial.Serial(serialid, buatrate)
        write_Data = write.write(Inputdata)
        return idk(serialid)
class katdiscord():
     def DiscordRaid(Link, Payload, Authorization_Token):
        Header = {"Authorization" : Authorization_Token }
        requests.post(Link, Payload, headers=Header)
     def Discord_Join_server(Authorization_Token, INVID):
        Header = {"Authorization" : Authorization_Token}
        join_servers = requests.post("https://discord.com/api/v9/channels{}".format(INVID), headers=Header) 
        return idk(Authorization_Token)
     def senddiscordwebhook(webhookURL , data):
        Send = SyncWebhook.from_url(webhookURL)
        Data_send = Send.send(data)
        return idk(webhookURL)
class katsystem():
    def Say(Engine, Say):
        engine = pyttsx4.init(Engine)
        engine.say(Say)
        engine.runAndWait()
class NER():
    print()
    
    
