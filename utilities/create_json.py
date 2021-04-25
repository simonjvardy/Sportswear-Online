"""
Open multiple files in a directory: 
    https://stackoverflow.com/questions/38991923/how-to-open-multiple-files-in-a-directory/38992988
Appending data to a file:
    https://thispointer.com/how-to-append-text-or-lines-to-a-file-in-python/
""" 

import json, os

json_path = r"D:\\FashionProductImageDataSet\\fashion-dataset\\curated_json\\"


def json_data(path):
    """
    Function to extract JSON file product data from kaggle.com data set saved locally
    on a separate drive to fit the Sportswear Online product model and fixtures JSON file format
    """
    pk = 1
    filelist = os.listdir(path)
    # write the data to a JSON file

    for i in filelist:
        if i.endswith(".json"):
            with open(path + i,"r") as f:
                json_data = json.load(f)

                json_data = {
                    "pk": pk,
                    "model": "products.product",
                    "column_names": {
                        "price": json_data['data']['price'],
                        "discount_price": json_data['data']['discountedPrice'],
                        "sku": json_data['data']['articleNumber'],
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
                # print(json_data)



json_data(json_path)