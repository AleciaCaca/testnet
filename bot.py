import requests
import time

payload = {'content': "!faucet 0xbfd123c057bd68407b5b8d72930b2f6bc82a033b"}
header = {'authorization': 'MzgxODMyMTY1OTkxOTA3MzI4.GIayVM.NFtLWatdXruxYMP6y9RwLMSXe8BjnIdzm8WvJs'}
link = "https://discord.com/api/v9/channels/1037811694564560966/messages"
r = requests.post(link, data=payload, headers=header)
print(" => Send")
time.sleep(7200)
print(" => Delay")