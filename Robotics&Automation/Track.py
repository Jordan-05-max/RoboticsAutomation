import phonenumbers
from phonenumbers import geocoder


def locate(num: str):
	phone_number = phonenumbers.parse(num)
	print("\nPhone numbers location\n")
	geo = geocoder.description_for_number(phone_number, "en")
	return geo


print(locate("+918360238249"))
print(locate("+22962747600"))
