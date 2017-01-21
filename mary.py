import sys
import pickle

class Mary:
	def __init__(self):
		self.messages = dict()
		self.deserialize()
		try:
			self.messages = self.deserialize()
			
		except FileNotFoundError:
			pass

	def add_messages_to_margaret(self, name, message):
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
	def delete_messages(self, name):
		try:
			del self.messages[name]
		except KeyError:
			pass

		self.serialize()


	def serialize(self):
		with open('mary.txt','wb+') as f:
			pickle.dump(self.messages, f)

		with open('mary.txt', 'rb') as f:
			binary = f.read()

		return binary

	def deserialize(self):
		try:

			with open('mary.txt', 'rb+') as f:
				
				self.messages = pickle.load(f)
		except KeyError:
			pass

		return self.messages

if __name__ == '__main__':

	mary = Mary()

	program_name = sys.argv[0]
	print(program_name)
	arguments = sys.argv[1:]

	
	mary.add_messages_to_margaret("Mary", arguments[0])

	if arguments[0] == "remove":
		mary.remove_messages(arguments[1], arguments[2])
	if arguments[0] == "ls":
		print(mary.messages)

	if arguments[0] == "delete":
		mary.delete_list_of_messages(arguments[1])
		
