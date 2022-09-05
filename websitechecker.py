import http.client


def websiteStatus(site):

    conn = http.client.HTTPConnection(site)
    conn.request("HEAD", "/")
    r1 = conn.getresponse()
    if r1.status == 200 and r1.reason == 'OK':
        print(f'{site} is Up and Reachable')
    else:
        print(f'{site} is unreachable, probably down or only using http')
        print(f'HTTP Response Status is "{r1.status}" with reason "{r1.reason}"')


if __name__ == '__main__':

    website = str(input(
        "Please enter the website URL to check status\n in the format <www.google.com>"))
    websiteStatus(website)


