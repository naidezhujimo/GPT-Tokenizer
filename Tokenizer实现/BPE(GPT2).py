# 读取文本文件
with open('the_verdict.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# 将文本编码为UTF-8格式的字节序列，并将其转换为整数列表
tokens = text.encode('utf-8')
tokens = list(map(int, tokens))
print(tokens)

# 计算字节对的出现频率
def get_stats(ids):
    counts = {}
    for pair in zip(ids, ids[1:]):
        counts[pair] = counts.get(pair, 0) + 1
    return counts

# 将频繁出现的字节对合并为一个新的字节
def merge(ids, pair, idx):
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i+1] == pair[1]:
            newids.append(idx)
            i += 2
        else:
            newids.append(ids[i])
            i += 1
    return newids

vocab_size = 276
num_merges = vocab_size - 256  # 假设vocab_size是最终词汇表的大小，256是ASCII字符集的大小
ids = list(tokens)

# 初始化合并字典
merges = {}
for i in range(num_merges):
    stats = get_stats(ids)
    # 找到出现频率最高的字节对
    pair = max(stats, key=stats.get)
    idx = 256 + i
    print(f"merging {pair} into a new token {idx}")
    ids = merge(ids, pair, idx)
    merges[pair] = idx

# 创建词汇表
vocab = {idx: bytes([idx]) for idx in range(256)}
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]

# 解码函数，将整数列表转换回文本
def decode(ids):
    tokens = b"".join(vocab[idx] for idx in ids)
    text = tokens.decode('utf-8', errors="replace")
    return text

# 编码函数，将文本转换为整数列表
def encode(text):
    tokens = list(text.encode('utf-8'))
    while len(tokens) >= 2:
        stats = get_stats(tokens)
        # 找到在合并字典中的最小频率字节对
        pair = min(stats, key=lambda p: merges.get(p, float('inf')))
        if pair not in merges:
            break
        idx = merges[pair]
        tokens = merge(tokens, pair, idx)
    return tokens

# 测试编码函数
print(encode("hello world!"))