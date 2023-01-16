#!/home/qq/Applications/miniconda3/bin/python

import argparse
import sys

import cchardet
import requests
from bs4 import BeautifulSoup
from lxml import etree


def list_of_streams(nickname, file_output='/home/qq/.local/share/qq/list-of-streams', separator=' | ', stdout=1, appending=0, rewrite=0):
    nickname = nickname.lower()
    domen = 'https://m.twitch.tv'
    response = requests.get(f'{domen}/{nickname}/videos?filter=all')
    result = cchardet.detect(response.content)
    soup = BeautifulSoup(response.content, 'lxml',
                         from_encoding=result["encoding"])
    dom = etree.HTML(str(soup))

    if appending:
        with open(file_output, mode='r') as f:
            streams_from_file = f.read().split('\n')

    streams_list = []
    elements = dom.xpath(
        '/html/body/div/div/div/div[1]/main/div[3]/div[2]/div[2]/div/div')
    for element in elements:
        link = element.xpath(
            'article/div/div/div[1]/div[1]/a')[0].attrib['href']
        title = element.xpath(
            'article/div/div/div[1]/div[1]/a/p')[0].attrib['title']
        game_name = element.xpath(
            'article/div/div/div[1]/div[2]/a[2]/p/button')[0].text
        streams_list.append(separator.join(
            [nickname, game_name, title, domen+link]))

    if stdout:
        return sys.stdout.write('\n'.join(streams_list))

    if appending:
        streams_list = list(set(streams_list) - set(streams_from_file))
        streams_list.append('\n')
        print(f"Appending to the file: {file_output}")
        with open(file_output, mode='a') as f:
            f.write('\n'.join(streams_list))

    if rewrite:
        streams_list.append('\n')
        print(f"Rewriting the file: {file_output}")
        with open(file_output, mode='w') as f:
            f.write('\n'.join(streams_list))

# import concurrent.futures
# import requests

# def fetch_data():
#     # make a request to a website
#     response = requests.get('https://www.example.com')
#     return response.text

# def prepare_data():
#     # prepare some data in the background
#     return 'prepared data'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     # Submit the fetch_data function to be run in the background
#     data_future = executor.submit(fetch_data)

#     # Do some other work
#     prepared_data = prepare_data()

#     # Wait for the fetch_data function to complete and get the result
#     website_data = data_future.result()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--nickname",
                        help="nickname of the streamer", required=True)
    parser.add_argument(
        "-o", "--output", default='/home/qq/.local/share/qq/list-of-streams', help="file for the output")
    parser.add_argument("-s", "--separator", default=' | ',
                        help="which separator to use")
    parser.add_argument("-S", "--stdout", action="store_true",
                        help="pass result to stdout")
    parser.add_argument("-A", "--append", action="store_true",
                        help="appending result to the file")
    parser.add_argument("-R", "--rewrite", action="store_true",
                        help="rewrite the file with result")
    args = parser.parse_args()

    list_of_streams(
        nickname=args.nickname,
        file_output=args.output,
        separator=args.separator,
        stdout=args.stdout,
        appending=args.append,
        rewrite=args.rewrite
    )
