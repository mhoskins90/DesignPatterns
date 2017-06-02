# command
class Command:
	def __init__(self, receiver, commandNumber):
		self.receiver = receiver
		self.commandNumber = commandNumber
	def execute_specific(self):
		self.receiver.execute(self.commandNumber)
# invoker
class Invoker:
	def __init__(self):
		self.commandList = []
	def add_command(self, command):
		self.commandList.append(command)
	def execute_all(self):
		for cmd in self.commandList:
			cmd.execute_specific()
	def undo_command_specific(self, command):
		self.commandList.remove(command)
	def undo_command(self):
		self.commandList.pop()

# receiver
class Receiver:
	def execute(self, commandNumber):
		print("Executed command" , commandNumber)


invoker = Invoker()
reciever = Receiver()
command1 = Command(reciever, 1)

invoker.add_command(command1)

command2= Command(reciever, 2)
invoker.add_command(command2)
invoker.execute_all()
undo = input("do you want to undo last command? Y|N:    ")
if undo.lower() =='y':
	invoker.undo_command()
	print('command removed')

if len(invoker.commandList) >1:
	word="are"
	plural="commands"
else:
	word='is'
	plural='command'
	
print('')
print('-'*20)
print('Final Execution:')
print('-------There {0} {1} {2} saved-------'.format(word, len(invoker.commandList), plural))
invoker.execute_all()
