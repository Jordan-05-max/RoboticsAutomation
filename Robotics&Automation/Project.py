"""WhatsApp Automation"""
import pyttsx3
import pywhatkit
# import pyautogui
# from keyboard import press_and_release
from tkinter import Tk
from pyttsx3 import Engine
# from pyautogui import hotkey, moveTo, leftClick
from tkinter.filedialog import askopenfilename
from pywhatkit import sendwhatmsg_instantly, sendwhatmsg, sendwhats_image, system


def systems() -> str:
	"""
    systems() gets the operating system on which app is working
    :return: system name
    """
	sys = system()
	print(sys)
	return sys


def website():
	"""
    updates the whatsapp website by opening and closing the website
    :return: none
    """
	web.open(f"https://web.whatsapp.com/")
	time.sleep(240)
	pyautogui.hotkey('ctrl', 'w')
	time.sleep(20)
	pyautogui.hotkey('alt', 'f4')


def talk(text: str):
	"""
    talk() read the value of the parameter that is parsed into the function
    :param text: str
    :return: speaker.say(param)
    """
	speaker: Engine = pyttsx3.init()
	speaker.setProperty('rate', 150)
	voices = speaker.getProperty('voices')
	speaker.setProperty('voice', voices[1].id)
	speaker.say(text)
	speaker.runAndWait()
	return speaker.say(text)


def display_contact_list(contacts, contact_numbers):
	desired_contacts = []
	print("Choose the name of your contact here: ")
	print("========================================")
	
	contact_list = contacts.keys()
	for contact_index, contact_name in enumerate(contact_list):
		print("{} - {}".format((contact_index + 1), contact_name))
	talk(" Choose the name of your contact here ")
	contact_choices = input("Contact Choice : ").split()
	
	for contact_index in contact_choices:
		print(contact_index)
		if contact_index.isdigit():
			
			contact_index = int(contact_index)
			if 1 <= contact_index <= len(contacts):
				phone_number = contact_numbers.get(contact_index)
				desired_contacts.append(phone_number)
			
			else:
				print("Invalid Option")
				continue
		else:
			raise Exception("Incorrect Input")
	
	return desired_contacts


def display_message_type():
	print("Please select the message type you want : \n")
	print("1 - Instantaneous Message\n")
	print("2 - Planned Message\n")
	print("3 - Diffusion List\n")
	print("4 - Send Image\n")
	talk("Please select the message type you want ")
	choice = input("Message type : ")
	if choice.isdigit():
		choice = int(choice)
		if 1 <= choice <= 4:
			return choice
		else:
			print("Invalid Option")
			exit()
	else:
		raise Exception("Incorrect Input")


def getMessage():
	talk("Please enter your message")
	message = input("Type your message: ")
	# message = ("\n"
	#            "    Monsieur/Madame!\n"
	#            "Nos Salutations les plus distinguées !\n"
	#            "\n"
	#            "Nous vous écrivons de Lovely Professional University en Inde, afin de vous assister dans votre processus d'admission dans notre "
	#            "université.\n"
	#            "Selon cet intérêt que vous avez manifesté, l'université vous offre une bourse de 50%.\n"
	#            "\n"
	#            "Pour commencer le processus d'admission, nous aimerions que vous remplissiez le questionnaire ci-dessous:\n"
	#            "Nom et prénom :\n"
	#            "Pays d'origine :\n"
	#            "Numéro WhatsApp(contact) :\n"
	#            "Date de naissance :\n"
	#            "Email :\n"
	#            "Nom du Père :\n"
	#            "Nom de la Mère :\n"
	#            "Sexe(Genre) :\n"
	#            "Programme d'étude/filière :\n"
	#            "\n"
	#            "Pour plus d'information et d'assistance, vous pouvez nous contacter sur ce même numéro: +918360238249\n")
	return message


def get_img():
	Tk().withdraw()
	filename = askopenfilename()
	return filename


def sendProgrammedDetails():
	try:
		hours = int(input("Please provide the hours: "))
		minutes = int(input("Please provide the minutes: "))
		program_details = {
			"hours": hours,
			"minutes": minutes
		}
		return program_details
	except:
		raise Exception(" Wrong Input")


def get_name(phone_number):
	"""
    name() function gets the name of the selected phone number
    :param phone: Any
    :return: names
    """
	dict2_list = list(phone_dict2.values())
	index = dict2_list.index(phone_number)
	dict_list = list(phone_dict.keys())
	names = dict_list[index]
	print(names)
	return names


