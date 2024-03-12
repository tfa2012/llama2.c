import sentencepiece as spm

model_name = 'meng.model'
orig_txt = "满纸荒唐言，一把辛酸泪！都云作者痴，谁解其中味？"
orig_ids = [368, 711, 2140, 2215, 244, 3, 1725, 3315, 1797, 477]

# 实例化一个分词实例，然后加载训练好的meng.model
sp = spm.SentencePieceProcessor()
print(f"model_name={model_name}")
sp.load(model_name)

# encode: text => id
print(f"orig_txt={orig_txt}")
print("encode_as_pieces = ", sp.encode_as_pieces(orig_txt))
print("   encode_as_ids = ", sp.encode_as_ids(orig_txt))

# decode: id => text
print(sp.decode_ids(orig_ids))