# demo-streamlit-penguins

- Code: <https://github.com/SamEdwardes/demo-streamlit-penguins>
- Deployment: <https://colorado.rstudio.com/rsc/demo-streamlit-penguins/>

![screenshot](imgs/app-screenshot.png)

## Usaage

To run the app locally:

```bash
source venv/bin/activiate
pip install -r app/requirements.txt
streamlit run app/app.py
```

## Deployment

The app is automatically deployed to RStudio connect using git backed deployment. Make any changes to the code, then run the following:

```bash
rsconnect write-manifest streamlit \
  --overwrite \
  --python venv/bin/python \
  --entrypoint app \
  app
```

> ⚠️ Remember to update the `app/requirements.txt` file if you add any new packages. 
