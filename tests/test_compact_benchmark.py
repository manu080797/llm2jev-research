import json
import unittest
from pathlib import Path

from llm2jev import Choice, Noul, Score
from llm2jev.sglang_server import _parse_request


ROOT = Path(__file__).resolve().parents[1]
WORKLOAD = ROOT / "benchmarks" / "compact_jev_v1.json"
RESULT_SCHEMA = ROOT / "benchmarks" / "result.schema.json"


class CompactBenchmarkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.workload = json.loads(WORKLOAD.read_text(encoding="utf-8"))

    def test_workload_has_unique_cases_and_expected_coverage(self) -> None:
        cases = self.workload["cases"]
        ids = [case["id"] for case in cases]

        self.assertEqual(self.workload["name"], "compact-jev")
        self.assertEqual(self.workload["version"], "1")
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(cases), 8)

        tags = {tag for case in cases for tag in case["tags"]}
        for expected in {
            "noul",
            "choice",
            "score",
            "short-context",
            "long-context",
            "unequal-candidate-length",
            "moderate-option-count",
        }:
            self.assertIn(expected, tags)

    def test_every_case_is_a_valid_single_question_jev_request(self) -> None:
        for case in self.workload["cases"]:
            with self.subTest(case=case["id"]):
                request = _parse_request(case["request"])
                self.assertEqual(request.model, "__MODEL__")
                self.assertEqual(len(request.questions), 1)

                reference = case["reference"]
                self.assertIn(reference["question_id"], request.questions)
                question = request.questions[reference["question_id"]]

                if isinstance(question, Choice):
                    self.assertEqual(reference["type"], "choice")
                    self.assertIn(reference["target"], question.criteria)
                elif isinstance(question, Noul):
                    self.assertEqual(reference["type"], "noul")
                    self.assertIsInstance(reference["target"], bool)
                elif isinstance(question, Score):
                    self.assertEqual(reference["type"], "score")
                    target = reference["target"]
                    self.assertIsInstance(target, int)
                    self.assertFalse(isinstance(target, bool))
                    self.assertIn(target, range(len(question.criteria)))
                else:
                    self.fail(f"unsupported question type: {type(question).__name__}")

    def test_result_schema_keeps_training_exposure_and_device_mode_explicit(self) -> None:
        schema = json.loads(RESULT_SCHEMA.read_text(encoding="utf-8"))
        system = schema["properties"]["system"]

        self.assertIn("training_exposure", system["required"])
        self.assertIn("device_mode", system["required"])
        self.assertEqual(
            system["properties"]["training_exposure"]["enum"],
            [
                "zero-training",
                "general-trained-specialist",
                "task-finetuned-specialist",
                "unknown",
            ],
        )
        self.assertEqual(
            system["properties"]["device_mode"]["enum"],
            ["cpu", "gpu", "hybrid", "unknown"],
        )


if __name__ == "__main__":
    unittest.main()
