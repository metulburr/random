
class EscapeColor():
	def __init__(self):
		self.reset = '\x1b[0m' #reset; clears all colors and styles (to white on black)
		self.bold_on = '\x1b[1m' #bold on 
		self.italic_on = '\x1b[3m' #italics on
		self.underline_on = '\x1b[4m' #underline on
		self.inverse_on = '\x1b[7m' #inverse on; reverses foreground & background colors
		self.strike_on = '\x1b[9m' # strikethrough on
		self.bold_off = '\x1b[22m' # bold off (see below)
		self.italic_off = '\x1b[23m' # italics off
		self.underline_off = '\x1b[24m' # underline off
		self.inverse_off = '\x1b[27m' #inverse off
		self.strike_off = '\x1b[29m'  #strikethrough off

		self.black = '\x1b[30m' #set foreground color to black
		self.red = '\x1b[31m' #set foreground color to red
		self.green = '\x1b[32m' #set foreground color to green
		self.yellow = '\x1b[33m' #set foreground color to yellow
		self.blue = '\x1b[34m' #set foreground color to blue
		self.purple = '\x1b[35m' #set foreground color to magenta (purple)
		self.cyan = '\x1b[36m' #set foreground color to cyan
		self.white = '\x1b[37m' #set foreground color to white
		self.default_white = '\x1b[39m' #set foreground color to default (white)

		self.light_black = '\x1b[1;30m' #set foreground color to black
		self.light_red = '\x1b[1;31m' #set foreground color to red
		self.light_green = '\x1b[1;32m' #set foreground color to green
		self.light_yellow = '\x1b[1;33m' #set foreground color to yellow
		self.light_blue = '\x1b[1;34m' #set foreground color to blue
		self.light_purple = '\x1b[1;35m' #set foreground color to magenta (purple)
		self.light_cyan = '\x1b[1;36m' #set foreground color to cyan
		self.light_white = '\x1b[1;37m' #set foreground color to white
		self.light_default_white = '\x1b[1;39m' #set foreground color to default (white)

		self.Bblack = '\x1b[40m' #set background color to black
		self.Bred = '\x1b[41m' #set background color to red
		self.Bgreen = '\x1b[42m' #set background color to green
		self.Byellow = '\x1b[43m' #set background color to yellow
		self.Bblue = '\x1b[44m' #set background color to blue
		self.Bpurple = '\x1b[45m' #set background color to magenta (purple)
		self.Bcyan = '\x1b[46m' #set background color to cyan
		self.Bwhite = '\x1b[47m' #set background color to white
		self.default_black = '\x1b[49m' #set background color to default (black)

color = EscapeColor()
print(color.blue + 'stringer' + color.reset)
