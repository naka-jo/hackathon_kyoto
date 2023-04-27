def change_railway(name):
    dict_railway = {
        '東京メトロ丸の内線': 'TokyoMetro.Marunouchi', '東京メトロ銀座線': 'TokyoMetro.Ginza', '東京メトロ千代田線': 'TokyoMetro.Chiyoda', '東京メトロ東西線': 'TokyoMetro.Tozai', '東京メトロ南北線': 'TokyoMetro.Namboku', '東京メトロ日比谷線': 'TokyoMetro.Hibiya', '東京メトロ半蔵門線': 'TokyoMetro.Hanzomon', '東京メトロ副都心線': 'TokyoMetro.Fukutoshin', '東京メトロ有楽町線': 'TokyoMetro.Yurakucho', 
        '都営三田線': 'Toei.Mita', '都営新宿線': 'Toei.Shinjuku', '都営浅草線': 'Toei.Asakusa', '都営大江戸線': 'Toei.Oedo', '都電荒川線': 'Toei.Arakawa', '日暮里・舎人ライナー': 'Toei.NipporiToneri', '横浜市営地下鉄ブルーライン': 'YokohamaMunicipal.Blue', '横浜市営地下鉄グリーンライン': 'YokohamaMunicipal.Green', '東京臨海高速鉄道りんかい線': 'TWR.Rinkai', 'つくばエクスプレス': 'MIR.TsukubaExpress', '多摩モノレール': 'TamaMonorail.TamaMonorail'}
    return dict_railway[name]