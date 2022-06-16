from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/', serverSelectionTimeoutMS=3000)
db = client['squirro']        

class DBManipulation(): 

    @staticmethod
    def get_all_texts() -> list:

        all_texts = db.texts.find()

        return list(all_texts)


    @staticmethod
    def get_text_by_id(id: int) -> dict:

        specific_text = db.texts.find_one({'_id': id})

        return specific_text


    @classmethod
    def get_new_id(cls) -> int:

        all_texts_list = cls.get_all_texts()

        if not all_texts_list:

            new_id = 1

            return new_id

        all_texts_list = list(all_texts_list)

        last_id = all_texts_list[-1].get('_id')

        new_id = last_id + 1

        return new_id


    @classmethod
    def save(cls, data: str) -> int:

        target_new_id = cls.get_new_id() 

        data_to_save = {'text': data, '_id': target_new_id}

        db.texts.insert_one(data_to_save)

        return target_new_id


    def delete_a_text(self, id: int) -> dict:

        deleted_text = db.texts.find_one_and_delete({'_id': id})

        return deleted_text
