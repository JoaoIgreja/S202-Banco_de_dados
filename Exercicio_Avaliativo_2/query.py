from database import Database


class Query:
    def __init__(self, db):
        self.db = db

    def question_1(self):
        query = """
        MATCH (t:Teacher {name: 'Renzo'})
        RETURN t.ano_nasc, t.cpf
        """
        return self.db.run(query)

    def question_2(self):
        query = """
        MATCH (t:Teacher)
        WHERE t.name STARTS WITH 'M'
        RETURN t.name, t.cpf
        """
        return self.db.run(query)

    def question_3(self):
        query = """
        MATCH (c:City)
        RETURN c.name
        """
        return self.db.run(query)

    def question_4(self):
        query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550
        RETURN s.name, s.address, s.number
        """
        return self.db.run(query)

    def question_5(self):
        query = """
        MATCH (t:Teacher)
        RETURN MIN(t.ano_nasc) AS youngest, MAX(t.ano_nasc) AS oldest
        """
        return self.db.run(query)

    def question_6(self):
        query = """
        MATCH (c:City)
        RETURN AVG(c.population) AS average_population
        """
        return self.db.run(query)

    def question_7(self):
        query = """
        MATCH (c:City {cep: '37540-000'})
        RETURN REPLACE(c.name, 'a', 'A') AS modified_name
        """
        return self.db.run(query)

    def question_8(self):
        query = """
        MATCH (t:Teacher)
        RETURN SUBSTRING(t.name, 3, 1) AS third_character
        """
        return self.db.run(query)
