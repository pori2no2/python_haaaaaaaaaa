from mastodon import Mastodon
import time
import re

def login():
    mastodon = Mastodon(
        client_id="client_id.txt",
        access_token="access_token.txt",
        api_base_url = "https://pawoo.net"
    )
    
    return mastodon

def haaaaaa(t):
    result = ''
    if 'は' in t:
        haa = r'はー+😊'
        pattern = re.compile(haa)
        if len(re.findall(pattern,t)) == 0:
            result = t.replace('は','はーー😊😊😊')
    return result

mastodon = login()

timeid = 0
#posted = mastodon.status_post("for test",visibility="direct")
while True:
    time.sleep(5)
    timeline_now = mastodon.timeline()
    if timeline_now[0]['id'] > timeid and timeline_now[0]['account']['id'] != 623599:
        newest_toot = timeline_now[0]['content'].replace('<p>','').replace('</p>','')
        tootWithHaaaa = haaaaaa(newest_toot)
        if tootWithHaaaa != '':
            posted = mastodon.status_post(tootWithHaaaa,visibility="unlisted")
            timeid = timeline_now[0]['id']
