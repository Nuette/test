import fasttext

path = "/home/nuette/PycharmProjects/Pre/data/Monolingual_corp/LID/"
print("training model")

model = fasttext.train_supervised(path + 'train.txt', dim=16, minn=2, maxn=4, loss='hs')
print("saving model")
print("testing model")
print(model.test(path + 'valid.txt'))
print("quantize model")
model.quantize(path + 'train.txt', cutoff=50000, retrain=True, qnorm=True)
print("saving model")
model.save_model('sa_lid')
