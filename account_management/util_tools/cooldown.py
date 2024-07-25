import math

def haversine(lon1, lat1, lon2, lat2):
    # 地球の半径（キロメートル）
    R = 6371.0

    # 度をラジアンに変換
    lon1_rad = math.radians(lon1)
    lat1_rad = math.radians(lat1)
    lon2_rad = math.radians(lon2)
    lat2_rad = math.radians(lat2)

    # 経度と緯度の差
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    # ハーバサインの公式
    a = math.sin(dlat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # 距離を計算
    distance = R * c

    return distance

def get_wait_time(distance):
    # 距離と待機時間の対応表
    wait_times = [
        (1, "30秒"),
        (5, "2分"),
        (10, "6分"),
        (25, "11分"),
        (35, "14分"),
        (65, "22分"),
        (81, "25分"),
        (100, "35分"),
        (250, "45分"),
        (500, "1時間"),
        (750, "1時間15分"),
        (1000, "1時間30分"),
        (1500, "2時間"),
    ]

    # 距離に応じた待機時間を取得
    for dist, wait_time in wait_times:
        if distance <= dist:
            return wait_time
    return "2時間以上"

# ユーザーからの入力
lon1 = float(input("最初の座標の経度を入力してください: "))
lat1 = float(input("最初の座標の緯度を入力してください: "))
lon2 = float(input("2番目の座標の経度を入力してください: "))
lat2 = float(input("2番目の座標の緯度を入力してください: "))

# 距離を計算
distance = haversine(lon1, lat1, lon2, lat2)
wait_time = get_wait_time(distance)

print(f"距離: {distance:.2f} km")
print(f"待機時間: {wait_time}")
