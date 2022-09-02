import sys

from integration_testing_environment.utils.content.content_save import open_content_and_start
from integration_testing_environment.utils.exception.exceptions import ITEContentFileException


def content_init(ite_instance):
    ite_instance.file_from_output_content = open_content_and_start()
    try:
        if ite_instance.file_from_output_content is not None:
            if ite_instance.file_from_output_content.get("program_buffer") is not None:
                ite_instance.program_buffer = \
                    int(ite_instance.file_from_output_content.get("program_buffer"))
    except ITEContentFileException as error:
        print(repr(error), file=sys.stderr)

