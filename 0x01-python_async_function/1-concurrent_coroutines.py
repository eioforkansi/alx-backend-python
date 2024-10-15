#!/usr/bin/env python3
"""
Module that provides wait_n function
"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Takes in 2 int arguments (in this order): n and max_delay.
    It spawn wait_random n times with the specified max_delay
    and return the list of all the delays (float values).
    """
    delays = [wait_random(max_delay) for _ in range(n)]
    result = []
    for task in asyncio.as_completed(delays):
        delay = await task
        result.append(delay)
    return result
