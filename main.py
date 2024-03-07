from os import makedirs
import pandas as pd

import data_process as dp
import WordCloud as wc
import key
import time
import sys
import clear


def main():
    user_key = input("输入密码：")
    if user_key != key.get_key():
        clear.clear_console()
        print("密码错误，你不是柠檬头！")
        time.sleep(10)
        sys.exit()
    print("密码正确，继续程序！")
    makedirs("data", exist_ok=True)
    file_path = input("输入文件位置:")  # E:/大学/宁静/东方甄选舆情事件.csv
    col_do = input("输入分析的列名:")  # 博文内容
    title = input("自己起一个文件名称:")  # 东方
    no_words = input("输入你不希望出现的词，两两之间空格隔开:")  # 东方
    words_counts = int(input("输入你希望出现的词语数量:"))  # 100
    back_color = input("输入你希望的背景颜色:")  # black
    words_color = input(
        "输入你希望出现的字体颜色，输入颜色编号，两两之间空格隔开:"
    )  # #FFA500 #FFFACD #FFAC6F #FAAC6A #FEA835 #ED8954 #D46C4F #FAB05A
    words_size = int(input("输入你希望的最大的字体大小，这个值越大，整体的字体大小越大:"))  # 150
    word_shape = input("输入你希望的词云形状:")  # fas fa-adjust
    data = pd.read_csv(
        file_path,
        encoding="gbk",
    )
    custom_palette = words_color.split(" ")
    no_word = no_words.split(" ")
    df = dp.data_process(data, col_do)
    wc.draw_words(
        df,
        title,
        no_word,
        words_counts,
        back_color,
        custom_palette,
        words_size,
        word_shape,
    )
    pass


if __name__ == "__main__":
    main()
