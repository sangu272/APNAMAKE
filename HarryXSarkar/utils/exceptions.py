#
# Copyright (C) 2024 by MISH0009@Github, < https://github.com/MISH0009 >.
#
# This file is part of < https://github.com/MISH0009/DNS > project,
# and is released under the MIT License.
# Please see < https://github.com/MISH0009/DNS/blob/master/LICENSE >
#
# All rights reserved.
#


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)


class DownloadError(Exception):
    """Custom exception for download failures."""

    def __init__(self, errr: str):
        super().__init__(errr)
