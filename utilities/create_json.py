"""
Open multiple files in a directory:
    https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory/38992988
Appending data to a file:
    https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
"""

import json
import os

json_path = r"D:\\FashionProductImageDataSet\\fashion-dataset\\curated_json\\"


def json_data(path):
    """
    Function to extract JSON file product data from kaggle.com data set
    to fit the Sportswear Online product model and fixtures JSON file format
    """
    pk = 1
    filelist = os.listdir(path)
    # write the data to a JSON file

    for i in filelist:
        if i.endswith(".json"):
            with open(path + i, "r") as f:
                json_data = json.load(f)

                """
                Source JSON file prices are in Indian Rupees
                Convert prices to GBP for the JSON output
                """
                price = json_data['data']['price']
                price_new = float("{:.2f}".format(price * 0.0096))

                """
                Convert prices to GBP for the JSON output and add an extra
                10% discount
                """
                discount_price = json_data['data']['discountedPrice']
                discount_price_new = float("{:.2f}".format(
                    (discount_price * 0.0096) * 0.90))

                # Build the products JSON structure
                json_data = {
                    "pk": pk,
                    "model": "products.product",
                    "column_names": {
                        "price": price_new,
                        "discount_price": discount_price_new,
                        "sku": json_data['data']['articleNumber'],
                        "name": json_data['data']['variantName'],
                        "product_description": json_data['data']['productDisplayName'],
                        "gender": json_data['data']['gender'],
                        "master_category": json_data['data']['masterCategory']['typeName'],
                        "sub_category": json_data['data']['subCategory']['typeName'],
                        "article_type": json_data['data']['articleType']['typeName'],
                        "image": str(json_data['data']['id']) + ".jpg",
                    }
                }

                # write the data to a JSON file
                with open('products.json', 'a') as json_file:
                    json.dump(json_data, json_file)

                pk += 1


json_data(json_path)
