import bs4
import requests

def get_torrents_api(keyword,i):
    result_json = "{\"data\":["
    headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36Query String Parametersview sourceview URL encoded"
               }
    url = "https://www.btmule.org/q/" + keyword + ".html?sort=rel&page=" + str(i)
    res = requests.get(url,headers = headers)
    res = bs4.BeautifulSoup(res.text,"html.parser")
    results = res.findAll(attrs={"class":"search-item"})
    for result in results:
        print("链接：",result.a['href'][8:])
        result_json += "{\"url\": \"" + result.a['href'][8:] + "\","
        print("名字：",result.a.get_text())
        result_json += "\"name\": " + "\"" + result.a.get_text() + "\","
        dets = result.findAll('span')
        a = 0
        for det in dets:
            a += 1
            if a == 1:
                print("类型",det.get_text()[1:])
                result_json += "\"type\":" + "\"" + det.get_text()[1:] + "\","
                continue
            if a == 2:
                print("时间",det.b.get_text())
                result_json += "\"time\":" + "\"" + det.b.get_text() + "\","
                continue
            if a == 3:
                print("大小",det.b.get_text())
                result_json += "\"size\":" + "\"" + det.b.get_text() + "\","
                continue
            if a == 4:
                print("热度",det.b.get_text())
                result_json += "\"like\":" + "\"" + det.b.get_text() + "\"},"
                continue
    return result_json[:-1]+"]}"
def get_torrent(url):
    headers = {"User-Agent":
                   "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36Query String Parametersview sourceview URL encoded"
               }
    url1 = "https://www.btmule.org/torrent/" + url
    res = requests.get(url1, headers=headers)
    res = bs4.BeautifulSoup(res.text, "html.parser")
    result = "{\"data\":{\"url\":\"" + res.find(attrs={'id':"m_link"}).get_text() + "\"}}"
    return result

