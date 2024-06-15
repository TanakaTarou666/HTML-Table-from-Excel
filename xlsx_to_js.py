import pandas as pd
import json

# ユーザー設定項目
excel_file = 'example.xlsx'  # 変換したいExcelファイルのパス
js_file = 'data.js'  # 出力したいJavaScriptファイルのパス
num_columns = 3


# 設定の確認
confirmation = input(f"""
xlsxファイル : '{excel_file}'
jsファイル   : '{js_file}'
列数         : {num_columns}

この設定でよいですか？ (y or n): """)

if confirmation.lower() != 'y':
    print("設定を変更してください。")
    exit()


# Excelファイルを読み込む
df = pd.read_excel(excel_file)

# num_columns行目までのデータを抽出する（例えば、n=3の場合は最初の3行を抽出）
df_subset = df.iloc[:, :num_columns]

# JSON形式に変換
json_str = df_subset.to_json(orient='records', lines=False, force_ascii=False)

# JSON文字列を整形
formatted_json_str = json.dumps(json.loads(json_str), indent=4, ensure_ascii=False).replace('\\\\', '/')

# JavaScriptの変数に変換
js_str = f'const data = {formatted_json_str};'

# JavaScriptファイルとして保存
with open(js_file, 'w', encoding='utf-8') as f:
    f.write(js_str)

print(f"Excelファイル '{excel_file}' がJavaScriptファイル '{js_file}' に変換されました。")