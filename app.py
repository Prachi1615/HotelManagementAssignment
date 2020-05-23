class FindHotel():
	def __init__(self):
		self.details = {}
		self.addHotel()

	def addHotel(self):
		hotelName = input("Enter Hotel name: ")
		if self.details.get(hotelName, False):
			print("Hotel already exists")
			self.addHotelAgain()
		else:
			self.details[hotelName]={}
			self.addRoom(hotelName)

	def addRoom(self, hotelName):
		room_no = input("Enter Room Number: ")
		self.details[hotelName][room_no]={"item": [], "itemList": [], "cost": 0}
		i = 0
		while i < 5:
			self.addAllitem(hotelName, room_no)
			i += 1
		self.additemAgain(hotelName, room_no)

	def addAllitem(self, hotelName, roomNo):
		item = input("Enter the item name: ")
		price = input("Enter cost of item in $ (should be a number): ")
		self.details[hotelName][roomNo]["item"].append({item:price})
		self.details[hotelName][roomNo]["itemList"].append(item)
		self.details[hotelName][roomNo]["cost"] += int(price)


	def additem(self, hotelName, roomNo):
		item = input("Enter the item name: ")
		price = input("Enter cost of item in $ (should be a number): ")
		self.details[hotelName][roomNo]["item"].append({item:price})
		self.details[hotelName][roomNo]["itemList"].append(item)
		self.details[hotelName][roomNo]["cost"] += int(price)
		self.additemAgain(hotelName, roomNo)


	def addHotelAgain(self):
		add_hotel = input("Do you want to add a New Hotel (Yes/No): ")
		if add_hotel.lower() == "yes":
			self.addHotel()
		elif add_hotel.lower() == "no":
			self.show()
		else:
			print("Invalid Input")
			self.addHotelAgain()

	def addRoomAgain(self, hotelName):
		add_room = input("Do you want to add more Room(Yes/No): ")
		if add_room.lower() == "yes":
			self.addRoom(hotelName)
		elif add_room.lower() == "no":
			self.addHotelAgain()
		else:
			print("Invalid Input")
			self.addRoomAgain(hotelName)


	def additemAgain(self, hotelName, roomNo):
		add_item = input("Do you want to add more items(Yes/No): ")
		if add_item.lower() == "yes":
			self.additem(hotelName, roomNo)
		elif add_item.lower() == "no":
			self.addRoomAgain(hotelName)
		else:
			print("Invalid Input")
			self.additemAgain(hotelName, roomNo)

	def show(self, budget=0):
		for hotel_hotelName, room_info in self.details.items():
			context = "\nRoom No {0} have the item like {1}, and room rent is ${2}."
			if budget == 0:
				details = '\n\n\nHotel {0} have following rooms\n'.format(hotel_hotelName)
				for room, amenti_info in room_info.items():
					amenti = ', '.join(amenti_info['itemList'])
					cost = amenti_info['cost']
					details += context.format(room, amenti, cost)
				print(details)
			else:
				details = '\n\n\nHotel {0} have following rooms matching your budget\n'.format(hotel_hotelName)
				availability = False
				for room, item_info in room_info.items():
					cost = item_info['cost']
					if cost <= budget:
						item = ', '.join(item_info['itemList'])
						availability = True
						details += context.format(room, item, cost)
				if availability:
					print(details)
				else:
					print("\n\n\nNo room available for your budget in hotel {0}".format(hotel_hotelName))
		if budget == 0:
			self.getUserBudget()

	def getUserBudget(self):
		print("\n-----------------------------------------------------------\n")
		budget = int(input("Please enter your budget: "))
		if budget > 1:
			self.show(budget)
		else:
			print("Invalid Budget range")
			self.getUserBudget()

print("\n-----------------------------------------------------------\n")
print("                   WELCOME TO OUR PORTAL")
print("\n-----------------------------------------------------------\n")
FindHotel()
