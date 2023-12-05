# data_handler.py

DATA_FILE_PATH = "ears_data.txt"


def retrieve_data() -> dict:
    """Retrieve data from a file."""
    try:
        with open(DATA_FILE_PATH, "r") as file:
            data = file.read()
            return {"data": data}
    except FileNotFoundError:
        return {"error": "Data file not found."}
    except Exception as e:
        return {"error": f"Error retrieving data: {str(e)}"}


def store_data(data: str) -> dict:
    """Store data to a file."""
    try:
        with open(DATA_FILE_PATH, "w") as file:
            file.write(data)
        return {"message": "Data stored successfully."}
    except Exception as e:
        return {"error": f"Error storing data: {str(e)}"}
