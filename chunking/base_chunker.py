# chunking/base_chunker.py

from abc import ABC, abstractmethod
from typing import List, Dict


class BaseChunker(ABC):
    """Abstract base class for chunking strategies."""

    @abstractmethod
    def chunk(self, documents: List[Dict]) -> List[Dict]:
        pass
