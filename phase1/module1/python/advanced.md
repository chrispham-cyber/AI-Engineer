# Avanced Python

## Exception Handling
```
try:
    risky()
except (ValueError, KeyError) as e:
    log.error(f"Failed: {e}")
    raise
```

## File I/O
### Read File
```
with open("data.txt") as f:
    content = f.read()
```

### Write File
```
with open("output.txt", "w") as f:      
    f.write("Hello\n")
```

### Modes

| Mode | Ý nghĩa |
|------|---------|
| `r` | read (default) |
| `w` | write (đè) |
| `a` | append |
| `r+` | read + write |
| `b` | binary (image, video) |
| `t` | text (default) |

## Async/Await

LLM API calls take 1–30 seconds. While waiting, you can make multiple other calls in parallel.

Async only speeds up I/O-bound tasks; it does not speed up CPU-bound tasks.

```
import asyncio

async def fetch_url(url):
    print(f"Fetching {url}")
    await asyncio.sleep(1)        
    return f"Data from {url}"

async def main():
    # Sequential
    r1 = await fetch_url("a.com")
    r2 = await fetch_url("b.com")
    # Run 2s
    
    # Parallel 
    r1, r2 = await asyncio.gather(
        fetch_url("a.com"),
        fetch_url("b.com")
    )
    # Run 1s

asyncio.run(main())
```

## Logging
```
import logging

logger.debug("Detail info for debug")
logger.info("Normal info")
logger.warning("Warning!")
logger.error("Error happened")
logger.critical("Critical!")

def process(data):
    logger.info(f"Processing {len(data)} items")
    try:
        result = do_work(data)
        logger.info("Done")
        return result
    except Exception as e:
        logger.error(f"Failed: {e}", exc_info=True)
        raise
```

## Exercises
- [URL Status Parallel Check](../exercises/urlCheck.py)