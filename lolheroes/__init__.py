# -*- codeing -*-
# @Time : 2021/11/15 0:14
# @Author : Torres-圣君
# @File : clockin.py
# @Sofaware : PyCharm
from nonebot.plugin import on_regex
from nonebot.adapters.onebot.v11 import Bot, Event, Message
import requests
import json

test = on_regex(r".*(lol).*(背景故事).*", priority=10)


@test.handle()
async def _(bot: Bot, event: Event):
    msg = str(event.get_message()).strip("lol背景故事 ")
    try:
        with open(r"C:\Users\Administrator\PycharmProjects\qqRobot\torres\src\plugins\lolheros\herosID.json", "r",
                  encoding='utf-8') as r:
            json_data = json.load(r)
            name_url = json_data[msg]
            hero_url = json_data[msg].split("/")
            hero_en = hero_url[-2]
        title_name = hero_en.title()
        photo = f'[CQ:image,file=https://game.gtimg.cn/images/lol/universe/v1/assets/images/champion/splash/{title_name}_0.jpg]'
        await test.finish(message=Message((photo + run(hero_en) +
                                           "\n———————————————————————\n" +
                                           msg + "更多内容请点击：\n" +
                                           name_url)))
    except Exception:
        pass
        # await test.finish(message=Message("您输入的英雄名字有误，或不存在."), at_sender=True)


# 获取英雄背景故事
def run(name_en):
    url = f"https://yz.lol.qq.com/v1/zh_cn/champions/{name_en}/index.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53"
    }
    res = requests.get(url, headers)
    name_data = res.json()
    return name_data["champion"]["biography"]["short"].strip("</p>")
