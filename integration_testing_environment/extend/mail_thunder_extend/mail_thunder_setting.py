import sys

from integration_testing_environment.utils.exception.exception_tag import send_html_exception_tag
from integration_testing_environment.utils.exception.exceptions import ITESendHtmlReportException
from integration_testing_environment.utils.manager.package_manager.package_manager_class import package_manager


def send_after_test(html_report_path: str = None):
    try:
        mail_thunder = package_manager.installed_package_dict.get("je_mail_thunder", None)
        if mail_thunder is not None:
            mail_thunder_smtp = mail_thunder.SMTPWrapper()
            if html_report_path is None and mail_thunder_smtp.login_state is True:
                user = mail_thunder_smtp.user
                with open("default_name.html", "r+") as file:
                    html_string = file.read()
                message = mail_thunder_smtp.create_message_with_attach(
                    html_string,
                    {"Subject": "Test Report", "To": user, "From": user},
                    "default_name.html", use_html=True)
                mail_thunder_smtp.send_message(message)
                mail_thunder_smtp.quit()
            elif mail_thunder_smtp.login_state is True:
                user = mail_thunder_smtp.user
                with open(html_report_path, "r+") as file:
                    html_string = file.read()
                message = mail_thunder_smtp.create_message_with_attach(
                    html_string,
                    {"Subject": "Test Report", "To": user, "From": user},
                    html_report_path, use_html=True)
                mail_thunder_smtp.send_message(message)
                mail_thunder_smtp.quit()
            else:
                raise ITESendHtmlReportException
        else:
            raise ITESendHtmlReportException
    except ITESendHtmlReportException as error:
        print(repr(error), file=sys.stderr)
        print(send_html_exception_tag, file=sys.stderr)

