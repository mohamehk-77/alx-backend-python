#!/usr/bin/env python3
"""
measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""
import asyncio
import time


wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure_time
    @n: times to call wait_random
    @max_delay: max delay of wait_random
    Return: total_time / n
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    return (end - start) / n
