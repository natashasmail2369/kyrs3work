from src.functions import load_operations, load_last_operations, mask_information


def main():
    # загружаем список операций
    operations = load_operations()
    # получаем 5 последний выполненных операций при помощи функции
    last_operations = load_last_operations(operations)
    for operation in last_operations:
        if "from" in operation:
            print(f"{operation["date"]} {operation["description"]}\n"
                  f"{mask_information(operation["from"])} -> {mask_information(operation["to"])}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")
        else:
            print(f"{operation["date"]} {operation["description"]}\n"
                  f"{mask_information(operation["to"])}\n"
                  f"{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n")


if __name__ == "__main__":
    main()