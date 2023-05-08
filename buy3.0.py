# uncompyle6 version 3.9.0
# Python bytecode version base 3.6 (3379)
# Decompiled from: Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: buy3.0.py
# Compiled at: 1995-09-28 00:18:56
# Size of source mod 2**32: 272 bytes
import requests, time, random, sys, re, json, datetime, random, csv, os
os.environ['NO_PROXY'] = '.163.com'
os.environ['REQUESTS_CA_BUNDLE'] = os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')
import warnings
warnings.filterwarnings('ignore')
MyUserAgents = [
 "'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'", 
 "'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)'", 
 "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'", 
 "'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20'", 
 "'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6'", 
 "'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'", 
 "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0) ,Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'", 
 "'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)'", 
 "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'", 
 "'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)'", 
 "'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre'", 
 "'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52'", 
 "'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12'", 
 "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)'", 
 "'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6'", 
 "'Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6'", 
 "'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'", 
 "'Opera/9.25 (Windows NT 5.1; U; en), Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9'", 
 "'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'"]

def buy(item):
    print('购买商品的请求：····')
    data = {
     'game': "'csgo'", 
     'allow_tradable_cooldown': '0', 
     'token': "''", 
     'cdkey_id': "''"}
    data.update(item)
    resp = http.post('https://buff.163.com/api/market/goods/buy', json=data)
    print(resp.json())
    if 'SellOrder Has Successed' in str(resp.json()):
        print('该商品已被别人买走，您被截胡了！')
        return 0
    if '刷新' in str(resp.json()):
        print('商品页面失效,尝试去buff网页更新一下cookie')
        return 0
    else:
        if '不支持' in str(resp.json()):
            if data['pay_method'] == 3:
                data['pay_method'] = 1
            else:
                if data['pay_method'] == 1:
                    data['pay_method'] = 3
            resp = http.post('https://buff.163.com/api/market/goods/buy', json=data)
            print(resp.json())
        order_id_list = re.findall("'id': '.*?'", str(resp.json()))
        temp_id_list = order_id_list[-1].split(': ')
        order_id = temp_id_list[-1]
        return eval(order_id)


def send_offer(order_id, buy_user_id):
    print('请卖家发报价的请求：····')
    refuse_buy_user_id = ''
    json_data = {'bill_orders':[
      order_id], 
     'game':'csgo'}
    resp = http.post('https://buff.163.com/api/market/bill_order/ask_seller_to_send_offer', json=json_data)
    print(resp.json())
    if '卖家拒绝主动发报价' in str(resp.json()):
        print('卖家拒绝主动发报价,槽它嘛嘛缺德玩意儿。')
        refuse_buy_user_id = buy_user_id
    else:
        print('卖家可以主动发报价')
        refuse_buy_user_id = ''
    return refuse_buy_user_id


