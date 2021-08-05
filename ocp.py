from abc import ABC, abstractmethod

class StatOperations(ABC):
    '''抽象クラス'''
    @abstractmethod
    def operation():
        pass

class TotalStat(StatOperations):
    def operation(stats):
        '''5つのステータスの合計点数を出力'''
        total_stat = sum(stats.values())
        print(f"総合評価の点数は{total_stat}点です")

class HighestStat(StatOperations):
    def operation(stats):
        '''一番高いステータスの点数を出力'''
        highest_stat_name, highest_stat = max(stats.items(), key=lambda k: k[1])
        print(f"最も強いステータスは{highest_stat_name}で、{highest_stat}点です")

class AverageStat(StatOperations):
    def operation(stats):
        '''5つのステータスの平均値を出力'''
        avg_stat = sum(stats.values()) / len(stats)
        print(f"{avg_stat}点より低いステータスは、重点的に管理しましょう")

class Main:
    def do_operations(stats):
        # __subclasses__はStatOperationsのすべてのサブクラスを探す
        for operation in StatOperations.__subclasses__():
            operation.operation(stats)
      
if __name__ == "__main__":
    Main.do_operations({"スピード":963, "スタミナ":564, "パワー":1124, "根性":283, "賢さ":322})