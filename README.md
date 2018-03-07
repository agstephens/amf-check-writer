# ncas-amf-check-writer

### download_from_drive.py ###

Usage: `python download_from_drive.py <output directory>`.

This script recursively finds all spreadsheets under a folder in Google Drive
and save sheets from each as a .tsv file (the root folder ID is hardcoded in
`amf-compliance-checker/download_from_drive.py`).

The directory structure of the Drive folder is preserved, and a directory for
each spreadsheet is created. The individual sheets are saved as
`<sheet name>.tsv` inside the spreadsheet directory.

#### Authentication ####

Follow the instructions on the Google site to get credentials for the Sheets
and Drive APIs:

https://developers.google.com/sheets/api/quickstart/python

https://developers.google.com/drive/v3/web/quickstart/python

Put the downloaded `client_secret.json` files at `client_secrets/sheets.json`
and `client_secrets/drive.json`.

When running the script for the first time a web browser will be opened for you
to verify access to your Google account. To avoid this run the script as
`python downloaded <out dir> --noauth_local_webserver` - you will then need to
visit a webpage and enter a verification code (the order of arguments is
important here).
