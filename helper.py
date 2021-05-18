import argparse

def parse_args():
    """
    define shell arguments
    ref_seq_id : reference sequence ID
    server_base_url: base url for the API

    If the arguments are not provided, they take the default values
    """
    parser = argparse.ArgumentParser(
        description='script to access reference sequence metadata in ENA using GA4GH refget API')
    parser.add_argument('--ref_seq_id',
        required=False,
        help='reference sequence ID',
        type=str,
        default='3050107579885e1608e6fe50fae3f8d0')
    parser.add_argument('--server_base_url',
        required=False,
        help='server base url',
        type=str,
        default='https://www.ebi.ac.uk/ena/cram')
    args = parser.parse_args()
    return(args)