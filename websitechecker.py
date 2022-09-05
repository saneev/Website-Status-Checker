import http.client

def websiteStatus(site):

    '''Checks if a website is available by reading the header via http to the server URL'''

    conn = http.client.HTTPConnection(site)
    conn.request("HEAD", "/")
    r1 = conn.getresponse()
    if r1.status == 200 and r1.reason == 'OK':
        print(f'{site} is Up and Reachable')
        print(
            f'HTTP Response Status Code is "{r1.status}" with reason "{r1.reason}"')
    elif r1.status in range(301,309):
        print(f'{site} is Up and Reachable but a redirect was performed')
        print(
            f'HTTP Response Status Code is "{r1.status}" with reason "{r1.reason}"')
    else:
        print(f'{site} is unreachable, probably down or only using http')
        print(
            f'HTTP Response Status Code is "{r1.status}" with reason "{r1.reason}"')
    conn.close()

if __name__ == '__main__':

    website = str(input(
        "Please enter the website URL to check status\n"))
    websiteStatus(website)


