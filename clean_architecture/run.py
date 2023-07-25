from src.main.server.server import app
poetry add loguru

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
