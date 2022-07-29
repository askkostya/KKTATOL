from libfptr10 import IFptr
import sys
import time

fptr = IFptr("")


def connectToKKT():
	if len(sys.argv) == 3:  # Передан IP адрес и порт
		fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_PORT, str(IFptr.LIBFPTR_PORT_TCPIP))
		fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPADDRESS, sys.argv[1])
		fptr.setSingleSetting(IFptr.LIBFPTR_SETTING_IPPORT, sys.argv[2])
		fptr.applySingleSettings()
	i = 1
	while i < 10:
		fptr.open()
		if fptr.isOpened():
			return 1
		else:
			time.sleep(5)
			i = i + i


def rebootKKT():
	fptr.deviceReboot()


def main():
	if len(sys.argv) == 1:
		print("No parameter")
		sys.exit()
	connectResult = connectToKKT()
	if connectResult == 1:
		rebootKKT()
	else:
		print("No connection")
	fptr.close()


if __name__ == '__main__':
	main()
