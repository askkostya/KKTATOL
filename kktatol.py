from libfptr10 import IFptr
import sys
import datetime
import time

fptr = IFptr("")

i = 1
while i < 10:
	fptr.open()
	if fptr.isOpened():
		break
	time.sleep(5)
	i = i+i


def deltadate(paramAsDateTime):
	now = datetime.datetime.now()
	deltaindays = (paramAsDateTime - now).days
	if deltaindays < -10000:
		return 0
	else:
		return deltaindays + 1


def getDataFromKKT(param):
	# Заводской номер ККТ
	if param == "1":
		fptr.setParam(IFptr.LIBFPTR_PARAM_DATA_TYPE, IFptr.LIBFPTR_DT_SERIAL_NUMBER)
		fptr.queryData()
		print(fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER))
	# РН ККТ
	if param == "2":
		fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_REG_INFO)
		fptr.fnQueryData()
		print(fptr.getParamString(1037))
	# Серийный номер ФН
	if param == "3":
		fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_FN_INFO)
		fptr.fnQueryData()
		print(fptr.getParamString(IFptr.LIBFPTR_PARAM_SERIAL_NUMBER))
	# Осталось дней до окончания ФН
	if param == "4":
		fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_VALIDITY)
		fptr.fnQueryData()
		print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME)))
	# Возраст в днях первого не отправленного документа в ФН
	if param == "5":
		fptr.setParam(IFptr.LIBFPTR_PARAM_FN_DATA_TYPE, IFptr.LIBFPTR_FNDT_OFD_EXCHANGE_STATUS)
		fptr.fnQueryData()
		print(deltadate(fptr.getParamDateTime(IFptr.LIBFPTR_PARAM_DATE_TIME))*(-1))


try:
	getDataFromKKT(sys.argv[1])
except IndexError:
	print("No parameter")

fptr.close()
