## Description: This file is the entry point of the application. It is responsible for running the FastAPI application.

import uvicorn
from src.settings import Settings

if __name__ == "__main__":
    settings = Settings()

    uvicorn.run(
      app="src.app:app", 
		host=settings.application.app_host, 
		port=settings.application.app_port, 
		reload=settings.application.app_debug
	)
