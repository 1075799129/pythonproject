import xlwt
import pandas as pd
import datetime


def export_excel(export):
    # 将字符串转换为DataFrame
    pf = pd.DataFrame(list(export))
    # 指定字段顺序
    order = ["road_name", "bus_plate", "timeline", "site", "road_type"]
    pf = pf[order]
    # 替换中文名
    columns_map = {
        "road_name": "路线",
        "bus_plate": "车牌",
        "timeline": "时间",
        "road_type": "方向",
        "site": "站点"
    }
    pf.rename(columns=columns_map, inplace=True)
    # 生成表格名称
    file_path = pd.ExcelWriter("busInfo.xlsx")
    # 替换空单元格
    pf.fillna(" ", inplace=True)
    # 输出
    pf.to_excel(file_path, encoding="utf-8")
    # 保存表格
    file_path.save()


if __name__ == "__main__":
    tables = [
        {"road_name": "08路", "bus_plate": "陕A888888", "timeline": datetime.datetime(2019, 7, 5, 12, 31, 45),
         "road_type": 0.0, "site": 22.0},
        {"road_name": "09路", "bus_plate": "陕A666666", "timeline": datetime.datetime(2019, 7, 5, 12, 31, 45),
         "road_type": 1.0, "site": 33.0},
        {"road_name": "10路", "bus_plate": "陕A999999", "timeline": datetime.datetime(2019, 7, 5, 12, 31, 45),
         "road_type": 2.0, "site": 44.0}
    ]
    # 导出表格
    export_excel(tables)
