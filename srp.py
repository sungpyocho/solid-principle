def get_total_stat(stats):
    '''5つのステータスの合計点数を出力'''
    total_stat = sum(stats.values())
    print(f"総合評価の点数は{total_stat}点です")

def get_highest_stat(stats):
    '''一番高いステータスの点数を出力'''
    highest_stat_name, highest_stat = max(stats.items(), key=lambda k: k[1])
    print(f"最も強いステータスは{highest_stat_name}で、{highest_stat}点です")

def main(stats):
    get_total_stat(stats)
    get_highest_stat(stats)

main({"スピード":963, "スタミナ":564, "パワー":1124, "根性":283, "賢さ":322})