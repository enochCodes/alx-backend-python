#!/usr/bin/env python3
"""create asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random delay number then return"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
