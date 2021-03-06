# -*- coding: UTF-8 -*-
#
# V0.153
# manque scenario et panel securité
# manque devices -temp, batterie, humidité
# doit marcher et a tester on/off - switch et HC 
# param à faire ip et port
#
from lisa.server.plugins.IPlugin import IPlugin
import gettext
import inspect
import os
import requests
import json


class Domoticz(IPlugin):
	def __init__(self):
		super(Domoticz, self).__init__()
		self.configuration_plugin = self.mongo.lisa.plugins.find_one({"name": "Domoticz"})
		self.path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(
		inspect.getfile(inspect.currentframe()))[0],os.path.normpath("../lang/"))))
		self._ = translation = gettext.translation(domain='domoticz',
			localedir=self.path,
                        languages=[self.configuration_lisa['lang']]).ugettext
#
#
#
	def devices(self, jsonInput):
		json_data=open('domoticz.json')
		data = json.load(json_data)
		res1 = data['param_dz']
	
		if jsonInput['outcome']['entities']['wit/location']['value'] :
			location = jsonInput['outcome']['entities']['wit/location']['value']
		else:
			bod = "pas de lieu"
		
		
		if jsonInput['outcome']['entities']['wit/temperature']['value'] :
			location = jsonInput['outcome']['entities']['wit/temperature']['value']
		else:
			bod = "pas de temperature"
#
		idex= location + "_" + on_off
		for rs in res1:
		  if rs['ids'] == idex :
			  rss = rs
			  bod = rss(boy)
		#	http://192.168.0.3:8080/json.htm?type=devices&filter=temp&rid=74
		# parse result : Temp	
		return {"plugin": "Domoticz",
			"method": "devices",
			"body": bod
		}

	
	def switchlight(self, jsonInput):
		json_data=open('domoticz2.json')
		data = json.load(json_data)
		res1 = data['param_dz']
	#
		if jsonInput['outcome']['entities']['wit/location']['value'] :
			location = jsonInput['outcome']['entities']['wit/location']['value']
		else:
			bod = "pas de lieu"

		if jsonInput['outcome']['entities']['wit/on_off']['value'] :
			on_off = jsonInput['outcome']['entities']['wit/on_off']['value']
		else:
			bod = "pas de on/off"
#
		idex= location + "_" + on_off
		for rs in res1:
		  if rs['ids'] == idex :
			  rss = rs
		bod = rss(boy)
		resp = requests.get ('http://192.168.0.3:8080/json.htm?type=command&param=switchlight&idx=%02d&switchcmd=%s&level=0' % (rss[idx],on_off.capitalize()))
		return {"plugin": "Domoticz",
			"method": "switchlight",
			"body": bod
		}
