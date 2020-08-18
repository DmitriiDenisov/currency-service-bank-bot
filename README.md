# currency_service

### How to run: 
1. Clone this repo
2. Create file `token.txt` and put there token from https://fixer.io/
2. (optional) change PORT variable in `run.sh` script
3. `bash ./run.sh`
4. To check: `curl "localhost:5000/get_rates?curr_from=aed&curr_to=usd"`

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
