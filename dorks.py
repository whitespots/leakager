import requests


def google_search(query, token):
    report_data = {}

    params = {
        'access_key': token,
        'query': query
    }

    api_result = requests.get('http://api.serpstack.com/search', params, verify=False)
    try:
        raw_list = api_result.json().get('organic_results')
        for search_result in raw_list:
            report_data.update({
                search_result['title']: {
                    'url': search_result['url'],
                    'cache': search_result['cached_page_url']
                }
            })
    except Exception as ex:
        print(ex)

    return report_data


def leackage_search(domain, token):
    report_data = {}

    queries = [
        f'intext:{domain} site:ideone.com | site:codebeautify.org | site:codeshare.io | ' 
        'site:codepen.io | site:repl.it | site:justpaste.it | site:pastebin.com | ' 
        f'site:jsfiddle.net | site:trello.com | site:gist.githubusercontent.com',
        f'site:.{domain} -inurl:robots | ext:conf | ext:cnf | ext:inf | ext:cfg | ext:txt | ext:ini | ' 
        'ext:sql | ext:dbf | ext:mdb | ext:bak | ext:old | ext:log | ext: pem | ext:p12 | ' 
        f'filename:.bash_history | filename:dbpasswd | filename:.pgpass'
    ]

    for query in queries:
        params = {
            'access_key': token,
            'query': query
        }

        api_result = requests.get('http://api.serpstack.com/search', params, verify=False)
        try:
            raw_list = api_result.json().get('organic_results')
            for search_result in raw_list:
                report_data.update({
                    search_result['title']: {
                        'url': search_result['url'],
                        'cache': search_result['cached_page_url']
                    }
                })
        except Exception as ex:
            print(ex)

        return report_data
