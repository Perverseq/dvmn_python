PRODUCTS = [
    # название, цена
    ['яблоки', 100],
    ['швейцарский сыр', 1500],
    ['красная рыба', 450],
]


def create_formatted_receipt(products):
    """Функция создает новый чек, принимает на вход любой список покупок - `products`.
    Функция сама не вызывает `print`, только готовит строки к последующему
    выводу на экран или печати."""
    receipt_lines = []
    line = '_' * 28
    empty_line = " " * 28
    receipt_lines.append(' ' + line + ' \r')
    receipt_lines.append("|" + empty_line + "|\r")
    for product, cost in products:
        receipt_lines.append("|{0:18}{1:>10}|\r".format(product, str(cost) + " руб."))
    receipt_lines.append('|' + line + '|\r')
    return receipt_lines


def print_all_lines(lines):
    """Функция печатает чек, предварительно созданный функцией create_formatted_receipt."""
    for line in lines:
        print(line)


def main():
    receipt = create_formatted_receipt(PRODUCTS)
    print_all_lines(receipt)


if __name__ == '__main__':
    main()
