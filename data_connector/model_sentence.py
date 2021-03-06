import data_connector.model
import analyser.caption
import re


class ModelSentence(data_connector.model.Model):
    @property
    def s_id(self):
        return self.__s_id

    @s_id.setter
    def s_id(self, value: int):
        self.__s_id = value

    @property
    def s_en(self):
        return self.__s_en

    @s_en.setter
    def s_en(self, value: str):
        self.__s_en = value

    @property
    def s_cn(self):
        return self.__s_cn

    @s_cn.setter
    def s_cn(self, value: str):
        self.__s_cn = value

    @property
    def s_voice(self):
        if self.__s_voice:
            return "'%s'" % self.__s_voice.replace("\\", '\\\\')
        else:
            return 'null'

    @s_voice.setter
    def s_voice(self, value: str):
        self.__s_voice = value

    @property
    def s_level(self):
        return self.__s_level

    @s_level.setter
    def s_level(self, value: int):
        self.__s_level = value

    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self, value: str):
        self.__f_name = value

    def to_sql(self):
        return "insert into t_sentence values (%s,'%s','%s',%s,%s,'%s')" \
               % (str(self.s_id), self.s_en, self.s_cn, self.s_voice, str(self.s_level), self.f_name)

    def __init__(self, id: int, caption: analyser.caption.Caption, f_name: str, level: int, voice_path: str = None):
        self.__s_id = id
        self.__s_en = caption.english.replace('\'', '\\\'')
        self.__s_cn = caption.chinese.replace('\'', '\\\'')
        self.__f_name = f_name
        self.__s_level = level
        self.s_voice = voice_path
