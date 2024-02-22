import os, yaml, time
from pathlib import Path
from mutagen.mp3 import MP3

playlist_directory = 'source/playlists'
playlist_dict = dict()

cycle_info = {
    'c0': {
        '01': {
            'album': '狂熱之夜01 - 聚集於此',
            'youtube': 'https://www.youtube.com/watch?v=hVe-A8CJlyk&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/01 Zealot.png'
        },
        '02': {
            'album': '狂熱之夜02 - 午夜假面',
            'youtube': 'https://www.youtube.com/watch?v=MSpfvLlpLPM&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/01 Zealot.png'
        },
        '03': {
            'album': '狂熱之夜03 - 地底噬魔',
            'youtube': 'https://www.youtube.com/watch?v=_jFvhIf3htc&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/01 Zealot.png'
        }
    },
    'c1': {
        '01a': {
            'album': '敦威治遺產01A - 課外活動',
            'youtube': 'https://www.youtube.com/watch?v=rjcRlKZ0koI&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/02 Dunwich.png'
        },
        '01b': {
            'album': '敦威治遺產01B - 百賭百勝',
            'youtube': 'https://www.youtube.com/watch?v=h3zgpiyLiLU&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/02 Dunwich.png'
        },
        '02': {
            'album': '敦威治遺產02 - 博物館之夜',
            'youtube': 'https://www.youtube.com/watch?v=-ueigvINLfE&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/02 Dunwich.png'
        },
        '03': {
            'album': '敦威治遺產03 - 瘋狂列車',
            'youtube': 'https://www.youtube.com/watch?v=uvGD6VdJT60&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/02 Dunwich.png'
        }
    },
    'c2': {
        '01': {
            'album': '卡爾克薩之路01 - 謝幕',
            'youtube': 'https://www.youtube.com/watch?v=6QdNBnYISHA&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '02': {
            'album': '卡爾克薩之路02 - 最後的王者',
            'youtube': 'https://www.youtube.com/watch?v=xBkrloJZVYM&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '03': {
            'album': '卡爾克薩之路03 - 往事回聲',
            'youtube': 'https://www.youtube.com/watch?v=J3ohv9sU-JI&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '04': {
            'album': '卡爾克薩之路04 - 邪穢誓約',
            'youtube': 'https://www.youtube.com/watch?v=2TYDEv0pJkE&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '05': {
            'album': '卡爾克薩之路05 - 真相幻影',
            'youtube': 'https://www.youtube.com/watch?v=Cz0r-4K3wXc&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '06': {
            'album': '卡爾克薩之路06 - 蒼白面具',
            'youtube': 'https://www.youtube.com/watch?v=h9t-jS9wVb4&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '07': {
            'album': '卡爾克薩之路07 - 黑星升起',
            'youtube': 'https://www.youtube.com/watch?v=QIXA1XATAzc&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        },
        '08': {
            'album': '卡爾克薩之路08 - 卡城幽影',
            'youtube': 'https://www.youtube.com/watch?v=zhfOGy30uqM&list=PLECCPPx48krLv9zE37O2N8lKXDdXYtZZz',
            'cover': '/covers/03 Carcosa.png'
        }
    },
}

for root, dirs, files in os.walk(playlist_directory):
    cycle = os.path.normpath(root).split(os.sep)[-2]
    scene = os.path.normpath(root).split(os.sep)[-1]
    playlist = '-'.join([cycle, scene])
    songs = []
    for file in files:
        song = dict()
        song['name'] = Path(file).stem
        song['artist'] = '不可名狀的玩家'
        song['album'] = cycle_info[cycle][scene]['album']
        song['url'] = '/' + '/'.join(os.path.normpath(root).split(os.sep)[1:]) + '/' + file
        song['cover'] = cycle_info[cycle][scene]['cover']
        song['youtube'] = cycle_info[cycle][scene]['youtube']
        audio = MP3(os.path.join(root,file))
        song['duration'] = time.strftime("%M:%S", time.gmtime(audio.info.length))
        songs.append(song)
    if len(songs) > 0:
        playlist_dict[playlist] = songs

print(playlist_dict)

with open('source/_data/playlist-gen.yml', 'w', encoding='utf-8') as outfile:
    yaml.dump(playlist_dict, outfile, default_flow_style=False, allow_unicode=True, encoding="utf-8")