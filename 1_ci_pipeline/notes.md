## Installation

1. move to the assesment dir `cd 1_ci_pipeline`
2. build docker img `docker build -t app:latest .`

## Run the app
1. run it with `docker run -d -p 5000:5000 app`
2. Access `http://127.0.0.1:5000`. You should see the following:

```json
{
    "resources_uris": {
        "user": "/users/\<username\>",
        "users": "/users"
    },
    "current_uri": "/"
}
```