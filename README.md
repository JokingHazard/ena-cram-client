# ena-cram-client
client code to query the server metadata endpoint of ENA CRAM archive. The endpoint for the ENA is https://www.ebi.ac.uk/ena/cram/ and an example sequence ID is 3050107579885e1608e6fe50fae3f8d0. 

## Installation

This application requires [Python> 3.6](https://www.python.org/downloads/)

clone the repository and cd into the root folder
```sh
cd ena-cram-client
```
Install and activate Python [VirtualEnv](https://docs.python.org/3/tutorial/venv.html) to isolate dependencies

Install required packages
```sh
pip install -r requirements.txt
```
## Run the code
### Optional command-line arguments
> **--ref_seq_id** 
> default value: 3050107579885e1608e6fe50fae3f8d0 
> description: ID parameter of the reference sequence.
> **--server_base_url** 
> default value: https://www.ebi.ac.uk/ena/cram
> description: server url where the API is hosted
> **--log_level** 
> default value: INFO 
> description: logging at or above this level


### Example usage
##### without command-line arguments

```sh
python client.py
```

##### with command-line arguments

```sh
python client.py --ref_seq_id 3050107579885e1608e6fe50fae3f8d0 --server_base_url https://www.ebi.ac.uk/ena/cram --log_level INFO
```

## Note:
* The command-line arguments are optional. If a command-line argument is not provided, it assumes the default value, as defined in the helper file.
* Logs are configured to be displayed on the terminal.
* If an error occurs due to incorrect parameters or other reasons, the error will be available in the logs. Metadata will be None.