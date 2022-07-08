import os
from pprint import pprint
from dorks import leackage_search, google_search
import argparse

serpstack_token = os.environ.get('serpstack_token', '')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--auto-dork-domain', dest='domain',
                        help='Search for some leakages automatically (takes 2 requests). \nRequires domain')
    parser.add_argument('--query',
                        help='Pass custom google query')
    args = parser.parse_args()

    if not args.domain and not args.query:
        print('Get help with --help')

    if args.domain:
        google_report = leackage_search(
            domain=args.domain,
            token=serpstack_token
        )
        pprint(google_report)

    if args.query:
        google_report = google_search(
            query=args.query,
            token=serpstack_token
        )
        pprint(google_report)



