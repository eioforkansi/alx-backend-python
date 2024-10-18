#!/usr/bin/env python3

"""
Module that provide async_generator corountine.
"""

import random
import asyncio
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10.
    """
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
