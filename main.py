


price_per_console = float(input("Введіть вартість однієї ігрової приставки: "))
quantity = int(input("Введіть кількість ігрових приставок: "))
discount_percentage = float(input("Введіть відсоток знижки: "))
choice = input("Оберіть 'загальна сума' або 'вартість однієї приставки' (введіть '1' або '2'): ")

if choice == '1':
    total_price = price_per_console * quantity * (1 - discount_percentage / 100)
    print(f"Загальна сума замовлення з урахуванням знижки: {total_price:.2f} грн.")
elif choice == '2':
    discounted_price = price_per_console * (1 - discount_percentage / 100)
    print(f"Вартість однієї приставки зі знижкою: {discounted_price:.2f} грн.")
else:
    print("Неправильний вибір. Будь ласка, введіть 'загальна сума' або 'приставка'.")