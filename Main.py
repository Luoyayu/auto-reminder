#-*-coding:utf-8-*-
import state
from user import *
import reminder
import time

cnt = 1
flag1 = False
flag2 = False

while(True):
    mo = state.status(domain,mo_cid,mo_ts)
    cc = state.status(domain, cc_cid, cc_ts)

    if(cc and flag1 == False):
        if(reminder.send_mail('CC', 'ME')):
            print('send suc to CC')
            flag1 = True
    elif(cc == False):
        flag1 = False

    if (mo and flag2 == False): # 如要求在[start:end]区间内提醒  and Checktime.check()
        if (reminder.send_mail('alessa', 'ME')):
            print('send suc to alessa')
            flag2 = True
    elif (mo == False):
        flag2 = False

    print('[process] ' + str(cnt))
    cnt += 1
    time.sleep(120)


