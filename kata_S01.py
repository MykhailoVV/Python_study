order = [
    {'order_id': '100000',
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
     }
]
products_id_on_warehouse = [
    12345678,
    701258,
    1234,
    123456,
    12345,
    2589354,
    3658998,
    148858,
    25897,
    25885
]

'''
Есть заказ order в котором есть продукты products, 
нужно оставить в заказе все товары которые есть в 
наличие на складе products_id_on_warehouse, 
от остальных товаров в заказе нужно избавиться.
'''


def clear_order(order: list, products: list):
    order[0].update(
        {
            'products': [
                {'product_id':
                     i['product_id']
                 }
                for i in order[0]['products']
                if int(i['product_id']) in products]
        }
    )
    return order


if __name__ == "__main__":
    print(clear_order(order=order, products=products_id_on_warehouse))
