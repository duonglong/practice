from datetime import datetime
import json
OUTPUT = 'orders.json'
DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
order_num = 51
data_tmp = {
    "name": "PBR11 28035-045-0086",
    "amount_paid": 33,
    "amount_total": 8,
    "amount_tax": 0.45,
    "amount_return": 25,
    "lines": [[0, 0,{"qty": 1, "price_unit": 8, "discount": 0, "product_id": 2951, "tax_ids": [[6, False, [1]]], "id": 19, "is_flavour_item": False, "bom_line_id": False, "show_in_cart": True, "is_bundle_item": False,
                                                                                                                                    "product_master_id": False, "pricelist_id": 4, "bom_quantity": False, "product_category_id": False, "error": False, "promotion_id": False, "product_promotion_id": False, "discount_amount": False,
                                                                                                                                    "rate_promotion": False, "bill_type": False, "bill_amount": False, "min_bill_apply": False, "bill_promotion_ids": [], "price_flavor": False, "user_promotion": False, "non_sale": False,
                                                                                                                                    "voucher": []}],
              [0, 0, {"qty": 90949470.17729282, "price_unit": 0, "discount": 0, "product_id": 957, "tax_ids": [[6, False, [1]]], "id": 21, "is_flavour_item": True, "bom_line_id": 4212,
                                                                                                                                                             "show_in_cart": True, "is_bundle_item": False, "product_master_id": 2951, "pricelist_id": 4, "bom_quantity": 2.5, "product_category_id": 64, "error": False,
                                                                                                                                                             "promotion_id": False, "product_promotion_id": False, "discount_amount": False, "rate_promotion": False, "bill_type": False, "bill_amount": False, "min_bill_apply": False,
                                                                                                                                                             "bill_promotion_ids": [], "price_flavor": 3.2, "user_promotion": False, "non_sale": False, "voucher": [], "total_qty": 2.5}],
              [0, 0,{"qty": 1, "price_unit": 0, "discount": 0,
"product_id": 1231,
                                                                                                                                                                                                                                                                                             "tax_ids": [[6, False, [1]]], "id": 20,
                                                                                                                                                                                                                                                                                             "is_flavour_item": True,
                                                                                                                                                                                                                                                                                             "bom_line_id": 4211, "show_in_cart": False,
                                                                                                                                                                                                                                                                                             "is_bundle_item": False,
                                                                                                                                                                                                                                                                                             "product_master_id": 2951,
                                                                                                                                                                                                                                                                                             "pricelist_id": 4, "bom_quantity": 1,
                                                                                                                                                                                                                                                                                             "product_category_id": False,
                                                                                                                                                                                                                                                                                             "error": False, "promotion_id": False,
                                                                                                                                                                                                                                                                                             "product_promotion_id": False,
                                                                                                                                                                                                                                                                                             "discount_amount": False,
                                                                                                                                                                                                                                                                                             "rate_promotion": False, "bill_type": False,
                                                                                                                                                                                                                                                                                             "bill_amount": False,
                                                                                                                                                                                                                                                                                             "min_bill_apply": False,
                                                                                                                                                                                                                                                                                             "bill_promotion_ids": [],
                                                                                                                                                                                                                                                                                             "price_flavor": False,
                                                                                                                                                                                                                                                                                             "user_promotion": False, "non_sale": False,
                                                                                                                                                                                                                                                                                             "voucher": [], "total_qty": 1}]],
    "statement_ids":
        [[0, 0, {"name": "2017-12-25 07:26:56", "statement_id": 170735, "account_id": 1427, "journal_id": 8, "amount": 33}]],
    "pos_session_id": 37446,
    "partner_id": False,
    "user_id": 5,
    "uid": "28035-045-0033",
    "sequence_number": 33,
    "creation_date": "2017-12-25T07:26:56.876Z",
    "fiscal_position_id": False,
    "outlet_id": 11,
    "invoice_no": "PBR11 28035-045-0033",
    "cfg_sequence_number": 5344,
    "use_voucher": [], "discount_payment": {}, "note": ""
}
order_temp = {
    "id": "28035-045-0074",
    # "data": data,
    "to_invoice": False
}

orders = []
for i in range(order_num):
    order = dict(order_temp)
    data = dict(data_tmp)
    data['name'] = '%s-%s' % (datetime.now().strftime(DATETIME_FORMAT), i)
    order['id'] = '%s-%s' % (datetime.now().strftime(DATETIME_FORMAT), i)
    order['data'] = data
    orders.append(order)

print [x['id'] for x in orders]

with open(OUTPUT, 'wb') as outfile:
    json.dump(orders, outfile)


