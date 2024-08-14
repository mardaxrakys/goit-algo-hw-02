import queue
import random
import time

# Створюємо чергу заявок
request_queue = queue.Queue()

# Генерація унікального ідентифікатора заявки
request_id = 1

def generate_request():
    global request_id
    # Створюємо нову заявку з унікальним ідентифікатором
    request = f"Заявка №{request_id}"
    # Додаємо заявку до черги
    request_queue.put(request)
    print(f"Згенеровано: {request}")
    request_id += 1

def process_request():
    if not request_queue.empty():
        # Видаляємо заявку з черги
        request = request_queue.get()
        # Імітуємо обробку заявки
        print(f"Обробляється: {request}")
        # Імітуємо затримку для обробки
        time.sleep(random.uniform(0.5, 1.5))
        print(f"Оброблено: {request}")
    else:
        print("Черга пуста, немає заявок для обробки.")

def main():
    try:
        while True:
            # Імітуємо створення нових заявок
            generate_request()
            # Імітуємо обробку заявок
            process_request()
            # Імітуємо затримку перед наступною ітерацією
            time.sleep(random.uniform(1, 3))
    except KeyboardInterrupt:
        print("Програма завершена.")

if __name__ == "__main__":
    main()
