import subprocess
import argparse
import time

def get_touchpad_id():
	command = "xinput list"
	proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	out, err = proc.communicate()
	
	if not err:
		out_split = out.split()
		touchpad = b'TouchPad'
		i = None
		for ind in out_split:
			if ind == touchpad:
				i = out_split.index(touchpad)
		val = out_split[i+1]
		if val.startswith(b'id='):
			return val[3:].decode()
		else:
			raise Exception('expected id value, index is not id')	
	else:
		raise Exception(err)
		
def get_touchpad_status(ID):
	command = "xinput list-props {}".format(ID)
	proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
	out, err = proc.communicate()
	if not err:
		out_split = out.split()
		enabled = b'Enabled'
		i = None
		for ind in out_split:
			if ind == enabled:
				i = out_split.index(enabled)
		val = out_split[i+2].decode()
		if val in ['0', '1']:
			return val
		else:
			raise Exception('expected 1 or 0')
	else:
		raise Exception(err)
		
def execute(ID, stat):
	command = 'xinput --set-prop {} "Device Enabled" {}'.format(ID, stat)
	print(command)
	proc = subprocess.Popen(command.split())

touchpad_id = get_touchpad_id()
touchpad_status = get_touchpad_status(touchpad_id)

parser = argparse.ArgumentParser(description="Toggle Touch Pad Arguemnts")
parser.add_argument('-1', '--on', action='store_true',
	help='turn touchpad on')
parser.add_argument('-0', '--off', action='store_true',
	help='turn touchpad off')
args = vars(parser.parse_args())

if args['on']:
	print('turn touchpad on')
	execute(touchpad_id, 1)
elif args['off']:
	print('turn touchpad off')
	execute(touchpad_id, 0)
elif not args['on'] and not args['off']:
	print('no argument')
	if touchpad_status:
		execute(touchpad_id, 0)
	else:
		execute(touchpad_id, 1)
