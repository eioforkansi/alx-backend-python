#!/usr/bin/env python3

"""
Module that provide measure_runtime corountine.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that will execute async_comprehension four times
    in parallel using asyncio.gather and
    measure the total runtime and return it.
    """
    tasks = [async_comprehension() for _ in range(4)]
    start = time.perf_counter()
    await asyncio.gather(*tasks)
    stop = time.perf_counter()
    total = stop - start
    return total
