import pandas as pd
import dmiapi

client = dmiapi.DmiApiClient()

obs_response = client.observations(2619856)
obs = pd.DataFrame(obs_response['observations']).set_index('time')
obs.to_csv('observations_{}.csv'.format(obs.index.max().strftime('%Y%m%d%H%M')))

forecast_response = client.forecasts(2619856)
forecasts = pd.DataFrame(forecast_response['forecasts']).set_index('time')
forecasts.to_csv('forecasts_{}.csv'.format(forecasts.index.min().strftime('%Y%m%d%H%M')))
