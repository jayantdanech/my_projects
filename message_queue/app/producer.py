from tasks import process_data

if __name__ == "__main__":
    print("Sending task...")
    result = process_data.delay(10, 20)
    print(f"Task ID: {result.id}")
    print("Waiting for result...")
    print("Result:", result.get(timeout=10))

