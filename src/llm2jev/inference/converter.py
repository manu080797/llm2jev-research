from __future__ import annotations

from dataclasses import dataclass, field

from ..backend.base import BinaryBackend
from ..core.request import JevRequest
from ..core.response import JevResponse
from .assembler import Normalizer
from .normalization import normalize_l1
from .prompt import DefaultPromptRenderer, PromptRenderer
from .scoring import BinaryScorer, ScoringStrategy


@dataclass(slots=True, kw_only=True)
class LLM2Jev:
    """Evaluate Jev requests through an interchangeable scoring strategy."""

    backend: BinaryBackend | None = None
    scoring_strategy: ScoringStrategy | None = None
    renderer: PromptRenderer = field(default_factory=DefaultPromptRenderer)
    normalizer: Normalizer = normalize_l1

    def __post_init__(self) -> None:
        if self.backend is None and self.scoring_strategy is None:
            raise ValueError("backend or scoring_strategy is required")

    def evaluate(self, request: JevRequest) -> JevResponse:
        if self.scoring_strategy is not None:
            return self.scoring_strategy.score(request)

        assert self.backend is not None
        return BinaryScorer(
            backend=self.backend,
            renderer=self.renderer,
            normalizer=self.normalizer,
        ).score(request)
