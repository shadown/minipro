from devices import devices

variants = list()

for i in devices:
	if 'TSOP48' in i['name']:
		if i['variant'] not in variants:
			print i['name'], 'protocol:', i['protocol_id'], 'variant', i['variant']
			variants.append(i['variant'])