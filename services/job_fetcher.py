# services/job_fetcher.py
import requests

class JobFetcher:
    def __init__(self, api_endpoint):
        self.api_endpoint = api_endpoint

    def fetch_jobs(self, query_params=None):
        response = requests.get(self.api_endpoint, params=query_params)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()