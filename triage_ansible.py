#!/usr/bin/env python
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible. If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import logging
import sys

from ansibullbot import constants
from ansibullbot.triagers.ansible import AnsibleTriage
import sentry_sdk


def handle_exception(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))


sys.excepthook = handle_exception


def main():
    sentry_sdk.init(
        dsn=constants.DEFAULT_SENTRY_DSN,
        environment=constants.DEFAULT_SENTRY_ENV,
        server_name=constants.DEFAULT_SENTRY_SERVER_NAME,
        attach_stacktrace=constants.DEFAULT_SENTRY_TRACE,
        release=constants.ANSIBULLBOT_VERSION,
    )
    # Run the triager ...
    AnsibleTriage().start()


if __name__ == "__main__":
    main()
