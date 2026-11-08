import response
from konlpy.tag import Twitter
import numpy as np
import pickle


def load_stopwords():
    with open("./data/stopwords.pickle", "rb") as handle:
        out = pickle.load(handle)

    return out


def load_data():
    DATA_PATH = "./data/"
    FILES = ["김유정_봄봄.txt", "김유정_소낙비.txt", "채만식_소설안쓰는변명.txt"]
    novels = []

    for file_name in FILES:
        with open(DATA_PATH + file_name, "r") as f:
            novels.append((f.read()))

    return novels


# TODO: [지시사항 1번] 불용어(stopwords)를 제거한 BoW를 출력하는 함수를 만드세요.
def bag_of_words(tokenized, stopwords):
    word_dict = {}

    # TODO: word_dict에 현재 token이 있으면 1을 더해주고,
    # 없으면 키가 token이고 값이 1인 새로운 딕셔너리 항목을 만드세요.
    for token in tokenized:
        try:
            word_dict[token] += 1
        except:
            word_dict[token] = 1

    # word_dict에서 불용어를 제거하세요.
    for stop in stopwords:
        try:
            # TODO: del 키워드를 이용하여 불용어(stop)를 제거합니다.
            del word_dict[stop]
        except:
            continue

    return word_dict


# TODO: [지시사항 2번] 문서를 형태소 단위로 토큰화된 리스트로 출력하는 함수를 만드세요.
def tokenizer(document):
    # analyzer는 Twitter()를 사용합니다.
    analyzer = Twitter()

    # analyzer의 morphs 함수를 이용하여 document를 토큰화하세요.
    tokenized_documents = analyzer.morphs(document)

    return tokenized_documents


# TODO: [지시사항 3번] 빈도 상위 k개의 토큰을 가져오는 함수를 만드세요.
def top_k(dic_bow, k):

    values = list(dic_bow.values())

    # TODO: values를 역순으로 정렬하세요.
    values = sorted(values)
    values.reverse()

    # TODO: 역순으로 정렬된 values에서 상위 k개의 값을 가져오세요.
    top_k = values[:k]

    top_k_words = []
    for key in dic_bow.keys():
        if dic_bow[key] in top_k:
            top_k_words.append(key)

    return top_k_words


def tf(doc, word):
    return doc.count(word)


# TODO: [지시사항 4번] IDF 함수를 완성하세요.
def idf(docs, word):
    num = 0
    for doc in docs:
        if doc.count(word) > 0:
            num += 1
    # TODO: docs의 길이에 np.log를 적용한 값을 (num+1)로 나눕니다.
    return np.log(len(docs) / (1 + num))


# TODO: [지시사항 5번] TF-IDF 함수를 완성하세요.
def tf_idf(docs, bow):
    len_vector = len(bow)
    vectors = []

    keys = list(bow.keys())

    for doc in docs:
        vector = []
        for i, key in enumerate(keys):
            # TODO: TF와 IDF값을 곱한 결과를 변수 vector에 추가하여 줍니다.
            vector.append(tf(doc, key) * idf(docs, key))

        vectors.append(vector)

    return vectors


def main():
    stopwords = load_stopwords()
    novel1, novel2, novel3 = load_data()
    stopwords = stopwords + [
        "(",
        ")",
        ".",
        ",",
        "그것",
        "도",
        "는",
        "은",
        "다",
        "이",
        "고",
        "서",
    ]

    # 각 문서의 토큰화를 진행합니다.
    novel1_token = tokenizer(novel1)
    novel2_token = tokenizer(novel2)
    novel3_token = tokenizer(novel3)

    # 토큰화된 문서를 바탕으로 각각의 BoW를 만듭니다.
    novel1_bow = bag_of_words(novel1_token, stopwords)
    novel2_bow = bag_of_words(novel2_token, stopwords)
    novel3_bow = bag_of_words(novel3_token, stopwords)

    # 토큰화된 문서를 바탕으로 각각의 BoW를 만듭니다.
    novel1_top_k = top_k(novel1_bow, 10)
    novel2_top_k = top_k(novel2_bow, 10)
    novel3_top_k = top_k(novel3_bow, 10)

    # 토큰화된 문서를 하나의 리스트 안에 (리스트 형태로)추가하여 전체 토큰화 문서 리스트를 만들어 줍니다.
    total_tokens = [novel1_token, novel2_token, novel3_token]

    # 각 문서별 BoW를 병합하여 total_bow를 만듭니다.
    total_bow = {}
    total_bow.update(novel1_bow)
    total_bow.update(novel2_bow)
    total_bow.update(novel3_bow)

    novel1_tfidf, novel2_tfidf, novel3_tfidf = tf_idf(total_tokens, total_bow)
    print(novel1_tfidf, novel2_tfidf, novel3_tfidf)

    return novel1, novel2, novel3, stopwords, novel1_token, novel1_bow, novel1_tfidf


if __name__ == "__main__":
    response.run()
