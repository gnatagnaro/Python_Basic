import json


if __name__ == '__main__':

    diff_list = ["services", "staff", "datetime"]
    with open('json_old.json', 'r') as f_old, open('json_new.json', 'r') as f_new:
        data_old = json.load(f_old)
        data_new = json.load(f_new)

    result = {}
    for key in diff_list:
        if data_old['data'][key] != data_new['data'][key]:
            result[key] = data_new['data'][key]

    with open('result.json', 'w') as f_res:
        json.dump(result, f_res, indent=4)

    print(result)
