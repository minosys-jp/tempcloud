#!/usr/bin/python
# -*- coding: utf-8 -*-

import json, datetime, time, struct, binascii, serial, urllib

def parseSHT11(data):
	# 先頭の : を取り除く
	if data[0] != ":":
		return False
	data = data[1:]

	# バイトデータに変換する
	ss = struct.Struct(">BBBBBBHHB")
	data = binascii.unhexlify(data.rstrip())
	parsed = ss.unpack(data);

	# 温度データを温度に変換
	temp = -39.6 + 0.01 * parsed[6]

	# 湿度データを湿度に変換
	hum = -2.0468 + 0.0367 * parsed[7] + -1.5955e-6 * parsed[7] * parsed[7]
	hum = (temp - 25.0) * (0.01 + 0.00008 * parsed[7]) + hum;

	# 現在時刻
	now = datetime.datetime.now()
	current = now.strftime("%Y-%m-%d %H:%M:%S")

	# 結果を返す
	result = {
		"type" : "sht11",
		"datetime" : current,
		"current" : int(time.mktime(now.timetuple())),
		"from" : parsed[0],
		"presence" : parsed[4],
		"status" : parsed[5],
		"temperature" : temp,
		"humidity" : hum
	}
	return result;

def dataPoster(js):
	url = urllib.URLopener();
	url.open("http://www.minosys.com/hems/appenddb.php", js);
	url.close()

# /dev/ttyUSB0 を開く
s = serial.Serial(port = "/dev/ttyUSB0", baudrate = 115200)

while True:
	# 1行読み取る
	data = s.readline()

	# 解釈する
	parsed = parseSHT11(data)

	# 書き込みファイルを開く
	if parsed != False:
		f = open("/tmp/sht11.txt", "a")
		js = json.dumps(parsed, sort_keys=True)
		f.write(js)
		f.write("\n")
		f.close()
		dataPoster(js)
else:
	True

# COM を閉じる
s.close()
