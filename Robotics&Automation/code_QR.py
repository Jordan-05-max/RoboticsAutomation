import qrcode as qr

# data = "https://www.kipper.ai/dashboard?location=ai-detector"
data = input("Enter the data for encapsulation: ")
# img = qr.make(data)
saving_file = input("How do you want to save it? ")

# img.save("./kipper.png")

def qrmaker(data, saveas):
	img = qr.make(data)
	img.save(f"./{saveas}.png")


qrmaker(data, saving_file)

