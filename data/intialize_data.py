from zipfile import ZipFile

with ZipFile("wildlife-strikes.zip", 'r') as zip_ref:
    zip_ref.extractall("")

with ZipFile("flight-delays.zip", 'r') as zip_ref:
   zip_ref.extractall("")

with ZipFile("twitter-airline-sentiment.zip", 'r') as zip_ref:
    zip_ref.extractall("")

with ZipFile("usa-airport-dataset.zip", 'r') as zip_ref:
   zip_ref.extractall("")


