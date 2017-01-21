import sys
import pickle

class Margaret:
	def __init__(self):
		self.messages = dict()
		self.deserialize()
		try:
			self.messages = self.deserialize()
			
		except FileNotFoundError:
			pass

	def add_messages_to_Mary(self, name, message):
			try:
				self.messages[name].append(message)

			except KeyError:
				self.messages[name] = []
				self.messages[name].append(message)

			self.serialize()
			print(self.messages)

	def remove_messages(self, name, message):
		try:

			  self.messages[name].remove(message)
		except KeyError:
				pass

		self.serialize()

	def delete_list_of_messages(self, name):
		try:
			del self.messages[name]

		except KeyError:
			pass
		self.serialize()
		print(self.messages)

	def serialize(self):
			with open('margaret.txt', 'wb+') as f:
				pickle.dump(self.messages, f)


				"""to save messages"""

			with open('margaret.txt', 'rb') as f:
				binary = f.read()

				return binary

	def deserialize(self):
		try:
			with open('margaret.txt', "rb+") as f:
				self.messages = pickle.load(f)
				"""to open files"""
		except EOFError:
			pass

		return self.messages


if __name__ == '__main__':

	ma = Margaret()

	program_name = sys.argv[0]
	print(program_name)
	arguments = sys.argv[1:]

# 	if arguments[1] == "add":
	ma.add_messages_to_Mary("Margaret", arguments[0])

# 	if arguments[0] == "remove":
# 		ma.remove_messages(arguments[1], arguments[2])
	if arguments[0] == "ls":
		print(ma.messages)

	if arguments[0] == "delete":
		ma.delete_list_of_messages(arguments[1])
		
