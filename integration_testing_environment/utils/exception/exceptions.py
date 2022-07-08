class ITEException(Exception):
    pass


class ITEAddCommandException(ITEException):
    pass


class ITESendHtmlReportException(ITEException):
    pass


class ITETestExecutorException(ITEException):
    pass
