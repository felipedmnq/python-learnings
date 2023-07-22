class HTTPRequest:
    def __init__(
        self,
        url: str,
        body: dict = None,
        headers: dict = None,
        query_params: dict = None,
        path_params: dict = None,
    ) -> None:
        self.url = url
        self.body = body
        self.headers = headers
        self.query_params = query_params
        self.path_params = path_params
