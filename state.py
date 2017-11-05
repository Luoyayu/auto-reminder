# -*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup


def status(domain, cid, ts):
    return_data = requests.get(domain+'player'+'?'+'id='+cid+'&'+ts,verify=True)
    soup = BeautifulSoup(str(return_data.text), "html.parser")
    # print(soup)
    if soup.find("state").string == 'LIVE':
        return True
    else:
        return False
# print(status(domain,t3_cid,t3_ts))
