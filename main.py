import xml.etree.ElementTree as ET
import pandas as pd


def kml_to_csv():
    """將kml中的simpleData抓出來變成csv"""

    filename = input('輸入檔案名稱：')
    # 還沒找到自動刪掉kml的方法

    # tree = ET.parse(filename)
    # root = tree.getroot()

    # # kml = root.findall('kml')
    # # root.remove(root[0])
    # print(root[1])
    # tree.write(filename)
    # print(kml)
    # print('修改成功')

    csv_json = dict()
    tree = ET.parse(filename)
    root = tree.getroot()
    doc = root.findall('Document')
    for placemark in root.findall('Placemark'):
        name = placemark.find('name').text
        single_data = dict()
        single_data.clear()
        single_data['Name'] = name
        for data in placemark.iter('SimpleData'):
            column = data.get('name')
            data_string = data.text
            single_data[column] = data_string
        csv_json[name] = single_data

    df = pd.DataFrame()
# key = []
    for values in csv_json.values():
        df = df.append(pd.json_normalize(values), ignore_index=True)

    df.to_csv(filename[0:-4]+'.csv')
    return print('轉檔成功！')


kml_to_csv()
