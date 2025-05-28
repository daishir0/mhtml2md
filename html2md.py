import sys
import os
import email
from bs4 import BeautifulSoup
import html2text
import re

def extract_html_from_mhtml(mhtml_path):
    with open(mhtml_path, 'rb') as f:
        msg = email.message_from_binary_file(f)
    
    for part in msg.walk():
        content_type = part.get_content_type()
        if content_type == 'text/html':
            html_bytes = part.get_payload(decode=True)
            return html_bytes.decode(part.get_content_charset('utf-8'))
    return None

def clean_markdown(markdown):
    # 画像マークダウン ![alt](url) → [alt] に変換
    markdown = re.sub(r'!\[([^\]]*)\]\([^\)]*\)', r'[\1]', markdown)
    
    # 不要なバックスラッシュを削除
    markdown = markdown.replace('\\', '')
    
    return markdown

def html_to_markdown(html, output_path):
    soup = BeautifulSoup(html, 'html.parser')
    
    # 実際に表示されるテキストだけを抽出
    for script in soup(["script", "style", "meta", "head", "link"]):
        script.decompose()
    
    visible_html = str(soup.body or soup)
    markdown = html2text.html2text(visible_html)
    cleaned_markdown = clean_markdown(markdown)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_markdown)

    print(f"✅ Markdownに変換完了: {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python html2md.py <input.mhtml>")
        sys.exit(1)

    input_path = sys.argv[1]
    if not os.path.exists(input_path):
        print("❌ ファイルが見つかりません:", input_path)
        sys.exit(1)

    html = extract_html_from_mhtml(input_path)
    if not html:
        print("❌ HTML部分が見つかりませんでした")
        sys.exit(1)

    output_path = os.path.splitext(input_path)[0] + ".md"
    html_to_markdown(html, output_path)
