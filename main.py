import requests, pytz, time
from datetime import datetime
from discord_webhook import DiscordWebhook


def checkprice():
    req = requests.get("https://anlikaltinfiyatlari.com/anlik/charts/jsonp2.php?filename=gramlive.json&time=56").json()
    lastkey = req.pop()
    son = datetime.fromtimestamp(lastkey[0]/1000.00, tz= pytz.timezone('Europe/Istanbul'))
    sontime = son.strftime('%d/%m/%Y %H:%M:%S')
    altinfiyat = lastkey[1]
    webhook = DiscordWebhook(url='buraya webhook urlsi', content=f'En son güncellenen tarih: {sontime} | Gram altın fiyatı: {altinfiyat}')
    yolla = webhook.execute()
    print(f'En son güncellenen tarih: {sontime} | Gram altın fiyatı: {altinfiyat}')


while True:
    checkprice()
    time.sleep(3600)