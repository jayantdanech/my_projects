from tasks import process_data

if __name__ == "__main__":
    result = process_data.delay(10, 20)
    print(f"Task sent! ID: {result.id}")

