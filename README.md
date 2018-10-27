# auto-reminder
##### 闲来无事写的b站直播提醒器, 可以自动发邮件，配合ifttt使用
原理仅仅是get了直播间的信息, 用bs4提取标签,
其实后来听同学说B站开放了此API, 调用方法: http://live.bilibili.com/bili/isliving/${mid}
UPDATE: 2018.01 该api已封
https://api.live.bilibili.com/room/v1/Room/room_init?id=[] 长短roomid皆可
返回格式：
```json
{"code":0,"msg":"ok","message":"ok","data":{"room_id":5440,"short_id":1,"uid":9617619,"need_p2p":0,"is_hidden":false,"is_locked":false,"is_portrait":false,"live_status":2,"hidden_till":0,"lock_till":0,"encrypted":false,"pwd_verified":false,"live_time":-62170012800,"room_shield":1,"is_sp":0}}
```
