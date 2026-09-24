import importlib.util
import unittest
from pathlib import Path

from llm2jev import (
    ChoiceAnswer,
    JevResponse,
    NoulAnswer,
    ScoreAnswer,
    Usage,
)


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "benchmarks" / "run_baseline.py"

spec = importlib.util.spec_from_file_location("run_baseline", RUNNER)
assert spec is not None and spec.loader is not None
run_baseline = importlib.util.module_from_spec(spec)
spec.loader.exec_module(run_baseline)


class BaselineRunnerTests(unittest.TestCase):
    def test_scores_choice_noul_and_score_predictions(self) -> None:
        choice = JevResponse(
            model="m",
            answers={
                "answer": ChoiceAnswer(
                    choice="b",
                    confidence=0.5,
                    probabilities={"a": 0.25, "b": 0.75},
                )
            },
            usage=Usage(),
        )
        noul = JevResponse(
            model="m",
            answers={"answer": NoulAnswer(noul=0.49)},
            usage=Usage(),
        )
        score = JevResponse(
            model="m",
            answers={
                "answer": ScoreAnswer(
                    score=2.6,
                    confidence=0.5,
                    legend={0: "a", 1: "b", 2: "c", 3: "d"},
                    probabilities={0: 0.0, 1: 0.0, 2: 0.4, 3: 0.6},
                )
            },
            usage=Usage(),
        )

        self.assertEqual(
            run_baseline._score_prediction(
                choice, {"question_id": "answer", "target": "b"}
            ),
            {"prediction": "b", "correct": True},
        )
        self.assertEqual(
            run_baseline._score_prediction(
                noul, {"question_id": "answer", "target": False}
            ),
            {
                "prediction": False,
                "correct": True,
                "noul_probability": 0.49,
            },
        )

        scored = run_baseline._score_prediction(
            score, {"question_id": "answer", "target": 3}
        )
        self.assertEqual(scored["rounded_level"], 3)
        self.assertTrue(scored["correct"])
        self.assertAlmostEqual(scored["absolute_error"], 0.4)

    def test_loads_compact_workload(self) -> None:
        workload = run_baseline._load_workload(
            ROOT / "benchmarks" / "compact_jev_v1.json"
        )
        self.assertEqual(workload["name"], "compact-jev")
        self.assertGreaterEqual(len(workload["cases"]), 8)


if __name__ == "__main__":
    unittest.main()
