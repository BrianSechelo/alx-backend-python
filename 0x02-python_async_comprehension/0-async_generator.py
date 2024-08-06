#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import random


async def async_generator():
    """Func documentation"""
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.uniform(0, 10) 
        i += 1
