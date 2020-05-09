# weight
Transfer weight and body fat percentage from Withings to Fitbit.  
[image]

This repository covers the blue area.

## Settings
This system need to set there enviroment.

| name                 | value         |
| -------------------- | ------------- |
| _WITHINGS_CLIENT_ID  | client_id     |
| _WITHINGS_CONS_SECRE | client_secret |

To Access Withing's APIs．  
See details, [click hera](https://developer.withings.com/oauth2/#)


| name                  | value                                                 |
| --------------------- | ----------------------------------------------------- |
| _FITBIT_USER_ID       | user_id                                               |
| _FITBIT_AUTHORIZATION | Authorization <br>  ex : Baser access_token_here..... |

To Access Fitbit APIs.  
See details , [ click here ]( https://dev.fitbit.com/build/reference/web-api/oauth2/ )  
This system use OAuth2 (Implicit Grant)

| name             | value                        |
| ---------------- | ---------------------------- |
| _GCP_PROJECT_ID  | project id                   |
| _GCP_KEY_NAME    | Secret Manager's key name    |
| _GCP_KEY_VERSION | Secret Manager's key version |

## Technologies

- GitHub
  - actions
- Python
  - falcon
- GCP
  - Cloud Run
  - Secret Manager
  - Cloud Storage
  - Cloud Scheduler 


