import time
import requests

url = "https://app.ucas.ac.cn/ncov/api/default/save"        # 学院填报接口
token = "d0165836daa847b4a51491acb1c5dd3c"                  # pushplus token
title= '每日疫情填报结果' #改成你要的标题内容
mes_url="http://www.pushplus.plus/customer/push/send"# pushplus推送url，无需更改
cookies = {
    "eai-sess": "lnjk4tc4bamur9so6b6sluom93",
    "UUkey": "7ccc0c2d815761b896eb148c30793a53"
}

data = {
    "realname": "李琰朕",  # 姓名
    "number": "2022E8013282046",  # 学号
    "date": time.strftime("%Y-%m-%d", time.localtime()),
    "jzdz":"北京市怀柔区雁栖湖",# 在京地址
    "zrzsdd":"1",# 昨日住宿地点
    "sfzx": "1",    # 是否在校
    "szgj": "中国", # 所在国家
    "szdd": "国内",  # 所在地点
    "dqszdd":"1", #当前所在地点
    "geo_api_info": "{\"address\":\"北京市怀柔区\",\"details\":\"中国科学院大学雁栖湖校区)\",\"province\":{\"label\":\"北京市\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"海淀区\",\"value\":\"\"}}",
    "szgj_api_info": "{\"area\":{\"label\":\"\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"address\":\"\",\"country\":{\"label\":\"\",\"value\":\"\"},\"details\":\"\",\"province\":{\"label\":\"\",\"value\":\"\"}}",
    "created":"1663549596", # 不明信息
    "dqsfzzgfxdq":"4", #当前是否在中高风险地区
    "zgfxljs":"4", # 中高风险旅居史
    "tw": "1",       # 体温选项序号
    "sffrzz":"0", #是否发热
    "dqqk1":"1", #当前情况
    "dqqk2":"1", #当前情况2（健康宝
    "sfjshsjc":"1", #是否接受核酸检测
    "old_szdd": "国内",
    "old_city": "{\"address\":\"北京市怀柔区\",\"details\":\"中国科学院大学雁栖湖校区)\",\"province\":{\"label\":\"北京市\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"海淀区\",\"value\":\"\"}}",
    "geo_api_infot": "{\"address\":\"\",\"details\":\"\",\"country\":{\"label\":\"\",\"value\":\"\"},\"province\":{\"label\":\"\",\"value\":\"\"},\"city\":{\"label\":\"\",\"value\":\"\"},\"area\":{\"label\":\"\",\"value\":\"\"}}",
    "app_id": "ucas",
}

result = requests.post(url=url, data=data,cookies=cookies)

if mes_url:
    if result.text[5] == "0":
        content="填报成功！感谢使用"
    elif result.text[5] == "1":
        content="今天已经填报过了哦！"
    else:
        content="总觉得哪里不对，快去看看吧"
    url = 'http://www.pushplus.plus/send?token='+token+'&title='+title+'&content='+content
    requests.get(url)
    print("运行结束")



