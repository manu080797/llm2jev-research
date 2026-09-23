import unittest
from collections.abc import Sequence

from llm2jev import (
    BinaryBackendOutput,
    BinaryScorer,
    Choice,
    JevRequest,
    JevResponse,
    LLM2Jev,
    Noul,
    NoulAnswer,
    Usage,
)


class FakeBackend:
    def __init__(self, probabilities: Sequence[float]) -> None:
        self.probabilities = tuple(probabilities)
        self.calls = 0

    def score(self, *, model: str, prompts) -> BinaryBackendOutput:
        self.calls += 1
        return BinaryBackendOutput(
            yes_probabilities=self.probabilities,
            usage=Usage(input_tokens=12),
        )


class FixedStrategy:
    def __init__(self) -> None:
        self.requests: list[JevRequest] = []

    def score(self, request: JevRequest) -> JevResponse:
        self.requests.append(request)
        return JevResponse(
            model=request.model,
            answers={"check": NoulAnswer(noul=0.25)},
            usage=Usage(input_tokens=3),
        )


class BinaryScorerTests(unittest.TestCase):
    def test_scores_existing_binary_path(self) -> None:
        request = JevRequest(
            state="duplicate charge",
            model="test-model",
            questions={
                "department": Choice(criteria={"billing": None, "returns": None}),
                "check": Noul(),
            },
        )
        backend = FakeBackend([0.8, 0.2, 0.9])

        response = BinaryScorer(backend=backend).score(request)

        self.assertEqual(response.answers["department"].choice, "billing")
        self.assertEqual(response.answers["check"], NoulAnswer(noul=0.9))
        self.assertEqual(response.usage, Usage(input_tokens=12))
        self.assertEqual(backend.calls, 1)

    def test_llm2jev_accepts_strategy_without_binary_backend(self) -> None:
        request = JevRequest(
            state="message",
            model="test-model",
            questions={"check": Noul()},
        )
        strategy = FixedStrategy()

        response = LLM2Jev(scoring_strategy=strategy).evaluate(request)

        self.assertEqual(response.answers["check"], NoulAnswer(noul=0.25))
        self.assertEqual(strategy.requests, [request])

    def test_llm2jev_requires_backend_or_strategy(self) -> None:
        with self.assertRaisesRegex(ValueError, "backend or scoring_strategy"):
            LLM2Jev()


if __name__ == "__main__":
    unittest.main()
