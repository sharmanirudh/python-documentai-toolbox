# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from .services.document_wrapper_service import ( 
    _read_output
)

from .services.page_wrapper_service import ( 
    _get_lines,
    _get_paragraphs,
    _get_tokens,
    _text_from_layout,
)

from .types.document_wrappers import (
    DocumentWrapper,
    PageWrapper,
)

__all__ = (
    "_get_lines",
    "_get_paragraphs",
    "_get_tokens",
    "_text_from_layout",
    "_read_output",
    "DocumentWrapper",
    "PageWrapper"
)