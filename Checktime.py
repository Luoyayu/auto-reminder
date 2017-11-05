import datetime
# 19:00pm to 23:00
start = 19 * 60
end = 23 * 60
def check():
    i = datetime.datetime.now()
    cur = i.hour*60 + i.minute
    if(cur > start and  cur < end):
        return True
    else:
        return False

# print(check())