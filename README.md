# demo-streamlit-penguins

Publish a Streamlit dashboard to RStudio Connect.

## Deploy

First add a new server:

```bash
rsconnect add \
    --server https://colorado.rstudio.com/rsc/ \
    --name colorado.rstudio.com \
    --api-key $CONNECT_API_KEY
```

Then deploy the app to the server:

```bash
rsconnect deploy streamlit \
    --server https://colorado.rstudio.com/rsc/ \
    --python ./venv/bin/python \
    --entrypoint app.py \
    app/
```