if __name__ == "__main__":
    url = "8db47b995a13663cdca9bee49b114355a4b3a3b7.html"
    print(get_torrent(url))
    #print(get_torrents_api("水形物语",1))



    #{"data":[{"url": "https://www.btmule.org/torrent/8db47b995a13663cdca9bee49b114355a4b3a3b7.html","name": "水形物语.The.Shape.Of.Water.2017.WEB-1080p.X264.AAC-99","type":"mp4","time":"2018-02-27","size":"2.4 GB","like":"4432"},{"url": "https://www.btmule.org/torrent/cdbc9cc3b501e20ed54a5ebe25023d4a192e3a49.html","name": "水形物语.The Shape of Water.DVDScr.2017-Forever24","type":"mkv","time":"2018-02-10","size":"3.2 GB","like":"3546"},{"url": "https://www.btmule.org/torrent/12469d4fb1c540b3231cb9312d08d6d7f7289a94.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-31","size":"1.6 GB","like":"2304"},{"url": "https://www.btmule.org/torrent/e15d5d7ce59434233223f4ef41824a20a6073209.html","name": "水形物语.2017.BD1280高清中字-www.987.cm.mp4","type":"mp4","time":"2018-01-24","size":"1.4 GB","like":"2887"},{"url": "https://www.btmule.org/torrent/37f0d406600372b57ce36157bea98c9b1cebda98.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"733"},{"url": "https://www.btmule.org/torrent/21e9e3d4a3c84588d6a55b7037adf783beb9d8f6.html","name": "水形物语.The.Shape.of.Water.2017.中英字幕.DVDScr.AAC.720x3","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"956"},{"url": "https://www.btmule.org/torrent/eb46a3c863e04ae0990f85d29de34a0935b4a73b.html","name": "水形物语.The.Shape.of.Water.2017.DVD.X264.AAC-99Mp4.mp","type":"mp4","time":"2018-01-18","size":"981 MB","like":"273"},{"url": "https://www.btmule.org/torrent/e869313941b2c97185bf0c68c8ab20d9d237c317.html","name": "水形物语 The Shape of Water HD MP4 2017 美国 剧情 奇幻 冒险 中文","type":"mp4","time":"2018-01-17","size":"1.9 GB","like":"1125"},{"url": "https://www.btmule.org/torrent/c39d9b9425063f8ee0e0f70e88ca3063fab768b2.html","name": "水形物语.The.Shape.of.Water.2017.DVD.x264.英语中字.eng.chs","type":"mkv","time":"2018-01-15","size":"1.7 GB","like":"847"},{"url": "https://www.btmule.org/torrent/ca5087084f1a1b9f7584ac47a93e5b89bdccb82f.html","name": "[2018.03.01]水形物语[2017年美国奇幻爱情(MKV)]（帝国出品）","type":"mkv","time":"2018-03-01","size":"2.9 GB","like":"6994"}]}
    #{"data":[{"url": "https://www.btmule.org/torrent/8db47b995a13663cdca9bee49b114355a4b3a3b7.html","name": "水形物语.The.Shape.Of.Water.2017.WEB-1080p.X264.AAC-99","type":"mp4","time":"2018-02-27","size":"2.4 GB","like":"4432"},{"url": "https://www.btmule.org/torrent/cdbc9cc3b501e20ed54a5ebe25023d4a192e3a49.html","name": "水形物语.The Shape of Water.DVDScr.2017-Forever24","type":"mkv","time":"2018-02-10","size":"3.2 GB","like":"3546"},{"url": "https://www.btmule.org/torrent/12469d4fb1c540b3231cb9312d08d6d7f7289a94.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-31","size":"1.6 GB","like":"2304"},{"url": "https://www.btmule.org/torrent/e15d5d7ce59434233223f4ef41824a20a6073209.html","name": "水形物语.2017.BD1280高清中字-www.987.cm.mp4","type":"mp4","time":"2018-01-24","size":"1.4 GB","like":"2889"},{"url": "https://www.btmule.org/torrent/37f0d406600372b57ce36157bea98c9b1cebda98.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"733"},{"url": "https://www.btmule.org/torrent/21e9e3d4a3c84588d6a55b7037adf783beb9d8f6.html","name": "水形物语.The.Shape.of.Water.2017.中英字幕.DVDScr.AAC.720x3","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"956"},{"url": "https://www.btmule.org/torrent/eb46a3c863e04ae0990f85d29de34a0935b4a73b.html","name": "水形物语.The.Shape.of.Water.2017.DVD.X264.AAC-99Mp4.mp","type":"mp4","time":"2018-01-18","size":"981 MB","like":"273"},{"url": "https://www.btmule.org/torrent/e869313941b2c97185bf0c68c8ab20d9d237c317.html","name": "水形物语 The Shape of Water HD MP4 2017 美国 剧情 奇幻 冒险 中文","type":"mp4","time":"2018-01-17","size":"1.9 GB","like":"1125"},{"url": "https://www.btmule.org/torrent/c39d9b9425063f8ee0e0f70e88ca3063fab768b2.html","name": "水形物语.The.Shape.of.Water.2017.DVD.x264.英语中字.eng.chs","type":"mkv","time":"2018-01-15","size":"1.7 GB","like":"848"},{"url": "https://www.btmule.org/torrent/ca5087084f1a1b9f7584ac47a93e5b89bdccb82f.html","name": "[2018.03.01]水形物语[2017年美国奇幻爱情(MKV)]（帝国出品）","type":"mkv","time":"2018-03-01","size":"2.9 GB","like":"6998"},{"data":[{"url": "https://www.btmule.org/torrent/8db47b995a13663cdca9bee49b114355a4b3a3b7.html","name": "水形物语.The.Shape.Of.Water.2017.WEB-1080p.X264.AAC-99","type":"mp4","time":"2018-02-27","size":"2.4 GB","like":"4432"},{"url": "https://www.btmule.org/torrent/cdbc9cc3b501e20ed54a5ebe25023d4a192e3a49.html","name": "水形物语.The Shape of Water.DVDScr.2017-Forever24","type":"mkv","time":"2018-02-10","size":"3.2 GB","like":"3546"},{"url": "https://www.btmule.org/torrent/12469d4fb1c540b3231cb9312d08d6d7f7289a94.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-31","size":"1.6 GB","like":"2304"},{"url": "https://www.btmule.org/torrent/e15d5d7ce59434233223f4ef41824a20a6073209.html","name": "水形物语.2017.BD1280高清中字-www.987.cm.mp4","type":"mp4","time":"2018-01-24","size":"1.4 GB","like":"2889"},{"url": "https://www.btmule.org/torrent/37f0d406600372b57ce36157bea98c9b1cebda98.html","name": "水形物语.The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hi","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"733"},{"url": "https://www.btmule.org/torrent/21e9e3d4a3c84588d6a55b7037adf783beb9d8f6.html","name": "水形物语.The.Shape.of.Water.2017.中英字幕.DVDScr.AAC.720x3","type":"mp4","time":"2018-01-20","size":"1.5 GB","like":"956"},{"url": "https://www.btmule.org/torrent/eb46a3c863e04ae0990f85d29de34a0935b4a73b.html","name": "水形物语.The.Shape.of.Water.2017.DVD.X264.AAC-99Mp4.mp","type":"mp4","time":"2018-01-18","size":"981 MB","like":"273"},{"url": "https://www.btmule.org/torrent/e869313941b2c97185bf0c68c8ab20d9d237c317.html","name": "水形物语 The Shape of Water HD MP4 2017 美国 剧情 奇幻 冒险 中文","type":"mp4","time":"2018-01-17","size":"1.9 GB","like":"1125"},{"url": "https://www.btmule.org/torrent/c39d9b9425063f8ee0e0f70e88ca3063fab768b2.html","name": "水形物语.The.Shape.of.Water.2017.DVD.x264.英语中字.eng.chs","type":"mkv","time":"2018-01-15","size":"1.7 GB","like":"848"},{"url": "https://www.btmule.org/torrent/ca5087084f1a1b9f7584ac47a93e5b89bdccb82f.html","name": "[2018.03.01]水形物语[2017年美国奇幻爱情(MKV)]（帝国出品）","type":"mkv","time":"2018-03-01","size":"2.9 GB","like":"6998"}]}
