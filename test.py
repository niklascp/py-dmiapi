import asyncio
from dmiapi import DmiApi 

async def run():
	forecast = await DmiApi.forecast(2619856)
	for t in forecast['timeserie']:
		print(t['time'], t['temp'])

loop = asyncio.get_event_loop()  
loop.run_until_complete(run())  
loop.close()  
