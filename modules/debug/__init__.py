#!/usr/bin/env python
#############################################################
# ubi_reader/ubifs
# (c) 2013 Jason Pruitt (jrspruitt@gmail.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#############################################################

import sys
import traceback

error_action = True             # if 'exit' on any error exit program.
fatal_traceback = True          # Print traceback on fatal errors.

ignore_block_errors = True      # Ignore block errors.
logging_on = True               # Print debug info on.
logging_on_verbose = False       # Print verbose debug info on.

use_dummy_socket_file = False   # Create regular file place holder.

def log(obj, message):
    if logging_on or logging_on_verbose:
    # will out to file or console.
        print obj.__name__, message

def verbose_log(obj, message):
    if logging_on_verbose:
        log(obj, message)

def verbose_display(displayable_obj):
    if logging_on_verbose:
        print displayable_obj.display('\t')

def error(obj, level, message):
    if error_action is 'exit':
        print obj.__name__, '%s: %s' % (level, message)
        if fatal_traceback:
            traceback.print_exc()
        sys.exit(1)

    else:
        if level.lower() == 'warn':
            print obj.__name__, '%s: %s' % (level, message)
        elif level.lower() == 'fatal':
            print obj.__name__, '%s: %s' % (level, message)
            if fatal_traceback:
                traceback.print_exc()
            sys.exit(1)
        else:
            print obj.__name__, '%s: %s' % (level, message)
