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
    counter = 0
    line = '_' * 30
    receipt_lines.append(' ' + line + ' \r')
    receipt_lines.append("|" + " " * 30 + "|\r")
    for product in PRODUCTS:
        receipt_lines.append("|{0:20}{1:>10}|\r".format(PRODUCTS[counter][0], str(PRODUCTS[counter][1]) + " руб."))
        counter += 1
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
