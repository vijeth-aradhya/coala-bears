from bears.markdown.MarkdownBear import MarkdownBear
from coalib.testing.LocalBearTestHelper import verify_local_bear

test_file1 = """1. abc
1. def
"""


test_file2 = """1. abc
2. def
"""

test_file3 = """1. abcdefghijklm
2. nopqrstuvwxyz
"""

MarkdownBearTest = verify_local_bear(MarkdownBear,
                                     valid_files=(test_file2,),
                                     invalid_files=(test_file1,))

MarkdownBearConfigsTest = verify_local_bear(
    MarkdownBear,
    valid_files=(test_file1,),
    invalid_files=(test_file2,),
    settings={'list_increment': False})

MarkdownBearMaxLineLengthSettingTest = verify_local_bear(
    MarkdownBear,
    valid_files=(test_file2,),
    invalid_files=(test_file3,),
    settings={'max_line_length': 10})
