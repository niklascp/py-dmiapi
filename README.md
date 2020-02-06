## Installation

```pip install dmiapi```

## Data available

- observations
- forecasts

## Usage

The wrapper supports both synchronous and asynchronous methods.

### Synchronous example
```python
import pandas as pd
import dmiapi

client = dmiapi.DmiApiClient()

obs_response = client.observations(station_id = 2619856)
obs = pd.DataFrame(obs_response['observations'])
print('Mean temperature (2 meters above ground):', obs['temperature2m'].mean())
```

### Asynchronous example
```python
import pandas as pd
import dmiapi

async def max_forecast_temp():
    client = dmiapi.DmiApiClient()
    forecasts_response = await client.async_forecasts(location_id = 2619856)
    forecasts = pd.DataFrame(forecasts_response['forecasts'])
    print('Forcasted max. temperature:', forecasts['temp'].max())
```
