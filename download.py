from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os,time,sys
import tkinter

class flicker_class(): 

    def flicker_down(self): 


        f = open('../flickerkey.txt', 'r')
        datalist = f.readlines()

        print (datalist[0])
        print (datalist[1])
        
        key = datalist[0].rstrip('\n')
        secret = datalist[1].rstrip('\n')
        wait_time = 1

        # コマンドラインの引数の1番目の値を取得。以下の場合は[cat]を取得
        # python download.py cat 
        animalname = self.get_data
        savedir = "../"+animalname

        if(os.path.isdir(savedir)==False):
            os.makedirs(savedir)

        # format:受け取るデータ(jsonで受け取る）
        flickr = FlickrAPI(key, secret, format='parsed-json')

        """
        text : 検索キーワード
        per_page : 取得したいデータの件数
        media : 検索するデータの種類
        sort : データの並び
        safe_seach :　UIコンテンツの表示有無
        extras : 取得したいオプションの値(url_q 画像のアドレス情報)
        """
        result  = flickr.photos.search(
            text = animalname,
            per_page = 10,
            media = 'photos',
            sort = 'relevance',
            safe_seach = 1,
            extras = 'url_q, licence'
        )

    # 結果  
        photos = result['photos']
        pprint(photos)


        for i,photo in enumerate(photos['photo']):
            url_q = photo['url_q']
            filepath = savedir + '/' + photo['id'] + '.jpg'

            # 重複したファイルが存在する場合スキップする。
            if os.path.exists(filepath):continue
            # 画像データをダウンロードする
            urlretrieve(url_q, filepath)
            # サーバーに負荷がかからないよう、1秒待機する
            time.sleep(wait_time)


    # clickイベント
    def btn_click(self):
        #入力文字列を獲得する
        self.get_data =self.txt.get()
        #出力エリアをクリアする
        self.txt2.delete(0, tkinter.END)
        #出力エリアにエコーする

        self.flicker_down()
        self.txt2.insert(tkinter.END,"完了")
    #基本となるフレームをインスタンス
    def main(self):
        root = tkinter.Tk()

        # ボタン 
        # commandのオプションはボタンを押した場合の動作を指定します

        btn = tkinter.Button(root, text='実行', command=self.btn_click)
        btn.place(x=140, y=170)


        # 画面サイズ
        root.geometry('300x200')
        # 画面タイトル
        root.title('Flicker ダウンロード')

        # ラベル
        lbl = tkinter.Label(text='検索ワード')
        lbl.place(x=10, y=70)

        lbl2 = tkinter.Label(text='経過')
        lbl2.place(x=10, y=100)

        # テキストボックス
        #ウイジット作成　部品のこと
        self.txt = tkinter.Entry(width=20)
        #場所決め
        self.txt.place(x=90, y=70)
        #文字初期値挿入
        self.txt.insert(tkinter.END,"dog")

        self.txt2 = tkinter.Entry(width=20)
        self.txt2.place(x=90, y=100)


        # 表示
        root.mainloop()



c=flicker_class()
c.main()