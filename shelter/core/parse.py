import itertools
import re

import httpx
from bs4 import BeautifulSoup


def get_url(url: str) -> str:
    with httpx.Client() as client:
        response = client.get(url)

        if response.status_code != 200:
            raise ValueError(f"Error {response.status_code} fetching page ({url})!")

        return response.text


def parse_immoscout_page(page: str):
    soup = BeautifulSoup(page, "html.parser")

    qa_string = soup.find_all(class_=re.compile("is24qa*"))
    qa_string = [string.striped_strings for string in qa_string]
    qa_string = " ".join(itertools.chain.from_iterable(qa_string))

    inetspeed_string = soup.find(id="telekomSpeedCheckTarif").find_previous_siblings(
        "span"
    )
    inetspeed_string = list(speed.stripped_strings for speed in inetspeed_string)
    inetspeed_string = next(itertools.chain.from_iterable(inetspeed_string))

    address = list(soup.find_all(class_="address-block")[0].stripped_strings)
    address = " ".join(address)

    title = soup.find(id="expose-title").get_text()

    return f"{title}\n{address}\n{qa_string} {inetspeed_string}"
