from typing import Optional, Dict


class ApiKeyStrategy:
    """
    API Key authentication strategy.
    """
    
    def __init__(self, api_key: str, header_name: str = 'X-API-Key'):
        """
        Initialize API Key strategy.
        
        Args:
            api_key: API key value
            header_name: Header name for key
        """
        self.api_key = api_key
        self.header_name = header_name
    
    def add_auth(self, headers: Optional[Dict] = None) -> Dict:
        """
        Add API key to headers.
        
        Args:
            headers: Existing headers
        
        Returns:
            Headers with API key
        """
        if headers is None:
            headers = {}
        
        headers[self.header_name] = self.api_key
        return headers