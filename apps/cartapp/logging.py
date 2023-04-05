import logging
import re
import json


class LogFormatter(logging.Formatter):
    def format(self, record):
        record.class_name = ""
        session_headers = {}
        if record.args and type(record.args) is dict:
            record.class_name = record.args.get("class_name", "") + " : "
            if "session_headers" in record.args:
                session_headers = record.args["session_headers"]
        record.session_headers = json.dumps(session_headers)

        
        return super().format(record)

logger = logging.getLogger()

ch = logging.StreamHandler()
ch.setFormatter(
    LogFormatter(
        "[ %(levelname)s ] - %(message)s (%(class_name)s%(funcName)s() -> %(filename)s:%(lineno)s) (session headers are: -> %(session_headers)s)"
    )
)

logging.basicConfig(handlers=[ch], level = logging.INFO)
