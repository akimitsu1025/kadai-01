### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました。".format(word))
    else:
        print("{}は見つかりませんでした".format(word))
        print('{}を鬼滅の登場人物に追加します。'.format(word))
        source.append(word)
        print(source)

# csv読み込み
with open('search_read.csv', 'r', encoding = 'utf-8-sig') as f:
    people = f.read()
    print(people)

# csv書き込み
with open('search_write.csv', 'w', encoding = 'utf-8-sig') as f:
    f.write(people)

if __name__ == "__main__":
    search()