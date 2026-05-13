"""测试脚本：验证 Python 3.12 conda 环境"""
import sys
import numpy as np
import pandas as pd
import matplotlib

print(f"Python 版本: {sys.version}")
print(f"numpy 版本: {np.__version__}")
print(f"pandas 版本: {pd.__version__}")
print(f"matplotlib 版本: {matplotlib.__version__}")

# 简单的 numpy 运算
arr = np.array([1, 2, 3, 4, 5])
print(f"
numpy 数组: {arr}")
print(f"数组均值: {arr.mean()}")

# 简单的 pandas 操作
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(f"
pandas DataFrame:
{df}")

print("
✅ 环境验证通过！")
