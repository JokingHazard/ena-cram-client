# ena-cram-client
client code to query the server metadata endpoint

## Installation

This application requires [Python 3.x](https://www.python.org/downloads/)

clone the repository and cd into the root folder
```sh
cd ena-cram-client
```
Install and activate Python [VirtualEnv](https://docs.python.org/3/tutorial/venv.html) to isolate dependencies

Install required packages
```sh
pip install -r requirements.txt
```
## Run the App
Run the following command
```sh
python app.py --ref_seq_id 3050107579885e1608e6fe50fae3f8d0 --server_base_url https://www.ebi.ac.uk/ena/cram --log_level INFO
```
### Optional Command line arguments
* **--ref_seq_id**
* **--server_base_url**
* **--log_level**