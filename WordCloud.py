from os import path
from os import remove
from stylecloud import gen_stylecloud
import pandas as pd
from jieba import cut


def draw_words(
    data_word,
    title,
    no_word,
    words_counts,
    back_color,
    custom_palette,
    words_size,
    word_shape,
):
    ans = {}
    for d in data_word:
        words = cut(d, cut_all=False)
        for w in words:
            if w in ans and len(w) > 1 and w not in no_word:
                ans[w] += 1
            elif len(w) > 1:
                ans[w] = 1
    sorted_ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    ans.clear()
    for data in sorted_ans:
        ans[data[0]] = data[1]
    print(ans)
    words = pd.DataFrame(list(ans.items()), columns=["data", "counts"])
    words.dropna(subset=["data"])
    words = words[words["data"].apply(len) > 1]
    draw_word_cloud(
        words, title, words_counts, back_color, custom_palette, words_size, word_shape
    )


def draw_word_cloud(
    df,
    title,
    words_counts,
    back_color,
    custom_palette,
    words_size,
    word_shape,
):
    df_using = df.head(words_counts)
    f_path = "temp.csv"
    df_using.to_csv(f_path, index=False)
    output_path = "data/" + title + "词云.png"
    gen_stylecloud(
        file_path=f_path,
        size=1920,
        icon_name=word_shape,
        colors=custom_palette,
        background_color=back_color,
        max_words=len(df_using),
        max_font_size=words_size,
        font_path="仓耳与墨 W03.TTF",
        output_name=output_path,
    )
    if path.exists(f_path):
        remove(f_path)
    else:
        print("完蛋")