phone_dict = {"Jordan": "+22962747600", "Mjd": "+2348140257660", "Papa": "+22997984266", "Saphir": "+23793195666",
              "Johnstone": "+263777128928", "Idohou": "+22961876476", "Vishnu": "+919591590281", "Rufin": "+22990166164",
              "Vikanshi": "+919012677280", "Dinah": "+22951864306", "Casimir": "+918968793478", "Tonton Rufin": "+22967601588",
              "Mr François": "+22997444472"}

phone_dict2 = {1: "+22962747600", 2: "+2348140257660", 3: "+22997984266", 4: "+23793195666",
               5: "+263777128928", 6: "+22961876476", 7: "+919591590281", 8: "+22990166164",
               9: "+919012677280", 10: "+22951864306", 11: "+918968793478", 12: "+22967601588",
               13: "+22997444472"}

message_type: int = display_message_type()
# print(message_type)

# desired_name = ""
# desired_number_list = display_contact_list(phone_dict, phone_dict2)
# desired_message = getMessage()
# print(desired_number_list)
# print(desired_message)


match message_type:
	case 1:
		try:
			systems()
			# website()
			desired_number_list = display_contact_list(phone_dict, phone_dict2)
			instant_sends = []
			for desired_number in desired_number_list:
				desired_name = get_name(desired_number)
				talk('Provide message for' + desired_name)
				desired_message = getMessage()
				instant_sends.append([desired_name, desired_number, desired_message])
			
			for instant_send in instant_sends:
				# print(instant_send)
				sendwhatmsg_instantly(instant_send[1], instant_send[2], 30, True, 15)
				"""moveTo(1330, 680, 0.5)
				leftClick()"""
				print("Successfully Sent!")
				talk("Message Successfully Sent to" + instant_send[0])
			# hotkey('ctrl', 'w')
		
		except:
			print("Error while sending")
			# hotkey('ctrl', 'w')
			talk("Error while sending")
	
	case 2:
		try:
			systems()
			# website()
			desired_number_list = display_contact_list(phone_dict, phone_dict2)
			plans = []
			for desired_number in desired_number_list:
				planned_details = sendProgrammedDetails()
				desired_name = get_name(desired_number)
				desired_message = getMessage()
				plans.append([desired_name, desired_number, list(planned_details.values()), desired_message])
			
			for plan in plans:
				# print(plan)
				sendwhatmsg(plan[1], plan[3], plan[2][0], plan[2][1], 30, True, 15)
				"""moveTo(1330, 680, 0.5)
				leftClick()"""
				print("Successfully Sent !")
				talk("Message Successfully Sent to!" + plan[0])
			# hotkey('ctrl', 'w')
		except:
			print("Error while sending message")
			# hotkey('ctrl', 'w')
			talk("Error while sending message")
	
	case 3:
		try:
			systems()
			# website()
			diffList = display_contact_list(phone_dict, phone_dict2)
			desired_message = getMessage()
			for desired_number in diffList:
				sendwhatmsg_instantly(desired_number, desired_message, 30, True, 15)
				"""moveTo(1330, 680, 0.5)
				leftClick()"""
				print("Successfully Sent!")
				talk("Message Successfully Sent to the diffusion list")
			# hotkey('ctrl', 'w')
		except:
			print("Error while sending message to the diffusion list")
			# hotkey('ctrl', 'w')
			talk("Error while sending message to the diffusion list")
	
	case 4:
		try:
			systems()
			# website()
			desired_number_list = display_contact_list(phone_dict, phone_dict2)
			imgs = []
			for desired_number in desired_number_list:
				desired_name = get_name(desired_number)
				desired_img = get_img()
				talk('Provide message for' + desired_name)
				desired_message = getMessage()
				imgs.append([desired_name, desired_number, desired_img, desired_message])
			
			for img in imgs:
				print(img)
				sendwhats_image(receiver=img[1], img_path=img[2], caption=img[3], wait_time=30, tab_close=True, close_time=15)
				"""moveTo(1330, 680, 0.5)
				leftClick()"""
				print("Image Successfully Sent!" + img[0])
				talk("Message Successfully Sent to" + img[0])
			# hotkey('ctrl', 'w')
		except:
			print("Error while sending the image")
			# hotkey('ctrl', 'w')
			talk("Error while sending the image")
