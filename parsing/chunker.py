import re

def simple_chunk(text: str, max_len: int = 500) -> list:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    chunk = ""
    for sentence in sentences:
        if len(chunk) + len(sentence) < max_len:
            chunk += sentence + " "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + " "
    if chunk:
        chunks.append(chunk.strip())
    return chunks

if __name__ == "__main__":
    with open("output/raw_html/bookmyshow.txt", "r", encoding="utf-8") as f:
        text = f.read()
    chunks = simple_chunk(text)
    with open("output/chunks/bookmyshow_chunks.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n---\n")
