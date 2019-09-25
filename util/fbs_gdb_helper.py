def handle_break(event):
	fame = gdb.selected_frame()
	c = 1
	while fame != None:
		function_name = fame.name()
		pc = fame.pc()
		m = gdb.parse_and_eval(function_name)

		print("{}|0x{:016x}|{}|{}".format(c, pc, function_name, pc-int(m.address)))

		fame = fame.older()
		c = c + 1

		#rip = str(fame.read_register("ddrip"))

	return

def main():
	gdb.execute("set pagination off")
	gdb.execute("set print pretty")
	gdb.events.stop.connect(handle_break)

if __name__ == '__main__':
	main()