def item_message(goods_id, good_name, min_paintwear='', max_paintwear='', paintseed='', top_price=0.05, cookie='', myuseragent=''):
    good_id = goods_id
    buy_sell_order_id = []
    buy_price = []
    buy_user_id = []
    buy_pay_method = []
    pay_method = 3
    url = 'https://buff.163.com/api/market/goods/sell_order?game=csgo&goods_id=' + str(good_id) + '&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&paintseed=' + str(paintseed) + '&min_paintwear=' + str(min_paintwear) + '&max_paintwear=' + str(max_paintwear)
    headers = {'User-Agent':myuseragent, 
     'Connection':'close', 
     'referer':'https://buff.163.com/goods/' + str(goods_id) + '?from=market', 
     'cookie':cookie}
    print(headers['referer'])
    try:
        response = requests.get(url, headers=headers, verify=False, timeout=(3, 7))
    except Exception as e:
        print(str(e))
        print('出错···')
        with open('error.txt', 'a', encoding='utf-8') as (file):
            file.write(str(e) + '\n')
        time_limit_random = random.uniform(time_limit_min, time_limit_max + 1)
        print('等待{0}秒后继续···'.format(time_limit_random))
        time.sleep(time_limit_random)
        return (buy_sell_order_id, buy_price, buy_pay_method, buy_user_id)

    print(response.status_code)
    content = response.text
    sell_order_id_list_init = re.findall('"id": ".*?"', content)
    price_list_init = re.findall('"price": ".*?"', content)
    user_id_list_init = re.findall('"user_id": ".*?"', content)
    if sell_order_id_list_init == []:
        if response.status_code == 429:
            print('响应错误429')
            with open('429.txt', 'a') as (file):
                file.write('响应错误429')
            f.close()
            return (1, 2, 3, 4)
        if response.status_code == 200:
            if '"goods_infos": {},' in response.text:
                print('暂无数据,请检查goods.txt和程序运行时的商品id，磨损，模板，价格是否对应是否一致。')
                print('也有可能商品信息正确，但是在售没有数据，等待几秒钟继续运行程序！')
                time_random = random.uniform(5, 11)
                print('扫描完毕，等待{0}秒中后继续···'.format(time_random))
                time.sleep(time_random)
    sell_order_id_list = []
    price_list = []
    user_id_list = []
    for i in sell_order_id_list_init:
        j = i.split(': ')[-1]
        sell_order_id_list.append(j)

    for i in price_list_init:
        j = i.split(': ')[-1]
        price_list.append(j)

    for i in user_id_list_init[:10]:
        j = i.split(': ')[-1]
        user_id_list.append(j)

    for price in price_list:
        print('第一页商品价格分别是:', price)

    print('开始扫描第一页商品······')
    for index in range(len(sell_order_id_list)):
        print('当前price:', price_list[index])
        if float(eval(price_list[index])) < top_price:
            print('找到漏！')
            url_buy = 'https://buff.163.com/api/market/goods/buy/preview?game=csgo&sell_order_id=' + eval(sell_order_id_list[index]) + '&goods_id=' + str(good_id) + '&price=' + eval(price_list[index]) + '&allow_tradable_cooldown=0'
            response_buy = requests.get(url_buy, headers=headers, verify=False, timeout=(3,
                                                                                         7))
            content_buy = response_buy.text
            print(response_buy.json())
            balance_list_init = re.findall('"balance": ".*?"', content_buy)
            balance_list = []
            for i in balance_list_init:
                j = i.split(': ')[-1]
                balance_list.append(float(eval(j)))

            print('余额列表=', balance_list)
            enough_list_init = re.findall("'enough': .*?,", str(response_buy.json()))
            enough_list = []
            for i in enough_list_init:
                j = i.split(': ')[-1]
                enough_list.append(j[:-1])

            if enough_list_init == []:
                print('商品可能被买走！')
                return (1, 2, 3, 4)
            if len(enough_list) == 4:
                for i in range(len(enough_list)):
                    if enough_list[i] == 'True':
                        if i == 0:
                            print('使用支付宝支付！')
                            pay_method = 3
                            buy_sell_order_id.append(sell_order_id_list[index])
                            buy_price.append(price_list[index])
                            buy_user_id.append(user_id_list[index])
                            buy_pay_method.append(pay_method)
                            break
                    elif i == 2:
                        print('使用银行卡支付！')
                        pay_method = 1
                        buy_sell_order_id.append(sell_order_id_list[index])
                        buy_price.append(price_list[index])
                        buy_user_id.append(user_id_list[index])
                        buy_pay_method.append(pay_method)
                        break
                    else:
                        print('买不起我是个穷b，再见。')

            else:
                if len(enough_list) == 5:
                    for i in range(len(enough_list)):
                        if enough_list[i] == 'True':
                            if i == 0:
                                print('使用支付宝支付！')
                                pay_method = 3
                                buy_sell_order_id.append(sell_order_id_list[index])
                                buy_price.append(price_list[index])
                                buy_user_id.append(user_id_list[index])
                                buy_pay_method.append(pay_method)
                                break
                            else:
                                if i == 1:
                                    continue
                                else:
                                    if i == 2:
                                        print('使用银行卡支付！')
                                        pay_method = 1
                                        buy_sell_order_id.append(sell_order_id_list[index])
                                        buy_price.append(price_list[index])
                                        buy_user_id.append(user_id_list[index])
                                        buy_pay_method.append(pay_method)
                                        break
                                    elif i == 3:
                                        print('使用银行卡和支付宝合并支付！')
                                        pay_method = 8
                                        buy_sell_order_id.append(sell_order_id_list[index])
                                        buy_price.append(price_list[index])
                                        buy_user_id.append(user_id_list[index])
                                        buy_pay_method.append(pay_method)
                                        break
                        elif i == 4:
                            continue
                        else:
                            print('买不起我是个穷b，再见。')

                else:
                    print('第三种情况，快快联系群主！')
            order_id = buy({'goods_id':goods_id, 
             'sell_order_id':eval(buy_sell_order_id[index]), 
             'price':eval(buy_price[index]), 
             'pay_method':buy_pay_method})
            if order_id == 0:
                pass
            else:
                print('-------------' * 10)
                refuse_buy_user_id = send_offer(order_id, buy_user_id[index])
                if refuse_buy_user_id == '':
                    print('成功购买，需要等待卖家发报价！')
                    now2 = datetime.datetime.now()
                    with open('捡到的漏都在这里.txt', 'a', encoding='utf-8') as (file):
                        file.write(str(now2)[0:10] + '：' + str(good_name) + '：' + str(buy_price[index]) + '\n')
                else:
                    print('成功失败，卖家这孙子不主动发报价！')
                    with open('SB卖家之黑名单.txt', 'a+', encoding='utf-8') as (file):
                        if re.search(str(refuse_buy_user_id), file.read()):
                            pass
                        else:
                            file.write(str('某sb卖家的USER-id：' + str(refuse_buy_user_id) + '\n'))
                print('快速购买完毕！')
                continue
        else:
            print('没有漏！')
            return (1, 2, 3, 4)

    print('扫描完毕')
    return (buy_sell_order_id, buy_price, buy_pay_method, buy_user_id)


