# HTML-Table-from-Excel
ExcelデータをJavaScriptファイルに変換し、HTMLで表示するスクリプト。
Excelデータ内のurlから画像を表示することができる。
以下が実行例。\n
https://tanakatarou666.github.io/HTML-Table-from-Excel/

## 特徴

- Excelファイル (.xlsx) をJavaScriptファイル (.js) に変換。
- JavaScriptデータをHTMLの表としてレンダリング。

## 必要条件

- Python 3.x
- pandas
- json

## インストール

1. リポジトリをクローンします：
    ```bash
    git clone https://github.com/TanakaTarou666/HTML-Table-from-Excel.git
    ```
2. プロジェクトディレクトリに移動します：
    ```bash
    cd HTML-Table-from-Excel
    ```
3. 必要なパッケージをインストールします：
    ```bash
    pip install pandas 
    ```

## 使い方

1. Excelファイルと画像をディレクトリに配置します。
2. `xlsx_to_js.py`のユーザー設定項目を設定します。
3. Pythonスクリプトを実行します：
    ```bash
    python trans_excel_to_js.py
    ```
4. JavaScriptファイルが同じディレクトリに生成されます。
5. `index.html`の`image_keys`で表示する画像のキーのリストを設定します。
6. 生成されたJavaScriptファイルをHTMLファイルに含めて表をレンダリングします。

## 例

`example.xlsx`というExcelファイルがある場合、スクリプトを実行すると`data.js`というJavaScriptファイルが生成され、それをHTMLファイルに含めることでデータを表としてレンダリングできます。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細については [LICENSE](LICENSE) ファイルをご覧ください。
