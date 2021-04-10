import requests
import base64
from time import sleep


class ItemFetchGenericError(Exception):
    pass


class ItemFetchTooManyRequestsError(Exception):
    pass


class ItemFetcher(object):
    url = 'https://eluv.io/items/{}'
    simultaneous_request_limit = 5
    
    def __init__():
        self.items = {}
        self.request_delay = 1 # in seconds
        self.request_count = 0

    def fetch_items(item_ids):
        for item_id in item_ids:
            if item_id in self.items:
                # Skip items we've requested already
                continue

            if self.request_count >= self.simultaneous_request_limit:
                # Since only 5 simultaneous requests can
                # be made, delay the next request to
                # avoid getting 429's
                sleep(self.request_delay)
                self.request_count = 0

            try:
                self._fetch_item(item_id)
            except ItemFetchTooManyRequestsError:
                # If we've received a 429 anyway,
                # increase the delay to avoid
                # them going forward
                self.request_delay += 1
                sleep(self.request_delay)
            except ItemFetchGenericError:
                print(str(e))

        return self.items

    def _fetch_item(self, id):
        headers = {'Authorization': base64.b64encode(id)}
        response = requests.get(self.url.format(id), headers=headers)

        self.request_count += 1

        if response.status_code == 429:
            raise ItemFetchTooManyRequestsError()
        elif response.ok:
            items[id] = response.json()
        else:
            raise ItemFetchException(
                'Encountered error while fetching item {}: {}').format(
                    id, response.text
                )


if __name__ == "__main__":
    item_ids = [
        'XLqJcYWUcoOFoWaQTzeUgRizPSr',
        'pxKSjVRNTzObVtWVuqGHZnwkEvB',
        'XEDpjDsxfdAaqdoxeDHELfIhknL',
        'WhmWGCeBelypzbQpuRSFkDDzOxn',
        'kzrGuFfznRBNrCtIsdkdWquRLQg',
        'tXeSmWuaEUXocrllJVkMTYPFbBX',
        'jyqPeAXzsfEufwOPEINxMyOtQxY',
        'XPfLyGarrxMvdUlSblQGWDBvtVq',
        'BIQpdWLmPDFJNjmBiDPBHqzMbwV',
        'nbrbHprRJgdZGZiaKlopSEizcLY',
        'NiVZZLlqXHGqbJBxCFGmkMOJGoI',
        'OVEgORdQLOmSEEJIorcLgWvVUAR',
        'OVEgORdQLOmSEEJIorcLgWvVUAR',
        'OVEgORdQLOmSEEJIorcLgWvVUAR',
        'ZhXBlywsWZAjokZnhUOWTiXVBxW',
        'SngIaEwQqtHhUrvYEncBAQudXRK',
        'SnVfgLEByWhBdNDFGZXGuvfCySD',
        'UdlHWgMZqvnqekPVheAQmiCCYXo',
        'oGFOvnHyQpjjicyLlzmLlCzrxUN',
        'zSWwMGIQNOjkNqUAwAjqsJdgJGz',
        'jJWFldjIVVIjXviaHHxDuJZoYJX',
        'YWxNErrgatZivdNaZLQjPRWmFPQ',
        'iFLsZkMjaQhOwGqCJKoTxXfZQxh',
        'CathkwOPqxpfcyczVHfbQmaTKBb',
        'kSjbQsAuYCMplUMgrDlLlEoIOUJ',
        'cNovhUNOgIhhiKMyqJPxeeYWwdG',
        'cNovhUNOgIhhiKMyqJPxeeYWwdG',
        'DjsmEQXMHMWQbgEGUhgRFlCJuxi',
        'NSundKLMPutPkjPziDOdCPtXvyf',
        'uEdDYGQzqlbSRQCzkzIDNMAvXPX',
        'uRwFXdLBYDsjdOHPAgNkxtWrQBB',
        'uRwFXdLBYDsjdOHPAgNkxtWrQBB',
        'FtnbSVDivzXUHYnJTUvvZaFKYCc',
        'lWORFdelwiZcCQzKpDKKCPQolSb',
        'CEmMhulAaYQELuEfoARTzIAuvPi',
        'LAicIPQfSmRnWUkGjielpuNfdrC',
        'qbjVWmEZLZyoJwBwBgnyEYwRiRA',
    ]

    fetcher = ItemFetcher()
    items = fetcher.fetch_items(item_ids)

    print(items)
