# demo-streamlit-penguins

Publish a Streamlit dashboard to RStudio Connect.

## Run the app

To run the app locally:

```bash
source venv/bin/activiate
pip install -r app/requirements.txt
streamlit run app/app.py
```

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
