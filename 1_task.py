PRODUCTS = [
    # название, цена
    ['яблоки', 100],
    ['швейцарский сыр', 1500],
    ['красная рыба', 450],
]
MAX_PRODUCT_NAME = 17
MAX_LENGTH_COST = 5
BORDER_SYMBOLS = 28


def create_formatted_receipt(border_symbols, products, max_product_name, max_length_cost):
    """Функция создает новый чек, принимает на вход любой список покупок - `products`.
    Функция сама не вызывает `print`, только готовит строки к последующему
    выводу на экран или печати."""
    receipt_lines = []
    line = '_' * border_symbols
    empty_line = " " * border_symbols
    receipt_lines.append(' ' + line + ' \r')
    receipt_lines.append("|" + empty_line + "|\r")
    for product, cost in products:
        receipt_lines.append("|{0:18}{1:>10}|\r".format(product[0:max_product_name],
                                                        str(cost)[0:max_length_cost] + " руб."))
    receipt_lines.append('|' + line + '|\r')
    return receipt_lines


def print_all_lines(lines):
    """Функция печатает чек, предварительно созданный функцией create_formatted_receipt."""
    for line in lines:
        print(line)


def main():
    receipt = create_formatted_receipt(BORDER_SYMBOLS, PRODUCTS, MAX_PRODUCT_NAME, MAX_LENGTH_COST)
    print_all_lines(receipt)


if __name__ == '__main__':
    main()
