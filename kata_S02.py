orders = [
    {
        'order_id': '100000',
        'create_date': '00.00.0000',
        'fullname': 'ТЕСТ ТЕСТ',
        'products': [
            {
                'product_id': '1234',
            },
            {
                'product_id': '1136'
            },
            {
                'product_id': '12345',
            },
            {
                'product_id': '123456',
            },
            {
                'product_id': '1234567'
            },
            {
                'product_id': '3258'
            },
            {
                'product_id': '12345678'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '122585'
            }
        ]
    },
    {
        'order_id': '100001',
        'create_date': '00.00.0000',
        'fullname': 'ТЕСТ ТЕСТ',
        'products': [
            {
                'product_id': '4321',
            },
            {
                'product_id': '1136'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '12345',
            },
            {
                'product_id': '123456',
            },
            {
                'product_id': '11025'
            },
            {
                'product_id': '3258'
            },
            {
                'product_id': '12345678'
            },
            {
                'product_id': '122585'
            },
            {
                'product_id': '11214'
            }
        ]
    },
    {
        'order_id': '100002',
        'create_date': '00.00.0000',
        'fullname': 'ТЕСТ ТЕСТ',
        'products': [
            {
                'product_id': '1234',
            },
            {
                'product_id': '1136'
            },
            {
                'product_id': '12345',
            },
            {
                'product_id': '123456',
            },
            {
                'product_id': '1234567'
            },
            {
                'product_id': '3258'
            },
            {
                'product_id': '12345678'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '122585'
            }
        ]
    },
    {
        'order_id': '100003',
        'create_date': '00.00.0000',
        'fullname': 'ТЕСТ ТЕСТ',
        'products': [
            {
                'product_id': '4321',
            },
            {
                'product_id': '1136'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '12345',
            },
            {
                'product_id': '897',
            },
            {
                'product_id': '11025'
            },
            {
                'product_id': '3258'
            },
            {
                'product_id': '122585'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '12345678'
            },
        ]
    },
    {
        'order_id': '100004',
        'create_date': '00.00.0000',
        'fullname': 'ТЕСТ ТЕСТ',
        'products': [
            {
                'product_id': '4321',
            },
            {
                'product_id': '4321658775'
            },
            {
                'product_id': '11214'
            },
            {
                'product_id': '43210258',
            },
            {
                'product_id': '432100000',
            },
            {
                'product_id': '432111025'
            },
            {
                'product_id': '32432158'
            },
            {
                'product_id': '1224321585'
            },
            {
                'product_id': '112143214'
            },
            {
                'product_id': '123456743218'
            },
        ]
    }
]


products_id_on_warehouse = [
    12345678,
    1234,
    123456,
    12345
]


'''
Есть заказы orders в которых есть продукты products,
нужно оставить в каждом заказе только те товары которые есть в
наличии на складе products_id_on_warehouse,
от остальных товаров в каждом заказе нужно избавиться.
В том случае если на складе нет ни одного товара
избавиться и от заказа.
'''


def clear_order(order: dict, products: list) -> dict:
    order.update(
        {
            'products': [
                {'product_id':
                     i['product_id']
                 }
                for i in order['products']
                if int(i['product_id']) in products]
        }
    )
    return order


def clear_orders(orders: list, products: list) -> list:
    new_orders = [
        x
        for x in orders
        if clear_order(x, products)['products']
    ]
    return new_orders


if __name__ == "__main__":
    print(clear_orders(orders=orders, products=products_id_on_warehouse))

