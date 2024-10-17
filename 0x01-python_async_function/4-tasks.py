#!/usr/bin/env python3
"""Task-based wait_n function."""
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn task_wait_random n times and return the list of delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
