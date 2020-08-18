# currency_service

### How to run: 
1. `./run.sh`
2. To check: `curl "localhost:5000/get_rates?curr_from=aed&curr_to=usd"`

### Input example:
```
{
  "curr_from": "USD",
  "curr_to": "AED"
}
```

### Output example:

```
{
  "rate": 0.2281707346846669
}
```
