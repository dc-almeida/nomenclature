import logging

import pysquirrel

logger = logging.getLogger(__name__)

nuts = pysquirrel.nuts
nuts.names = [item.name for item in nuts.data]
nuts.codes = [item.code for item in nuts.data]
