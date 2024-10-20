#!/usr/bin/env python3

"""
Module that provide async_comprehension corountine.
"""

import random
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine will collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers.
    """
    numbers = [data async for data in async_generator()]
    return numbers
