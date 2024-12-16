import os
from dotenv import load_dotenv

# Load environment variables from a `.env` file if present
load_dotenv()

class ConfigError(Exception):
    """Custom exception for configuration-related errors."""
    pass

class AppConfig:
    """Centralized environment configuration handler."""
    def __init__(self):
        # Load the required variables
        self.DATABASE_URL = self._get_env_variable("DATABASE_URL")
        self.LOG_LEVEL = self._get_env_variable("LOG_LEVEL", default="INFO")

    def _get_env_variable(self, var_name: str, default: str = None) -> str:
        """
        Retrieves environment variable value or raises exception if missing.
        
        Args:
            var_name (str): Environment variable to fetch.
            default (str, optional): Default value if not set. Defaults to None.
        
        Raises:
            ConfigError: If the environment variable is not set and no default is provided.
        
        Returns:
            str: Value of the environment variable.
        """
        value = os.getenv(var_name, default)
        # Log the environment variable loading
        print(f"Loaded {var_name}: {value}")
        if not value:
            raise ConfigError(f"Required environment variable '{var_name}' is missing.")
        return value


# Instantiate the configuration
config = AppConfig()
