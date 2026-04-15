import asyncio
from typing import AsyncIterator, Callable


class AsyncFileIterator:
    """
    Async iterator for reading large files in chunks.
    
    Args:
        filepath: Path to file
        chunk_size: Size of each chunk in bytes
    """
    
    def __init__(self, filepath: str, chunk_size: int = 1024):
        self.filepath = filepath
        self.chunk_size = chunk_size
        self.file = None
    
    def __aiter__(self):
        """Return async iterator."""
        self.file = open(self.filepath, 'r', encoding='utf-8')
        return self
    
    async def __anext__(self):
        """Read next chunk."""
        if self.file is None:
            raise StopAsyncIteration
        
        chunk = self.file.read(self.chunk_size)
        
        if not chunk:
            self.file.close()
            raise StopAsyncIteration
        
        await asyncio.sleep(0)
        return chunk


async def process_stream(iterator: AsyncIterator, processor: Callable):
    """
    Process data from async iterator.
    
    Args:
        iterator: Async iterator
        processor: Function to process each chunk
    """
    async for chunk in iterator:
        processor(chunk)