from schema.adventure_schema import AdventureSchema, ValidationError
import json

llm_output = {
    "activity_name": "Kayaking Adventure",
    "platform": "BookMyShow",
    "location": "Bengaluru",
    "category": "Water Sports",
    "duration": "2 hours",
    "price": "INR 1500",
    "rating": 4.8,
    "link": "https://in.bookmyshow.com/explore/adventure-bengaluru",
    "image": "https://example.com/image.jpg"
}

def validate_schema(data: dict):
    try:
        item = AdventureSchema(**data)
        return item.dict()
    except ValidationError as e:
        print("Validation Error:", e)
        return None

if __name__ == "__main__":
    validated = validate_schema(llm_output)
    if validated:
        with open("output/final_json/bookmyshow_adventure.json", "w", encoding="utf-8") as f:
            json.dump(validated, f, indent=2)
