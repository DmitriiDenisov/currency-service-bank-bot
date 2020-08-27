# currency_service

### How to run: 
1. Clone this repo
2. `docker login` (in case of ` Got permission denied while trying to connect...` then `sudo chmod 666 /var/run/docker.sock`)
3. Create file `.env` and put there token (from https://fixer.io/) and port, it should look like this:
```
TOKEN=abcd
PORT=5004
```
(optional) change PORT variable in `run.sh` script

4. `bash ./run.sh`
5. To check: `curl "localhost:5004/get_rates?curr_from=aed&curr_to=usd"`

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
