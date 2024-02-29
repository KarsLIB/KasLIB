import serial
import requests
import pyttsx4
from discord import SyncWebhook
class kars():
    def read(serialid, buatrate):
        read = serial.Serial(serialid, buatrate)
        received_data = read.readline().decode('utf-8').strip()
        return received_data
    def write(serial, buatrate, Inputdata):
        write = serial.Serial(serial, buatrate)
        write_Data = write.write(Inputdata) 
    def senddiscordwebhook(webhookURL , data):
        Send = SyncWebhook.from_url(webhookURL)
        Data_send = Send.send(data)
        return print("data sent!")
    def Say(Engine, Say):
        engine = pyttsx4.init(Engine)
        engine.say(Say)
        engine.runAndWait
    def DiscordRaid(Link, Payload, Token):
        Header = {
            "Authorization" : Token
        }
        requests.post(Link, Payload, headers=Header)
    def Discord_Join_server(Authorization_Token, INVID):
        Header = {
            "Authorization" : Authorization_Token
        }
        join_servers = requests.post("https://discord.com/api/v9/channels{}".format(INVID), headers=Header)  ### Ex. kars.Discord_Join_server("YOUR TOKEN", "INVID")
