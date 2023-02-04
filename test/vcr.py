import vcr
import os


CASSETTES_DIR = os.path.dirname(os.path.abspath(__file__))
DUMMY_INFO = 'XXXXXXXXXXXX'

custom_vcr = vcr.VCR(
    cassette_library_dir=CASSETTES_DIR + '/fixtures/cassettes',
    filter_headers=[('authorization', DUMMY_INFO)],
    filter_query_parameters=[
        ('api_token', DUMMY_INFO),
        ('api_token_secret', DUMMY_INFO),
    ]
)
