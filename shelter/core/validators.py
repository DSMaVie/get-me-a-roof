def url_is_valid(url: str) -> bool:
    """
    Check if the URL is valid
    """
    return True if url.startswith("http://") or url.startswith("https://") else False


def domain_is_supported(url: str) -> bool:
    """
    Check if the domain is supported
    """
    supported_domains = ["immobilienscout24.de"]  # could be improved for modularity
    return True if any((domain in url) for domain in supported_domains) else False


def validate_url(url: str) -> None:
    """
    Check if the URL is valid and supported
    """
    if not url_is_valid(url):
        raise ValueError("URL is not valid. Please enter a valid URL.")

    if not domain_is_supported(url):
        raise ValueError(
            "Domain is not supported. Please enter a URL from immobilienscout24.de."
        )
