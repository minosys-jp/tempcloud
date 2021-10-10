#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, datetime, time, struct, binascii, serial

def parseMAX31855(data):
	# 先頭の : を取り除く
	if data[0] != ":":
		return False
	data = data[1:]

	# バイトデータに変換する
	ss = struct.Struct(">BBBBlB")
	data = binascii.unhexlify(data.rstrip())
	parsed = ss.unpack(data);

	# 温度データを温度に変換
	temp = (parsed[4] >> 18) * 0.25

	# error ビットを解釈
	error = parsed[4] & 0x07

	# 現在時刻
	now = datetime.datetime.now()
	current = now.strftime("%Y-%m-%d %H:%M:%S")

	# 結果を返す
	result = {
		"type" : "max31855",
		"datetime" : current,
		"current" : int(time.mktime(now.timetuple())),
		"from" : parsed[0],
		"presence" : 128,
		"status" : error,
		"temperature" : temp,
		"humidity": 0,
	}
	return result;

# /dev/ttyUSB0 を開く
s = serial.Serial(port = "/dev/ttyUSB0", baudrate = 115200)

while True:
	# 1行読み取る
	data = s.readline()

	# 解釈する
	parsed = parseMAX31855(data)

	# 書き込みファイルを開く
	if parsed != False:
		f = open("/tmp/max31855.txt", "a")
		f.write(json.dumps(parsed, sort_keys=True))
		f.write("\n")
		f.close()
else:
	True

# COM を閉じる
s.close()
