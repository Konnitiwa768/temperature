import numpy as np
import matplotlib.pyplot as plt

# 画像のサイズ
width, height = 512, 512

# 空の画像を作成
climate_map = np.zeros((height, width, 3), dtype=np.uint8)

# 気候の割り当て（仮）
for y in range(height):
    for x in range(width):
        if y < height * 0.2:
            climate_map[y, x] = [0, 0, 255]  # 寒帯 (青)
        elif y < height * 0.4:
            climate_map[y, x] = [0, 255, 0]  # 冷帯 (緑)
        elif y < height * 0.6:
            climate_map[y, x] = [255, 255, 0]  # 温帯 (黄色)
        elif y < height * 0.8:
            climate_map[y, x] = [255, 165, 0]  # 亜熱帯 (オレンジ)
        else:
            climate_map[y, x] = [255, 0, 0]  # 熱帯 (赤)

# 画像を保存
plt.imsave('climate_map.png', climate_map)
