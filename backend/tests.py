import unittest
from models import Benchmark, Usecase
from app import app, db

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client
        self.ctx = self.app.app_context()
        self.ctx.push()
        self.db = db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.ctx.pop()

    def test_benchmark_to_json(self):
        benchmark = Benchmark(name='Test Benchmark', subject='Test Subject')
        self.db.session.add(benchmark)
        self.db.session.commit()

        expected_json = {
            'id': benchmark.id,
            'name': 'Test Benchmark',
            'subject': 'Test Subject',
            'use_cases': [],
            'notes': None
        }
        self.assertEqual(benchmark.to_json(), expected_json)

    def test_usecase_to_json(self):
        usecase = Usecase(name='Test Usecase')
        self.db.session.add(usecase)
        self.db.session.commit()

        expected_json = {
            'id': usecase.id,
            'name': 'Test Usecase'
        }
        self.assertEqual(usecase.to_json(), expected_json)

if __name__ == "__main__":
    unittest.main()