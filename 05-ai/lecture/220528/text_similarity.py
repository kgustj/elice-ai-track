import numpy as np
from konlpy.tag import Twitter

# 원-핫 인코딩을 구현하는 함수입니다.
def one_hot(x, depth):
    output = []
    for i in range(depth):
        if i == x:
            output.append(1)
        else:
            output.append(0)

    return output


def sum_list(X, depth):
    output = np.zeros(depth)
    for _list in X:
        output = np.add(output, _list)

    return output


# TODO: [지시사항 1번] BoW를 딕셔너리 형태로 출력하는 함수를 만드세요.
def bag_of_words(tokenized_sentences):
    word_dict = {}
    for tokenized_sentence in tokenized_sentences:
        for token in tokenized_sentence:
            try:
                # word_dict에 token이 있으면 1을 더해주고,
                word_dict[token] += 1
            except:
                # 없으면 키가 token이고 값이 1인 새로운 딕셔너리 항목을 만드세요.
                word_dict[token] = 1

    return word_dict


# TODO: [지시사항 2번] 자카드 유사도를 구하는 함수를 만드세요.
def jaccard(X, Y):
    # TODO: 요소의 중복을 허용하는 리스트의 길이를 len_total에 저장합니다.
    len_total = len(X + Y)

    # TODO: 요소의 중복을 허용하지 않는 리스트(두 리스트의 합집합)의 길이를 len_union에 저장합니다.
    len_union = len(set(X + Y))

    # TODO: len_total과 len_union을 이용하여 중복된 리스트(두 리스트의 교집합)의 길이를 len_inter 에 저장합니다.
    len_inter = len_total - len_union

    # TODO: 자카드 유사도를 구하세요.
    jaccard_similarity = len_inter / len_union

    return jaccard_similarity


# TODO: [지시사항 3번] numpy를 이용하여 코사인 유사도를 계산하는 함수를 만드세요.
def cosine(x, y):
    cosine_similarity = np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))
    return cosine_similarity


def TextSimilarity():
    sentences = ["나는 어제 잠을 못 잤습니다", "나는 어제 밥을 굶었습니다", "오늘 밥은 맛이 없습니다.", "오늘 밥은 별로입니다."]
    analyzer = Twitter()
    tokenized = [analyzer.morphs(sen) for sen in sentences]

    ## 토큰화된 문장을 바탕으로 자카드 유사도를 출력해 봅니다.
    print("첫 번째 문장과 두 번째 문장의 자카트 유사도는 %f 입니다." % (jaccard(tokenized[0], tokenized[1])))
    print("첫 번째 문장과 세 번째 문장의 자카트 유사도는 %f 입니다." % (jaccard(tokenized[0], tokenized[2])))
    print("두 번째 문장과 세 번째 문장의 자카트 유사도는 %f 입니다." % (jaccard(tokenized[1], tokenized[2])))
    ## 토큰화된 문장을 바탕으로 BoW를 만듭니다.

    BoW = bag_of_words(tokenized)
    print("<전체 문장에 대한 BoW>\n", BoW)

    ## {'word':index} 딕셔너리를 만듭니다.
    word_index = {k: v for v, k in enumerate(BoW.keys())}

    ## word_index_dict의 길이를 구하고 이를 바탕으로 원-핫 인코딩을 진행합니다.
    len_wordIndex = len(word_index)

    sen1 = [one_hot(word_index[token], len_wordIndex) for token in tokenized[0]]
    sen2 = [one_hot(word_index[token], len_wordIndex) for token in tokenized[1]]
    sen3 = [one_hot(word_index[token], len_wordIndex) for token in tokenized[2]]

    ## 각각의 단어별 임베딩된 것을 더하여 문장의 임베딩 값으로 나타냅니다.
    sen1_onehot = sum_list(sen1, len_wordIndex)
    sen2_onehot = sum_list(sen2, len_wordIndex)
    sen3_onehot = sum_list(sen3, len_wordIndex)

    print("첫 번째 문장의 벡터:", sen1_onehot)
    print("두 번째 문장의 벡터:", sen2_onehot)
    print("세 번째 문장의 벡터:", sen3_onehot)

    ## 이를 바탕으로 코사인 유사도를 출력합니다.
    sm_12 = cosine(sen1_onehot, sen2_onehot)
    sm_13 = cosine(sen1_onehot, sen3_onehot)

    print("첫 번째 문장과 두 번째 문장의 코사인 유사도는 %f 입니다." % sm_12)
    print("첫 번째 문장과 두 번째 문장의 코사인 유사도는 %f 입니다." % sm_13)
    print(tokenized)
    print(str(sen1_onehot))
    print(f"{sen1_onehot}, {sen2_onehot}, {sen3_onehot}")

    print(sm_12, sm_13)

    return tokenized, sen1_onehot, sen2_onehot, sen3_onehot, sm_12, sm_13


if __name__ == "__main__":
    TextSimilarity()