def init():
    print('本软件由简陋小屋出品······')
    time.sleep(1)
    print('欢迎加QQ群703811326，更有buff自动购买扫拍，IGXE一键压价、buff自动上架等工具和福利等你···')
    time.sleep(1)
    print('······' * 300)
    print('······························本软件仅在QQ群售卖，咸鱼售卖的一律是骗子······························')
    print('······························本软件仅在QQ群售卖，咸鱼售卖的一律是骗子······························')
    print('······························本软件仅在QQ群售卖，咸鱼售卖的一律是骗子······························')
    print('······' * 300)
    time.sleep(1.5)


if __name__ == '__main__':
    good_name = []
    good_id = []
    top_price = []
    min_paintwear = []
    max_paintwear = []
    paintseed = []
    gt = datetime.datetime(2023, 5, 10, 12, 0, 28, 396610)
    print('软件到期时间是', str(gt)[:10])
    try:
        NOW = datetime.datetime.now()
        if NOW > gt:
            a = input('软件使用期限已到期')
            sys.exit(0)
        init()
        time_limit_min = float(input('请输出扫拍查询间隔时间-最低几秒钟查询一次：'))
        time_limit_max = float(input('请输出扫拍查询间隔时间-最高几秒钟查询一次：'))
        f = open('goods.txt', encoding='utf-8')
        line = f.readlines()
        print('商品信息行数：', len(line))
        for i in range(len(line)):
            good_name.append(line[i].split('-')[0].strip())
            good_id.append(line[i].split('-')[1])
            paintseed.append(eval(line[i].split('-')[2]))
            min_paintwear.append(eval(line[i].split('-')[3]))
            max_paintwear.append(eval(line[i].split('-')[4]))
            top_price.append(float(eval(line[i].split('-')[5].strip())))

        f.close()
        print('商品名称:', good_name)
        print('商品id:', good_id)
        print('商品模板:', paintseed)
        print('最小磨损:', min_paintwear)
        print('最大磨损:', max_paintwear)
        print('最高价格:', top_price)
        f = open('cookie.txt', encoding='utf-8')
        cook = f.read()
        f.close()
        print('信息检索完毕，3秒后开始检索商品！！！')
        time.sleep(3)
        http = requests.Session()
        cookie = cook
        x_csrftoken_index = cookie.index('csrf_token=')
        x_csrftoken = cookie[x_csrftoken_index + 11:x_csrftoken_index + 102]
    except Exception as e:
        print(str(e))
        print('可能是商品信息出错或者cookie未填写，请检查！')
        with open('error.txt', mode='a', encoding='utf-8') as (file):
            file.write(str(e) + '\n')
            a = input()

    index = 0
    refuse_buy_user_id = ''
    while 1:
        NOW = datetime.datetime.now()
        if NOW > gt:
            a = input('软件使用期限已到期')
            sys.exit(0)
        try:
            myuseragent = random.choice(MyUserAgents)
            http.headers = {'accept':'application/json, text/javascript, */*; q=0.01', 
             'accept-encoding':'gzip, deflate, br', 
             'accept-language':'zh-CN,zh;q=0.9', 
             'content-length':'150', 
             'content-type':'application/json', 
             'cookie':cookie, 
             'origin':'https://buff.163.com', 
             'referer':'https://buff.163.com/goods/' + good_id[index], 
             'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"', 
             'sec-ch-ua-mobile':'?0', 
             'sec-fetch-dest':'empty', 
             'sec-fetch-mode':'cors', 
             'sec-fetch-site':'same-origin', 
             'User-Agent':myuseragent, 
             'x-csrftoken':x_csrftoken, 
             'x-requested-with':'XMLHttpRequest'}
            print('开始检索：', good_name[index])
            print('--------' * 10)
            buy_sell_order_id, buy_price, buy_pay_method, buy_user_id = item_message(good_id[index], good_name[index], min_paintwear[index], max_paintwear[index], paintseed[index], top_price[index], cookie, myuseragent)
            if buy_sell_order_id == 1 or len(buy_sell_order_id) == 0:
                print('出现意外，放弃购买或者没扫到漏、或者快速购买完毕。')
                if index < len(good_id) - 1:
                    index = index + 1
                else:
                    index = 0
                time_limit_random = random.uniform(time_limit_min, time_limit_max + 1)
                print('准备完毕，等待{0}秒中后继续···'.format(time_limit_random))
                time.sleep(time_limit_random)
                continue
        except Exception as e:
            print(str(e))
            with open('error.txt', 'a', encoding='utf-8') as (file):
                file.write(str(e) + '\n')
            time_limit_random = random.uniform(time_limit_min, time_limit_max + 1)
            print('等待{0}秒中后继续···'.format(time_limit_random))
            time.sleep(time_limit_random)
            continue
# okay decompiling buy3.0.pyc
