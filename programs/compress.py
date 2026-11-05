import gzip

with open("sample.txt", "rb", buffering=0) as f:
    with gzip.open("sample.txt.gz", "wb") as out:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            out.write(chunk)
