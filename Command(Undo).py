# command
class DrawCommand:
	def __init__(self, draw, commandNumber):
		self.draw = draw
		self.commandNumber = commandNumber
	def execute_drawing(self):
		self.draw.execute(self.commandNumber)
# invoker
class InvokeDrawLines:
	def __init__(self):
		self.commandList = []
	def add_command(self, command):
		self.commandList.append(command)
	def draw(self):
		for cmd in self.commandList:
			cmd.execute_drawing()
	def undo_command_specific(self, command):
		self.commandList.remove(command)
	def undo_command(self):
		self.commandList.pop()

# receiver
class DrawALine:
	def execute(self, commandNumber):
		print("Executed command" , commandNumber)


invoke_draw = InvokeDrawLines()
draw_a_line = DrawALine()
draw_command1 = DrawCommand(draw_a_line, 1)

invoke_draw.add_command(draw_command1)
#invoke_draw.click_to_draw()
draw_command2 = DrawCommand(draw_a_line, 2)
invoke_draw.add_command(draw_command2)
invoke_draw.draw()
undo = input("do you want to undo last command? Y|N:    ")
if undo.lower() =='y':
	invoke_draw.undo_command()
	print('command removed')

if len(invoke_draw.commandList) >1:
	word="are"
	plural="commands"
else:
	word='is'
	plural='command'
	
print('')
print('-'*20)
print('Final Execution:')
print('-------There {0} {1} {2} saved-------'.format(word, len(invoke_draw.commandList), plural))
invoke_draw.draw()
