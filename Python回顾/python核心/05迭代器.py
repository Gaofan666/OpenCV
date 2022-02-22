# 技能类
class Skill:
    pass


# 技能迭代器
class Skill_Iterator:
    def __init__(self, target):  # target:迭代对象
        self.__target = target
        self.__inidex = 0

    def __next__(self):
        # 当前索引比最大索引还大 停止迭代
        if self.__inidex > len(self.__target)-1:
            raise StopIteration
        # 返回下一个数据
        temp = self.__target[self.__inidex]
        self.__inidex += 1
        return temp


# 技能管理
class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):  # 有这个才可以for
        # 创建一个迭代器对象,并传递需要迭代的数据
        return Skill_Iterator(self.__skills)


manager = SkillManager()
manager.add_skill(Skill())
manager.add_skill(Skill())
manager.add_skill(Skill())

iterator = manager.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break
