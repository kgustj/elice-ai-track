from PIL import Image
from PIL import ImageEnhance


def change_brightness(img, factor):
    # TODO: [지시사항 1번] 이미지의 밝기를 변화시키는 코드를 완성하세요.
    bright_enhancer = ImageEnhance.Brightness(img)
    return bright_enhancer.enhance(factor)


def change_contrast(img, factor):
    # TODO: [지시사항 2번] 이미지의 대조를 변화시키는 코드를 완성하세요.
    contrast_enhancer = ImageEnhance.Contrast(img)
    return contrast_enhancer.enhance(factor)


def change_grayscale(img):
    # TODO: [지시사항 3번] 이미지를 흑백 이미지로 변경하는 코드를 완성하세요.
    return img.convert("L")


def show_image(img, name):
    img.save(name)


def main():
    # TODO: [지시사항 4번] 지시사항에 따라 적절한 이미지 변환을 수행하세요.
    img = Image.open("/Users/root-_-/Documents/GitLab/lecture-ai/220518/img/Lenna.png")

    # 이미지 밝게 하기
    img_bright = change_brightness(img, 1.5)

    # 이미지 어둡게 하기
    img_dark = change_brightness(img, 0.2)

    # 이미지 대조 늘리기
    img_high_contrast = change_contrast(img, 3)

    # 이미지 대조 줄이기
    img_low_contrast = change_contrast(img, 0.1)

    # 이미지 흑백 변환
    img_gray = change_grayscale(img)

    print("=" * 49, "밝은 이미지", "=" * 49)
    # show_image(img_bright, "bright.png")

    print("=" * 48, "어두운 이미지", "=" * 48)
    # show_image(img_dark, "dark.png")

    print("=" * 46, "강한 대조 이미지", "=" * 47)
    # show_image(img_high_contrast, "high_contrast.png")

    print("=" * 46, "약한 대조 이미지", "=" * 47)
    # show_image(img_low_contrast, "low_contrast.png")

    print("=" * 49, "흑백 이미지", "=" * 49)
    # show_image(img_gray, "gray.png")

    return img_bright, img_dark, img_high_contrast, img_low_contrast, img_gray


if __name__ == "__main__":
    main()
