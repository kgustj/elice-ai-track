from PIL import Image
from PIL import ImageFilter


def sharpening(img):
    # TODO: [지시사항 1번] 이미지에 샤프닝 필터를 적용시키는 코드를 완성하세요.
    return img.filter(ImageFilter.SHARPEN)


def blur(img):
    # TODO: [지시사항 2번] 이미지에 블러 필터를 적용시키는 코드를 완성하세요.
    return img.filter(ImageFilter.BLUR)


def detect_edge(img):
    # TODO: [지시사항 3번] 이미지의 경계선을 탐지하는 코드를 완성하세요.
    return img.filter(ImageFilter.FIND_EDGES)


def show_image(img, name):
    img.save(name)


def main():
    # TODO: [지시사항 4번] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    img = Image.open("/Users/root-_-/Documents/GitLab/lecture-ai/220518/img/Lenna.png")

    # 이미지 샤프닝 한번 적용하기
    img_sharpen_1 = sharpening(img)

    # 이미지 샤프닝 5번 적용하기
    img_sharpen_5 = sharpening(img)
    img_sharpen_5 = sharpening(img_sharpen_5)
    img_sharpen_5 = sharpening(img_sharpen_5)
    img_sharpen_5 = sharpening(img_sharpen_5)
    img_sharpen_5 = sharpening(img_sharpen_5)

    # 이미지 블러 한번 적용하기
    img_blur_1 = blur(img)

    # 이미지 블러 5번 적용하기
    img_blur_5 = blur(img)
    img_blur_5 = blur(img_blur_5)
    img_blur_5 = blur(img_blur_5)
    img_blur_5 = blur(img_blur_5)
    img_blur_5 = blur(img_blur_5)

    # 이미지 경계선 찾기
    img_edge = detect_edge(img)

    print("=" * 42, "샤프닝 한번 적용한 이미지", "=" * 42)
    # show_image(img_sharpen_1, "sharpen_1.png")

    print("=" * 41, "샤프닝 다섯번 적용한 이미지", "=" * 41)
    # show_image(img_sharpen_5, "sharpen_5.png")

    print("=" * 43, "블러 한번 적용한 이미지", "=" * 43)
    # show_image(img_blur_1, "blur_1.png")

    print("=" * 42, "블러 다섯번 적용한 이미지", "=" * 42)
    # show_image(img_blur_5, "blur_5.png")

    print("=" * 48, "경계선 이미지", "=" * 48)
    # show_image(img_edge, "edge.png")

    return img_sharpen_1, img_sharpen_5, img_blur_1, img_blur_5, img_edge


if __name__ == "__main__":
    main()
