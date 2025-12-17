
from PIL import Image
from app.core.gemini import model, SYSTEM_PROMPT
from app.services.inventory_service import lookup_inventory
import json

def audit_image(image_path: str):
    image = Image.open(image_path)

    response = model.generate_content(
        [SYSTEM_PROMPT, image]
    )

    # Check for function calls
    if response.candidates and response.candidates[0].content.parts:
        for part in response.candidates[0].content.parts:
            if hasattr(part, 'function_call') and part.function_call:
                function_call = part.function_call
                if function_call.name == "lookup_inventory":
                    item_name = function_call.args.get("item_name")
                    if item_name:
                        inventory_result = lookup_inventory(item_name)

                        # Create a follow-up message with the function result
                        follow_up_prompt = f"""
                        Based on the inventory lookup result: {json.dumps(inventory_result)}

                        Now provide the final analysis as a JSON object with:
                        item_detected, category, inventory_status, quantity, recommended_action
                        """

                        follow_up_response = model.generate_content(
                            [follow_up_prompt, image]
                        )
                        return follow_up_response.text

    return response.text
