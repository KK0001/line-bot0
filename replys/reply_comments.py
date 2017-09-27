# リプライ用
from random import randint

def auto_reply():
    comments = [
        "そうなんだー",
        "へえ",
        "そうなの？",
        "うんうん",
        "...",
        "んー？",
        "うん",
        "...？",
        "うんうん",
        "...！",
        "ところでアレはどうなったの？",
        "わあ",
        "？。？",
        "モ",
        "はい",
        "うむ",
        "おなかすいたなー",
        "おなかすかない？",
        "今日ってプレミアムフライデーだっけ？",
        "。",
        "3。3",
        "インド",
        "モイ！"
    ]
    idx = randint(0, len(comments)-1)
    return comments[idx]

def ohayo():
    comments = [
        "おはー",
        "おはよ",
        "おはよー",
        "よく眠れた？"
    ]
    idx = randint(0, len(comments)-1)
    return comments[idx]

def oyasu():
    comments = [
        "おやすみー",
        "おやすみ！"
    ]
    idx = randint(0, len(comments)-1)
    return comments[idx]
