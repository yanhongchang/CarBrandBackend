import json


class CarbrandResource(object):

    def __init__(self, carbrand):
        self.carbrand = carbrand

    def to_list_dict(self):
        data = {
            "id": self.carbrand.carbrand_id,
            "img": self.carbrand.img,
            "name": self.carbrand.name_cn,
            "country": self.carbrand.country.country_name_cn,
            "countryId": self.carbrand.country.country_id,
            "ranking": self.carbrand.ranking,
            "level": self.carbrand.level
        }
        return data

    def to_detail_dict(self):

        data = {
            "id": self.carbrand.carbrand_id,
            "img": self.carbrand.img,
            "coverImg": self.carbrand.img,
            "name": self.carbrand.name_cn,
            "country": self.carbrand.country.country_name_cn,
            "countryId": self.carbrand.country.country_id,
            "introduction": self.carbrand.introduction,
            "series": []
        }
        return data
