from loguru import logger
from src.main.server.server import app

if __name__ == "__main__":
    logger.info("Starting server...")
    app.run(host="0.0.0.0", port=5005, debug=True)
