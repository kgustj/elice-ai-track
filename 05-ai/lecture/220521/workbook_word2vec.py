from gensim.models import word2vec
import list_file


# 1. CBOW 방식의 Word2Vec 모델을
#    반환하는 CBOW 함수를 완성하세요.
def CBOW(sentences):
    return word2vec.Word2Vec(sentences, size=300, min_count=1, window=10, sg=0)


# 2. Skip-Gram 방식의 Word2Vec 모델을
#    반환하는 Skip_Gram 함수를 완성하세요.
def Skip_Gram(sentences):
    return word2vec.Word2Vec(sentences, size=300, min_count=1, window=10, sg=1)


# 3. 각 모델의 결괏값을 정의하세요.
def main():
    sen1, sen2 = list_file.sen1(), list_file.sen2()

    sentences = [sen1, sen2]

    cbow = CBOW(sentences)
    skipgram = Skip_Gram(sentences)

    idx2word_set_cbow = cbow.wv.index2word
    idx2word_set_skipgram = skipgram.wv.index2word

    print("CBOW: ", idx2word_set_cbow)
    print("\nSkip-Gram: ", idx2word_set_skipgram)

    return idx2word_set_cbow, idx2word_set_skipgram


if __name__ == "__main__":
    main()
