import requests
import json
import logging
from helper import parse_args

class ENAClient:

	def __init__(self, server_base_url, ref_seq_id):
		self.server_base_url = server_base_url
		self.metadata_url = "/sequence/{}/metadata"
		self.ref_seq_id = ref_seq_id
		self.headers = {
		'accept': 'application/vnd.ga4gh.refget.v1.0.0+json',
		'charset': 'us-ascii'
		}

	def get_server_metadata(self):
		"""
		returns the json response of the metadata endpoint for the given reference sequence id
		returns None, if an error occurs. The error message is logged 
		"""
		logging.info('requesting metadata for {} from server url {}'.format(self.ref_seq_id,self.server_base_url))
		url = (self.server_base_url+self.metadata_url).format(self.ref_seq_id)
		try:
			response = requests.request("GET", url, headers=self.headers)
			logging.debug('metadata endpoint response for reference sequence ID {}: {}'.format(self.ref_seq_id,response.text))
			if response.status_code == 200:
				response_json = response.json()
				return response_json
			else:
				logging.error('!200 status_code for request response. status_code = {}, reason = {}, response_text = {}'.format(response.status_code, response.reason, response.text))
		except Exception as e:
			logging.error('Exception occured while accessing metadata for reference sequence ID {}. Exception: {}'.format(self.ref_seq_id,str(e)))
		return None			

if __name__ == "__main__":

	# get ref_seq_id, server_base_url, log_level as command line args.
	# If not provided, they take the default values
	args=parse_args()  
	ref_seq_id = args.ref_seq_id
	server_base_url = args.server_base_url
	severity = args.log_level

	# setting native logs of requests and urllib3 to error level to ignore them
	logging.getLogger("requests").setLevel(logging.CRITICAL)
	logging.getLogger("urllib3").setLevel(logging.CRITICAL) 
	logging.basicConfig(level=severity)

	ena = ENAClient(server_base_url=server_base_url, ref_seq_id=ref_seq_id)
	metadata = ena.get_server_metadata()
	logging.info('metadata endpoint response for reference sequence ID {} and server url {} is {}'.format(ref_seq_id,server_base_url,metadata))
	print('.............')
	print('\nreference sequence ID = {}, \nserver url = {} \nMETADATA = {}'.format(ref_seq_id,server_base_url,metadata))