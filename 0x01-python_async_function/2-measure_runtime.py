#!/usr/bin/env python3
"""
Module that provides measure_time function
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    A function with integers n and max_delay as
    arguments that measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter()

    total_time = stop - start
    return total_time/n
