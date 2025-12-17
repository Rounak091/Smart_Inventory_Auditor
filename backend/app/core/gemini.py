import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

lookup_tool = genai.protos.Tool(
    function_declarations=[
        genai.protos.FunctionDeclaration(
            name="lookup_inventory",
            description="Look up inventory details for a given item name",
            parameters=genai.protos.Schema(
                type=genai.protos.Type.OBJECT,
                properties={
                    "item_name": genai.protos.Schema(
                        type=genai.protos.Type.STRING,
                        description="The name of the item to look up in inventory"
                    )
                },
                required=["item_name"]
            )
        )
    ]
)

model = genai.GenerativeModel(
    model_name=settings.MODEL_NAME,
    tools=[lookup_tool]
)

SYSTEM_PROMPT = """
You are an enterprise-grade Smart Inventory Auditor.

Instructions:
- Analyze the provided image.
- Identify ONE primary item.
- Call the inventory lookup function.
- Return ONLY a single JSON object with:
  item_detected,
  category,
  inventory_status,
  quantity,
  recommended_action

No explanations.
No markdown.
Only valid JSON.
"""
