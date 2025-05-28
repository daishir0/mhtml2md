# mhtml2md

## Overview
mhtml2md is a Python utility that converts MHTML (MIME HTML) files to clean Markdown format. It extracts HTML content from MHTML files, removes unnecessary elements like scripts and styles, and converts the visible content to Markdown while cleaning up image references and formatting.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/daishir0/mhtml2md
   ```

2. Navigate to the project directory:
   ```bash
   cd mhtml2md
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the script from the command line with an MHTML file as input:

```bash
python html2md.py <input.mhtml>
```

**Example:**
```bash
python html2md.py webpage.mhtml
```

This will create a Markdown file with the same name as the input file but with a `.md` extension (e.g., `webpage.md`).

## Notes
- The script automatically removes script tags, style tags, meta tags, and other non-visible HTML elements
- Image markdown syntax `![alt](url)` is converted to simple `[alt]` format
- Backslashes are automatically removed from the output
- The output file is saved in the same directory as the input file
- Ensure the input file is a valid MHTML format

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

# mhtml2md

## 概要
mhtml2mdは、MHTML（MIME HTML）ファイルをクリーンなMarkdown形式に変換するPythonユーティリティです。MHTMLファイルからHTMLコンテンツを抽出し、スクリプトやスタイルなどの不要な要素を削除して、表示可能なコンテンツを画像参照や書式をクリーンアップしながらMarkdownに変換します。

## インストール方法
1. リポジトリをクローンします：
   ```bash
   git clone https://github.com/daishir0/mhtml2md
   ```

2. プロジェクトディレクトリに移動します：
   ```bash
   cd mhtml2md
   ```

3. 必要な依存関係をインストールします：
   ```bash
   pip install -r requirements.txt
   ```

## 使い方
コマンドラインからMHTMLファイルを入力としてスクリプトを実行します：

```bash
python html2md.py <input.mhtml>
```

**例：**
```bash
python html2md.py webpage.mhtml
```

これにより、入力ファイルと同じ名前で拡張子が`.md`のMarkdownファイルが作成されます（例：`webpage.md`）。

## 注意点
- スクリプトは自動的にscriptタグ、styleタグ、metaタグ、その他の非表示HTML要素を削除します
- 画像のマークダウン記法 `![alt](url)` はシンプルな `[alt]` 形式に変換されます
- 出力からバックスラッシュは自動的に削除されます
- 出力ファイルは入力ファイルと同じディレクトリに保存されます
- 入力ファイルが有効なMHTML形式であることを確認してください

## ライセンス
このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。
