import json
from dateutil import parser


def load_operations():
    """
    Загружает список из выполненных операций
    """
    with open('../operations.json', 'r', encoding='utf') as file:
        read_file = file.read()
        loaded_operations = json.loads(read_file)

    executed_operations = []

    for operation in loaded_operations:
        if operation:
            if operation['state'] == 'EXECUTED':
                executed_operations.append(operation)
    return executed_operations


def load_last_operations(executed_operations):
    """
    Возвращает 5 операций с измененной датой
    """
    last_5_operations = []

    executed_operations.sort(key=lambda x: str(x.get("date")), reverse=True)
    executed_operations = executed_operations[:5]
    for operation in executed_operations:
        operation["date"] = parser.parse(operation["date"]).date()
        operation["date"] = operation["date"].strftime("%d.%m.%Y")
        last_5_operations.append(operation)

    return last_5_operations


def mask_information(info_from_to):
    """
    Возвращает замаскированный номер счёта или карты
    """
    info_to_part = info_from_to.split()
    title = " ".join(info_to_part[:-1])
    part_to_mask = info_to_part[-1]
    if "Счет" in title:
        return "{} **{}".format(title, part_to_mask[-4:])
    else:
        return "{} {} {}** **** {}".format(title, part_to_mask[:4], part_to_mask[4:6], part_to_mask[12:])
