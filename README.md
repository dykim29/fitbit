# Fitbit data

This repo downloads Fitbit data and processes it, for analysis.

## Setting up secret config
In order to use this repo, you need to add a file called `secret_config.json` in the main directory with this format:
```
{
  "client_id": CLIENT_ID,
  "client_secret": CLIENT_SECRET,
  "redirect_url": REDIRECT_URL,
  "auth_url": AUTH_URL, 
  "access_token_url": ACCESS_TOKEN_URL
}
```
The values can be obtained through the Fitbit API dev portal, by registering an app to obtain API client credentials
