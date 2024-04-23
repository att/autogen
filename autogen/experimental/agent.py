from __future__ import annotations

from typing import TYPE_CHECKING, AsyncGenerator, Protocol, Union, runtime_checkable

if TYPE_CHECKING:
    from .chat_history import ChatHistoryReadOnly
    from .types import GenerateReplyResult, IntermediateResponse


@runtime_checkable
class Agent(Protocol):
    """(In preview) A protocol for Agent.

    An agent can communicate with other agents and perform actions.
    Different agents can differ in what actions they perform in the `receive` method.
    """

    @property
    def name(self) -> str:
        """The name of the agent."""
        ...

    @property
    def description(self) -> str:
        """The description of the agent. Used for the agent's introduction in
        a group chat setting."""
        ...

    async def generate_reply(
        self,
        chat_history: ChatHistoryReadOnly,
    ) -> GenerateReplyResult: ...


@runtime_checkable
class AgentStream(Agent, Protocol):
    def stream_generate_reply(
        self,
        chat_history: ChatHistoryReadOnly,
    ) -> AsyncGenerator[Union[IntermediateResponse, GenerateReplyResult], None]: ...