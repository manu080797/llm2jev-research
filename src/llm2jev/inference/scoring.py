from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol

from ..backend.base import BinaryBackend
from ..core.request import JevRequest
from ..core.response import JevResponse
from .assembler import Normalizer, assemble_response
from .binary import compile_binary_questions
from .normalization import normalize_l1
from .prompt import DefaultPromptRenderer, PromptRenderer


class ScoringStrategy(Protocol):
    """Turn a Jev request into a scored Jev response."""

    def score(self, request: JevRequest) -> JevResponse:
        """Score one request."""


@dataclass(slots=True, kw_only=True)
class BinaryScorer:
    """Existing independent yes/no scoring strategy."""

    backend: BinaryBackend
    renderer: PromptRenderer = field(default_factory=DefaultPromptRenderer)
    normalizer: Normalizer = normalize_l1

    def score(self, request: JevRequest) -> JevResponse:
        tasks = compile_binary_questions(request)
        prompts = tuple(self.renderer.render(task) for task in tasks)
        output = self.backend.score(model=request.model, prompts=prompts)
        return assemble_response(
            request=request,
            tasks=tasks,
            yes_probabilities=output.yes_probabilities,
            usage=output.usage,
            normalizer=self.normalizer,
        )
