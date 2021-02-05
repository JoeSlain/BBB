import csv, re, time, datetime, sched
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from pyfiglet import Figlet
from order_maker import place_order

class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'
    UNDERLINE = '\033[4m'
custom_fig = Figlet(font='big')
print(bcolors.OKGREEN + custom_fig.renderText("L'avé Maria") + bcolors.ENDC)
print(bcolors.OKBLUE + "By Joss le colosse\n\n" + bcolors.ENDC)

api_id = YOUR TELEGRAM ID
api_hash = 'YOUR TELEGRAM HASH'
phone = 'YOUR PHONE NUMBER (+123456789)'
client = TelegramClient(phone, api_id, api_hash)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Enter the code: '))


chats = []
last_date = None
chunk_size = 200
groups=[]
 
result = client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
chats.extend(result.chats)
#for c in chats:
 #   print(c.title)
#for chat in chats:
#    try:
#        if chat.megagroup== False:
#            groups.append(chat)
#    except:
#        continue

#print('Choose a group to scrape members from:')
#i=0
#for g in chats:
#    print(str(i) + '- ' + g.title)
#    i+=1
#
#g_index = input("Enter a Number: ")
for g in chats:
    if g.title=="Big Pump Signal":
        target_group=g       
#target_group=chats[int(g_index)]

print("Hour of the pump (24h format) ex:22")
pump_hour = input()
print("amount BTC you want to invest")
amount = input()
coin = []
t = datetime.datetime.today() 
pmp_time = datetime.datetime(t.year,t.month,t.day,int(pump_hour)-1,59,59) 
while pmp_time > datetime.datetime.now():
    time.sleep(0.5)
while not coin:
    for message in client.iter_messages(target_group, limit=1):
        coin = re.findall(r"[$]\w+", message.text)
place_order(coin[0].replace('$', ''), amount)
