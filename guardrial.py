from typing import List
from pydantic import BaseModel
from agents import (
    input_guardrail,
    output_guardrail,
    GuardrailFunctionOutput,
    RunContextWrapper,
    Runner,
)
from agents.agent import Agent
from agents import TResponseInputItem

# ---------------------------
# 👀 Input Guardrail Model
# ---------------------------

class HealthInputCheckOutput(BaseModel):
    is_valid: bool
    reasoning: str

# Guardrail agent to validate user input
input_check_agent = Agent(
    name="Input Quality Checker",
    instructions="Check if the user's input is detailed and relevant for a health assistant. Must be at least 10 characters and meaningful.",
    output_type=HealthInputCheckOutput,
)

# @input_guardrail(name="HealthPlannerInputGuard")
# async def health_input_guardrail(
#     ctx: RunContextWrapper[None],
#     agent: Agent,
#     input: str | List[TResponseInputItem]
# ) -> GuardrailFunctionOutput:
#     result = await Runner.run(input_check_agent, input, context=ctx.context)
#     return GuardrailFunctionOutput(
#         output_info=result.final_output,
#         tripwire_triggered=not result.final_output.is_valid
#     )


@input_guardrail(name="HealthPlannerInputGuard")
async def health_input_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | List[TResponseInputItem]
) -> GuardrailFunctionOutput:
    try:
        result = await Runner.run(input_check_agent, input, context=ctx.context)

        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=not result.final_output.is_valid
        )

    except Exception as e:
        print(f"[Guardrail Error] Input validation failed: {e}")

        # Return a fallback result to indicate invalid input
        return GuardrailFunctionOutput(
            output_info=HealthInputCheckOutput(
                is_valid=False,
                reasoning="Input validation failed due to an internal error."
            ),
            tripwire_triggered=True
        )


# ---------------------------
# ✅ Output Guardrail Model
# ---------------------------

class HealthOutputValidation(BaseModel):
    is_safe: bool
    summary: str

# Output validation agent
output_check_agent = Agent(
    name="Output Quality Checker",
    instructions="Check if the health assistant's response is safe, non-medical, and appropriate for general wellness advice.",
    output_type=HealthOutputValidation,
)

# # @output_guardrail(name="HealthPlannerOutputGuard")
# # async def health_output_guardrail(
#     ctx: RunContextWrapper[None],
#     agent: Agent,
#     output: str
# ) -> GuardrailFunctionOutput:
#     result = await Runner.run(output_check_agent, output, context=ctx.context)

#     try:

#         return GuardrailFunctionOutput(
#             output_info=result.final_output,
#             tripwire_triggered=not result.final_output.is_safe
#         )
    
#     except :
#         print([])
@output_guardrail(name="HealthPlannerOutputGuard")
async def health_output_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    output: str
) -> GuardrailFunctionOutput:
    try:
        result = await Runner.run(output_check_agent, output, context=ctx.context)

        return GuardrailFunctionOutput(
            output_info=result.final_output,
            tripwire_triggered=not result.final_output.is_safe
        )

    except Exception as e:
        print(f"[Guardrail Error] Output validation failed: {e}")

        # Return a fallback result to maintain system stability
        return GuardrailFunctionOutput(
            output_info=HealthOutputValidation(
                is_safe=False,
                summary="Validation could not be completed due to an internal error."
            ),
            tripwire_triggered=True
        )
