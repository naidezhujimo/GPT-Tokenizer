# 输入文本
text = """
All Posts
Reading Veach’s Thesis, Part 2
February 25, 2023 · Graphics, Math · 0 Comments

... (省略部分文本)
"""

# 将文本编码为 UTF-8 字节序列，并将其转换为整数列表
tokens = text.encode('utf-8')
tokens = list(map(int, tokens))
print(tokens)  # 打印原始字节序列

# 获取字节对的统计信息
def get_stats(ids):
    """
    统计字节序列中所有相邻字节对的出现次数。
    :param ids: 字节序列（整数列表）
    :return: 一个字典，键为字节对，值为出现次数
    """
    counts = {}
    for pair in zip(ids, ids[1:]):  # 遍历相邻字节对
        counts[pair] = counts.get(pair, 0) + 1  # 统计出现次数
    return counts

# 合并字节对
def merge(ids, pair, idx):
    """
    将字节序列中的指定字节对替换为一个新的字节。
    :param ids: 字节序列（整数列表）
    :param pair: 要合并的字节对
    :param idx: 新字节的索引
    :return: 替换后的字节序列
    """
    newids = []
    i = 0
    while i < len(ids):
        if i < len(ids) - 1 and ids[i] == pair[0] and ids[i + 1] == pair[1]:
            newids.append(idx)  # 替换为新字节
            i += 2
        else:
            newids.append(ids[i])  # 保留原字节
            i += 1
    return newids

# 设置词汇表大小和合并次数
vocab_size = 276
num_merges = vocab_size - 256  # 从 256 开始扩展词汇表
ids = list(tokens)  # 初始化字节序列

# 存储合并操作
merges = {}
for i in range(num_merges):
    stats = get_stats(ids)  # 获取当前字节对的统计信息
    pair = max(stats, key=stats.get)  # 选择出现次数最多的字节对
    idx = 256 + i  # 新字节的索引
    print(f"merging {pair} into a new token {idx}")
    ids = merge(ids, pair, idx)  # 替换字节对
    merges[pair] = idx  # 记录合并操作

# 创建词汇表
vocab = {idx: bytes([idx]) for idx in range(256)}  # 初始化词汇表（单字节）
for (p0, p1), idx in merges.items():
    vocab[idx] = vocab[p0] + vocab[p1]  # 合并字节对生成新字节

# 解码函数
def decode(ids):
    """
    将合并后的字节序列解码为原始文本。
    :param ids: 合并后的字节序列
    :return: 解码后的文本
    """
    tokens = b"".join(vocab[idx] for idx in ids)  # 将字节索引转换为原始字节
    text = tokens.decode('utf-8', errors="replace")  # 解码为 UTF-8 文本
    return text

# 编码函数
def encode(text):
    """
    将文本编码为合并后的字节序列。
    :param text: 输入文本
    :return: 编码后的字节序列
    """
    tokens = list(text.encode('utf-8'))  # 将文本编码为 UTF-8 字节序列
    while len(tokens) >= 2:
        stats = get_stats(tokens)  # 获取字节对统计信息
        pair = min(stats, key=lambda p: merges.get(p, float('inf')))  # 选择可合并的字节对
        if pair not in merges:
            break
        idx = merges[pair]  # 获取新字节索引
        tokens = merge(tokens, pair, idx)  # 替换字节对
    return tokens

# 测试编码和解码
encoded_text = encode("hello world!")
print(f"Encoded: {encoded_text}")
decoded_text = decode(encoded_text)
print(f"Decoded: {decoded_text}")